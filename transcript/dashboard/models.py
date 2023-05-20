from django.db import models
from django.db.models import ImageField
# Create your models here.

class academicyear(models.Model):
    academicyear = models.CharField(max_length=100, unique=True,null=True)
    def __str__(self):
        return self.academicyear

#SUBJECT:
class Class(models.Model):
    classid = models.IntegerField(primary_key=True)
    classname = models.CharField(max_length=50)
    credit = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.classname

#GRADE:
class Year(models.Model):
    yearid = models.AutoField(primary_key=True)
    YEAR_CHOICES = (
        (9, '9th'),
        (10, '10th'),
        (11, '11th'),
        (12, '12th'),
    )

    year = models.IntegerField(choices=YEAR_CHOICES)

    def __str__(self):
        return f"{self.year}"


class Student(models.Model):
    studentid = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    dateofbirth = models.DateField()
    dateofenrolment = models.DateField()
    nationality = models.CharField(max_length=50)
    dateofgraduation = models.DateField(null=True, blank=True)
    photo = ImageField(upload_to='images/', null=True, blank=True)
    classes = models.ManyToManyField(Class, related_name='students')
    academicyear = models.ForeignKey(academicyear, related_name='scores', on_delete=models.CASCADE, null=True)


class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    yearid = models.ForeignKey(Year, on_delete=models.CASCADE)
    classes_taken = models.ForeignKey(Class, on_delete=models.CASCADE)
    score = models.FloatField()
    academicyear = models.CharField(max_length=100, null=True)
    grademark = models.CharField(max_length=100)

    def calculate_gpa(self):
        scores = Score.objects.filter(studentid=self.studentid)
        if scores.exists():
            total_score = 0
            total_units = 0
            for score in scores:
                total_score += score.score * score.classes_taken.units
                total_units += score.classes_taken.units
            return total_score / total_units
        else:
            return 0.0

    def save(self, *args, **kwargs):
        self.gpa = self.calculate_gpa()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Score for {self.studentid} in {self.classes_taken} ({self.academicyear})"



#class grades_pdf(models.Model):
    #pdf = models.FileField(upload_to='pdfs/')
