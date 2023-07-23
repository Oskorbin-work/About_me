from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='projects_sending_emails'),
    path("new_email_recipient/", login_required(views.new_email_recipient), name="new_email_recipient"),
    path("new_email_template/", login_required(views.new_email_template), name="new_email_template"),

]