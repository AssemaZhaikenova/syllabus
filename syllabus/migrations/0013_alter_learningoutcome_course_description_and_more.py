# Generated by Django 4.2.7 on 2023-11-11 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0012_courseoutcome_programoutcome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learningoutcome',
            name='course_description',
            field=models.TextField(null=True, verbose_name='Описание курса'),
        ),
        migrations.RemoveField(
            model_name='learningoutcome',
            name='learning_outcome_course',
        ),
        migrations.RemoveField(
            model_name='learningoutcome',
            name='learning_outcome_program',
        ),
        migrations.DeleteModel(
            name='CourseOutcome',
        ),
        migrations.DeleteModel(
            name='ProgramOutcome',
        ),
        migrations.AddField(
            model_name='learningoutcome',
            name='learning_outcome_course',
            field=models.TextField(null=True, verbose_name='Результаты обучения курса (РО курса)'),
        ),
        migrations.AddField(
            model_name='learningoutcome',
            name='learning_outcome_program',
            field=models.TextField(null=True, verbose_name='Результаты обучения образоватильной программы (РО ОП)'),
        ),
    ]
