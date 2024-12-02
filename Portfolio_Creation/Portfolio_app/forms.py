from django import forms
from .models import UserProfile, Education, Experience, Project, Certification, ContactInfo

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name','about', 'skills']

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['phone_number', 'email', 'address']
class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school_name', 'degree', 'yop', 'others', 'specialization']


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['company_name', 'role', 'start_date', 'end_date', 'description']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'technologies_used', 'published', 'description', 'url']


class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['name', 'issued_by', 'date_issued', 'description', 'url']
