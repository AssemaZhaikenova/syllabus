# Generated by Django 4.2.7 on 2023-11-10 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Согласование',
                'verbose_name_plural': 'Согласовывание',
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Телефонный номер')),
                ('position', models.CharField(blank=True, max_length=100, null=True, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Директор',
                'verbose_name_plural': 'Директоры',
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=255, verbose_name='Дисциплина')),
            ],
            options={
                'verbose_name': 'Дисциплина',
                'verbose_name_plural': 'Дисциплины',
            },
        ),
        migrations.CreateModel(
            name='EducationLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Уровень обучения')),
            ],
            options={
                'verbose_name': 'Уровень обучения',
                'verbose_name_plural': 'Уровень обучения',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Язык обучения')),
            ],
            options={
                'verbose_name': 'Язык обучения',
                'verbose_name_plural': 'Язык обучения',
            },
        ),
        migrations.CreateModel(
            name='LanguageProficiency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=50, verbose_name='Уровень владения языком')),
            ],
            options={
                'verbose_name': 'Уровень владения языком',
                'verbose_name_plural': 'Уровень владения языком',
            },
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название силлабуса')),
                ('ects', models.IntegerField(verbose_name='Кредиты ECTS')),
                ('total_hours', models.IntegerField(verbose_name='Всего часов')),
                ('classroom_hours', models.IntegerField(verbose_name='Аудиторные часы')),
                ('iw_hours', models.IntegerField(verbose_name='Самостоятельная работа (СРОП, СРО)')),
                ('semester', models.IntegerField(verbose_name='Семестр')),
                ('prerequisites', models.CharField(max_length=255, verbose_name='Пререквизиты')),
                ('educational_program', models.CharField(max_length=255, verbose_name='Образовательная программа')),
                ('time_class', models.CharField(max_length=255, verbose_name='Время и место проведения занятий')),
                ('course_goal', models.TextField(default='Здесь может быть цель курса', verbose_name='Цель курса')),
                ('from_asu_repository', models.BooleanField(default=False, verbose_name='На основе ASU репозитории')),
                ('approvals_syllabus', models.ManyToManyField(blank=True, related_name='syllabus_approvals', through='syllabus.Approval', to='syllabus.director', verbose_name='Согласование')),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syllabus.discipline', verbose_name='Дисциплина')),
                ('education_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syllabus.educationlevel', verbose_name='Уровень обучения')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syllabus.language', verbose_name='Язык обучения')),
                ('language_proficiency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syllabus.languageproficiency', verbose_name='Уровень владения языком')),
            ],
            options={
                'verbose_name': 'Силлабус',
                'verbose_name_plural': 'Силлабус',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('position', models.CharField(default='Преподаватель', max_length=100, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
            },
        ),
        migrations.CreateModel(
            name='TeachingFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format_name', models.CharField(max_length=50, verbose_name='Формат обучения')),
            ],
            options={
                'verbose_name': 'Формат обучения',
                'verbose_name_plural': 'Формат обучения',
            },
        ),
        migrations.CreateModel(
            name='ThematicPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField(default=0, verbose_name='Неделя')),
                ('topic', models.CharField(max_length=255, verbose_name='Тема / модуль')),
                ('ro', models.CharField(max_length=255, null=True, verbose_name='РО курса, РО ОП')),
                ('qm', models.CharField(max_length=255, null=True, verbose_name='Вопросы по теме/ модулю')),
                ('tasks', models.CharField(max_length=255, null=True, verbose_name='Задания')),
                ('lit', models.CharField(max_length=255, null=True, verbose_name='Литература')),
                ('so', models.CharField(max_length=255, null=True, verbose_name='Структура оценок')),
                ('syllabus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='syllabus.syllabus', verbose_name='Силлабус')),
            ],
            options={
                'verbose_name': 'Тематический план',
                'verbose_name_plural': 'Тематические планы',
            },
        ),
        migrations.AddField(
            model_name='syllabus',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syllabus.teacher', verbose_name='Преподаватель'),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='teaching_format',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syllabus.teachingformat', verbose_name='Формат обучения'),
        ),
        migrations.CreateModel(
            name='PhilosophyAndPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('philosophy', models.TextField(verbose_name='Философия курса')),
                ('policy', models.TextField(verbose_name='Политика курса')),
                ('syllabus', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='syllabus.syllabus', verbose_name='Силлабус')),
            ],
            options={
                'verbose_name': 'Философия и политика курса',
                'verbose_name_plural': 'Философия и политика курса',
            },
        ),
        migrations.CreateModel(
            name='Literature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('author', models.CharField(max_length=255, verbose_name='Автор')),
                ('syllabus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syllabus.syllabus', verbose_name='Силлабус')),
            ],
            options={
                'verbose_name': 'Литература',
                'verbose_name_plural': 'Список литературы',
            },
        ),
        migrations.CreateModel(
            name='LearningOutcome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_description', models.TextField(verbose_name='Описание курса')),
                ('learning_outcome_course', models.TextField(verbose_name='Результаты обучения курса (РО курса)')),
                ('learning_outcome_program', models.TextField(verbose_name='Результаты обучения образоватильной программы (РО ОП)')),
                ('syllabus', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='syllabus.syllabus')),
            ],
            options={
                'verbose_name': 'Результат обучения',
                'verbose_name_plural': 'Результат обучения',
            },
        ),
        migrations.CreateModel(
            name='EvaluationSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criteria', models.CharField(max_length=255, verbose_name='Критерии оценивания')),
                ('weight', models.IntegerField(verbose_name='Вес критерия')),
                ('syllabus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syllabus.syllabus', verbose_name='Силлабус')),
            ],
            options={
                'verbose_name': 'Система оценивания курса',
                'verbose_name_plural': 'Системы оценивания курса',
            },
        ),
        migrations.AddField(
            model_name='approval',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syllabus.director', verbose_name='Директор'),
        ),
        migrations.AddField(
            model_name='approval',
            name='syllabus_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='approvals', to='syllabus.syllabus', verbose_name='Силлабус'),
        ),
    ]