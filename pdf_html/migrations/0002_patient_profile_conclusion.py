# Generated by Django 2.1.4 on 2019-01-03 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_html', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient_profile_conclusion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hrmoglobin_cnt', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'conclusion1',
            },
        ),
    ]