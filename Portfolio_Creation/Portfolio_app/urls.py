from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('education/<int:pk>/', views.education_details, name='education_details'),
    path('experience/<int:pk>/', views.experience_details, name='experience_details'),
    path('project/<int:pk>/', views.project_details, name='project_details'),
    path('certification/', views.certification_details, name='certification_details'),

    path('about/', views.about_me, name='about_me'),
    path('edit_contact/', views.edit_contact_info, name='edit_contact_info'),
    path('contact/', views.contact_me, name='contact_me'),
    path('register/', views.userRegistration, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user_view/', views.user_view, name='user_view'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('add_education/', views.add_education, name='add_education'),
    path('edit_education/<int:pk>/', views.edit_education, name='edit_education'),
    path('add_experience/', views.add_experience, name='add_experience'),
    path('edit_experience/<int:pk>/', views.edit_experience, name='edit_experience'),
    path('add_project/', views.add_project, name='add_project'),
    path('edit_project/<int:pk>/', views.edit_project, name='edit_project'),
    path('add_certification/', views.add_certification, name='add_certification'),
    path('edit_certification/<int:pk>/', views.edit_certification, name='edit_certification'),
]
