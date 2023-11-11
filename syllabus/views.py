import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages

from django.http import HttpResponse
from docxtpl import DocxTemplate
from io import BytesIO


def home_view(request):
    return render(request, 'home.html')


def account(request):
    user = request.user
    return render(request, 'account.html', {'user': user})


@login_required
def create_syllabus_view(request):
    if request.method == 'POST':
        form = SyllabusForm(request.POST)
        if form.is_valid():
            syllabus = form.save(commit=False)
            syllabus.created_by = request.user
            syllabus.save()
            return redirect('correspondence', syllabus_id=syllabus.id)
    else:
        form = SyllabusForm()

    return render(request, 'create_syllabus.html', {'form': form})


def correspondence(request, syllabus_id):
    syllabus = get_object_or_404(Syllabus, id=syllabus_id)
    learning_outcomes = syllabus.learningoutcome_set.all()

    if request.method == 'POST':
        form = LearningOutcomeForm(request.POST)
        if form.is_valid():
            learning_outcome = form.save(commit=False)
            learning_outcome.syllabus = syllabus
            learning_outcome.save()

            return redirect('correspondence', syllabus_id=syllabus.id)
    else:
        form = LearningOutcomeForm()

    return render(request, 'correspondence.html', {'form': form, 'syllabus': syllabus, 'learning_outcomes': learning_outcomes})


def delete_learning_outcome(request, syllabus_id, outcome_id):
    learning_outcome = get_object_or_404(LearningOutcome, pk=outcome_id)

    if request.method == 'POST':
        learning_outcome.delete()
        return redirect('correspondence', syllabus_id=syllabus_id)

    return redirect('correspondence', syllabus_id=syllabus_id)


def thematic_plan(request, syllabus_id):
    syllabus = Syllabus.objects.get(id=syllabus_id)

    if request.method == 'POST':
        form = ThematicPlanForm(request.POST)
        if form.is_valid():
            thematic_plan = form.save(commit=False)
            thematic_plan.syllabus = syllabus
            thematic_plan.save()

            return redirect('thematic_plan', syllabus_id=syllabus_id)
    else:
        form = ThematicPlanForm()

    thematic_plans = syllabus.thematicplan_set.all()

    return render(request, 'thematic_plan.html', {'form': form, 'syllabus': syllabus, 'thematic_plans': thematic_plans})


def delete_thematic_plan(request, syllabus_id, plan_id):
    thematic_plan = get_object_or_404(ThematicPlan, pk=plan_id)

    if request.method == 'POST':
        thematic_plan.delete()
        return redirect('thematic_plan', syllabus_id=syllabus_id)

    return render(request, 'thematic_plan.html', {'thematic_plan': thematic_plan})


def evaluation_system(request, syllabus_id):
    syllabus = Syllabus.objects.get(id=syllabus_id)

    if request.method == 'POST':
        form = EvaluationSystemForm(request.POST)
        if form.is_valid():
            evaluation_system = form.save(commit=False)
            evaluation_system.syllabus = syllabus
            evaluation_system.save()

            return redirect('evaluation_system', syllabus_id=syllabus_id)
    else:
        form = EvaluationSystemForm()

    evaluation_systems = syllabus.evaluationsystem_set.all()

    return render(request, 'evaluation_system.html', {'form': form, 'syllabus': syllabus, 'evaluation_systems': evaluation_systems})


def delete_evaluation_system(request, syllabus_id, system_id):
    evaluation_system = get_object_or_404(EvaluationSystem, pk=system_id)

    if request.method == 'POST':
        evaluation_system.delete()
        return redirect('evaluation_system', syllabus_id=syllabus_id)

    return render(request, 'evaluation_system.html', {'evaluation_system': evaluation_system})


def literature_list(request, syllabus_id):
    syllabus = Syllabus.objects.get(id=syllabus_id)

    if request.method == 'POST':
        form = LiteratureForm(request.POST)
        if form.is_valid():
            literature = form.save(commit=False)
            literature.syllabus = syllabus
            literature.save()

            return redirect('literature_list', syllabus_id=syllabus_id)
    else:
        form = LiteratureForm()

    literature_list = syllabus.literature_set.all()

    return render(request, 'literature_list.html', {'form': form, 'syllabus': syllabus, 'literature_list': literature_list,})


def delete_literature(request, syllabus_id, literature_id):
    literature = get_object_or_404(Literature, pk=literature_id)

    if request.method == 'POST':
        literature.delete()
        return redirect('literature_list', syllabus_id=syllabus_id)

    return render(request, 'literature_list.html', {'literature': literature})


def philosophy_and_policy(request, syllabus_id):
    syllabus = Syllabus.objects.get(id=syllabus_id)

    try:
        philosophy_and_policy = PhilosophyAndPolicy.objects.get(syllabus=syllabus)
    except PhilosophyAndPolicy.DoesNotExist:
        philosophy_and_policy = None

    if request.method == 'POST':
        form = PhilosophyAndPolicyForm(request.POST, instance=philosophy_and_policy)
        if form.is_valid():
            philosophy_and_policy = form.save(commit=False)
            philosophy_and_policy.syllabus = syllabus
            philosophy_and_policy.save()
            messages.success(request, 'Силлабус успешно сохранен!')

            return redirect('home')
    else:
        form = PhilosophyAndPolicyForm(instance=philosophy_and_policy)

    return render(request, 'philosophy_and_policy.html', {'form': form, 'syllabus': syllabus})


@login_required
def syllabus_list(request):
    user_syllabuses = Syllabus.objects.filter(created_by=request.user)
    return render(request, 'syllabus_list.html', {'syllabuses': user_syllabuses})


@login_required
def syllabus_detail_edit(request, syllabus_id):
    syllabus = get_object_or_404(Syllabus, id=syllabus_id, created_by=request.user)

    if request.method == 'POST':
        form = SyllabusForm(request.POST, instance=syllabus)
        if form.is_valid():
            form.save()
            return redirect('correspondence', syllabus_id=syllabus.id)
    else:
        form = SyllabusForm(instance=syllabus)

    return render(request, 'syllabus_detail_edit.html', {'form': form, 'syllabus': syllabus})


@login_required
def delete_syllabus(request, syllabus_id):
    syllabus = get_object_or_404(Syllabus, id=syllabus_id, created_by=request.user)

    if request.method == 'POST':
        syllabus.delete()
        return redirect('syllabus_list')

    return render(request, 'delete_syllabus.html', {'syllabus': syllabus})


def download_syllabus_word_ru(request, syllabus_id):
    syllabus = get_object_or_404(Syllabus, pk=syllabus_id)
    learningoutcome = LearningOutcome.objects.get(syllabus=syllabus)
    thematicplan = ThematicPlan.objects.get(syllabus=syllabus)
    evaluation_system = EvaluationSystem.objects.get(syllabus=syllabus)
    literature = Literature.objects.get(syllabus=syllabus)
    philosophy_and_policy = PhilosophyAndPolicy.objects.get(syllabus=syllabus)

    script_directory = os.path.dirname(os.path.abspath(__file__))

    template_path = os.path.join(script_directory, 'syllabus_template.docx')

    doc = DocxTemplate(template_path)

    context = {
        'discipline': syllabus.discipline,
        'education_level': syllabus.education_level,
        'language': syllabus.language,
        'ects': syllabus.ects,
        'total_hours': syllabus.total_hours,
        'classroom_hours': syllabus.classroom_hours,
        'iw_hours': syllabus.iw_hours,
        'semester': syllabus.semester,
        'language_proficiency': syllabus.language_proficiency,
        'email': syllabus.teacher.email,
        'prerequisites': syllabus.prerequisites,
        'educational_program': syllabus.educational_program,
        'teaching_format': syllabus.teaching_format,
        'time_class': syllabus.time_class,
        'teacher': syllabus.teacher,
        'course_goal': syllabus.course_goal,
        'course_description': learningoutcome.course_description,
        'learning_outcome_course': learningoutcome.learning_outcome_course,
        'learning_outcome_program': learningoutcome.learning_outcome_program,
        'week': thematicplan.week,
        'topic': thematicplan.topic,
        'tasks': thematicplan.tasks,
        'ro': thematicplan.ro,
        'qm': thematicplan.qm,
        'lit': thematicplan.lit,
        'so': thematicplan.so,
        'tm': evaluation_system.tm,
        'mp': evaluation_system.mp,
        'mv': evaluation_system.mv,
        'tb': evaluation_system.tb,
        'vk': evaluation_system.tm,
        'title': literature.title,
        'author': literature.author,
        'philosophy': philosophy_and_policy.philosophy,
        'policy': philosophy_and_policy.policy,

    }

    doc.render(context)

    document_buffer = BytesIO()
    doc.save(document_buffer)

    response = HttpResponse(document_buffer.getvalue(),
                            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=syllabus.docx'

    return response
