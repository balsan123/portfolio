from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Education, Experience, Project, Certification, LoginTable, ContactInfo
from .forms import UserProfileForm, EducationForm, ExperienceForm, ProjectForm, CertificationForm, ContactInfoForm

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def userRegistration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()

                UserProfile.objects.create(user=user)
                LoginTable.objects.create(username=username, password=password, type='user')

                messages.info(request, 'Registration successful')
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
    return render(request, 'register.html')



# User login view
def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['username'] = username
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

# User logout view
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')

# Home view
@login_required
def home(request):
    education = Education.objects.filter(user=request.user).first()
    experience = Experience.objects.filter(user=request.user).first()
    project = Project.objects.filter(user=request.user).first()

    return render(request, 'home.html', {'experience': experience, 'education': education, 'project':project})


@login_required
def user_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    education = Education.objects.filter(user=request.user)
    experience = Experience.objects.filter(user=request.user)
    projects = Project.objects.filter(user=request.user)
    certifications = Certification.objects.filter(user=request.user)

    return render(request, 'user_view.html', {
        'user_profile': user_profile,
        'education': education,
        'experience': experience,
        'projects': projects,
        'certifications': certifications
    })


@login_required
def edit_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('about_me')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'edit_profile.html', {'form': form})


# Add and edit education
@login_required
def add_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.user = request.user
            education.save()
            return redirect('edit_education',pk=education.pk)
    else:
        form = EducationForm()

    return render(request, 'add_education.html', {'form': form})



def edit_education(request, pk):
    education = get_object_or_404(Education, pk=pk)

    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect('education_details',pk=education.pk)
    else:
        form = EducationForm(instance=education)

    return render(request, 'edit_education.html', {'form': form, 'education': education})



@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('edit_project', pk=project.pk)
    else:
        form = ProjectForm()

    return render(request, 'add_project.html', {'form': form})


@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_details',pk=project.pk)
    else:
        form = ProjectForm(instance=project)

    return render(request, 'edit_project.html', {'form': form, 'project': project})




@login_required
def add_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = request.user
            experience.save()
            return redirect('edit_experience', pk=experience.pk)
    else:
        form = ExperienceForm()

    return render(request, 'add_experience.html', {'form': form})


@login_required
def edit_experience(request, pk):
    experience = get_object_or_404(Experience, pk=pk)

    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            return redirect('experience_details',pk=experience.pk)
    else:
        form = ExperienceForm(instance=experience)

    return render(request, 'edit_experience.html', {'form': form, 'experience': experience})


@login_required
def add_certification(request):
    certifications = Certification.objects.filter(user=request.user)

    if request.method == 'POST':
        form = CertificationForm(request.POST)
        if form.is_valid():
            certification = form.save(commit=False)
            certification.user = request.user
            certification.save()
            return redirect('add_certification')
    else:
        form = CertificationForm()

    return render(request, 'add_certification.html', {
        'form': form,
        'certifications': certifications
    })


@login_required
def edit_certification(request, pk):
    certification = get_object_or_404(Certification, pk=pk, user=request.user)

    if request.method == 'POST':
        form = CertificationForm(request.POST, instance=certification)
        if form.is_valid():
            form.save()
            return redirect('certification_details', pk=certification.pk)
    else:
        form = CertificationForm(instance=certification)

    return render(request, 'edit_certification.html', {'form': form})

def about_me(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'about_me.html', {'user_profile': user_profile})


def edit_contact_info(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    contact_info, created = ContactInfo.objects.get_or_create(
        user_profile=user_profile)
    if request.method == 'POST':
        form = ContactInfoForm(request.POST, instance=contact_info)
        if form.is_valid():
            form.save()
            return redirect('contact_me')
    else:
        form = ContactInfoForm(instance=contact_info)

    return render(request, 'edit_contact_info.html', {'form': form})

def contact_me(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    contact_info = get_object_or_404(ContactInfo, user_profile=user_profile)

    return render(request, 'contact_me.html', {'contact_info': contact_info})

def education_details(request, pk):
    education = get_object_or_404(Education, pk=pk)
    return render(request, 'education_details.html', {'education': education})

def experience_details(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    print(experience)
    return render(request, 'experience_details.html', {'experience': experience})

def project_details(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project.html', {'project': project})

def certification_details(request, pk=None):
    certification = Certification.objects.filter(user=request.user)
    return render(request, 'certification.html', {'certification': certification})