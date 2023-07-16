from django.urls import path
from . import views

urlpatterns = [
    path('',  views.redirect_to_url_main_page, name=''),
    path('main_page/', views.main_page, name='main_page'),
    path('about_me/education/',  views.about_me_education, name='about_me_education'),
    path('about_me/skills/', views.about_me_skills, name='about_me_skills'),
    path('contacts/', views.contacts, name='contacts'),
    path('about_me/education/grades/<int:pk>/', views.EducationDetail.as_view(), name='education'),
]