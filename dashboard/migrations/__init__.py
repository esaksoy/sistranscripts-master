from django.db import migrations

def set_default_yearid(apps, schema_editor):
    Year = apps.get_model('dashboard', 'Year')
    Year.objects.filter(yearid=None).update(yearid=0)

class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20230515_0946'),
    ]

    operations = [
        migrations.RunPython(set_default_yearid),
    ]