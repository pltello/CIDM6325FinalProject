# Generated by Django 4.2.5 on 2023-10-08 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('degree_checklist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='core_requirements',
            name='CourseName',
            field=models.CharField(help_text='Course Name', max_length=75),
        ),
    ]