# Generated by Django 2.1.4 on 2019-01-03 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_html', '0002_patient_profile_conclusion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient_profile_conclusion',
            old_name='hrmoglobin_cnt',
            new_name='hemoglobin_cnt',
        ),
        migrations.AlterModelTable(
            name='patient_profile_conclusion',
            table=None,
        ),
        migrations.AlterModelTable(
            name='profile',
            table=None,
        ),
    ]
