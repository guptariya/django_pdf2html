# Generated by Django 2.1.4 on 2019-01-03 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_html', '0004_auto_20190103_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_profile_conclusion',
            name='MCH_cnt',
            field=models.CharField(default='0', max_length=5),
        ),
    ]
