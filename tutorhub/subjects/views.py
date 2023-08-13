from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Subject
from .forms import SubjectForm
from django.contrib.auth.decorators import login_required



def subjects(request):
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'subjects/subjects.html', {'subjects':subjects})


def subject(request, pk):
    subjectObj = Subject.objects.get(id=pk)
    tags = subjectObj.tags.all()
    return render(request, 'subjects/single-subject.html', {'subject': subjectObj, 'tags': tags})

@login_required(login_url='login')
def addSubject(request):
    tutorprofile = request.user.tutorprofile
    form = SubjectForm()

    if request.method == 'POST':
        form = SubjectForm(request.POST, request.FILES)
        if form .is_valid():
            subject = form.save(commit=False)
            subject.owner = tutorprofile
            subject.save()
            return redirect('subjects')
        
    context = {'form': form}
    return render(request, 'subjects/subject-form.html', context)


@login_required(login_url='login')
def editSubject(request, pk):
    tutorprofile = request.user.tutorprofile
    subject = tutorprofile.subject_set.get(id=pk)
    form = SubjectForm(instance=subject)

    if request.method == 'POST':
        form = SubjectForm(request.POST, request.FILES, instance=subject)
        if form .is_valid():
            form.save()
            return redirect('subjects')
        
    context = {'form': form}
    return render(request, 'subjects/subject-form.html', context)

@login_required(login_url='login')
def deleteSubject(request, pk):
    tutorprofile = request.user.tutorprofile
    subject = tutorprofile.subject_set.get(id=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('subjects')
    context = {'object': subject}
    return render(request, 'delete-template.html', context)