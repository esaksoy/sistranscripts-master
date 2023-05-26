from . models import *
from import_export.admin import ImportExportModelAdmin
from django.urls import path
from django.shortcuts import redirect
from django.contrib import admin
from django.shortcuts import reverse, render
from django.utils.html import format_html
from django.shortcuts import redirect
from django.urls import path
from .models import Year, Class


class StudentAdmin(ImportExportModelAdmin):
    list_display = ["studentid", "firstname","lastname","dateofbirth" ]
    search_fields = ["studentid"]
    list_per_page = 9
    pass

class ScoreInline(admin.TabularInline):
    model = Score

#edit


class YearAdmin(admin.ModelAdmin):
        list_display = ["year"]
        list_display_links = None  # Remove the link from the year field

        def year_link(self, obj):
            url = reverse("admin:year-classes", args=[obj.pk])  # URL for the classes page
            return f'<a href="{url}">{obj.year}</a>'

        year_link.short_description = "Year"
        list_display = [year_link]

        def get_urls(self):
            urls = super().get_urls()
            custom_urls = [
                path('<int:year_id>/classes/', self.admin_site.admin_view(self.year_classes_view), name='year-classes')
            ]
            return custom_urls + urls

        def year_classes_view(self, request, year_id):
            year = Year.objects.get(pk=year_id)
            classes = year.class_set.all()
            return render(request, 'admin/year_classes.html', {'year': year, 'classes': classes})


class ClassAdmin(admin.ModelAdmin):
    list_display = ["classname"]
    #inlines = [ScoreInline]


class ScoreAdmin(admin.ModelAdmin):
    list_display = ["student", "yearid", "classes_taken", "score", "calculate_gpa"]
    search_fields = ["student"]
    list_per_page = 9

class academicyearAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student, StudentAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Year, YearAdmin)
admin.site.register(academicyear, academicyearAdmin)





