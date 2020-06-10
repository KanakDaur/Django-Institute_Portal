"""edsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app1 import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard_view, name = "dashboard"),
    path('', views.first_login_page),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup_view),
    path('addclass/', views.AddClass.as_view(), name='add class'),
    path('viewallclass/', views.AllClass.as_view(), name='view class'),
    path('deleteclass/<int:pk>', views.DeleteClass.as_view(), name='delete class'),
    path('editdelete/', views.EditDeleteClass.as_view()),
    path('updateclass/<int:pk>', views.UpdateClass.as_view(), name='update class'),
    path('insertsubject/', views.InsertSubject.as_view(), name='add sub'),
    path('subjectlist/', views.SubjectList, name = "subject list"),
    path('logout/',views.logout_view),
    path('editsubject/<int:pk>',views.editsubject.as_view()),
    path('deletesubject/<int:pk>',views.deletesubject.as_view()),
    path('addstudents/',views.addstudent.as_view()),
    path('listofstudents/',views.studentslist,name = 'students list'),
    path('editdeletestudents/',views.EditDeleteStudent.as_view(),name = "editdeletestud"),
    path('editstudent/<int:pk>',views.editstudent.as_view()),
    path('deletestudent/<int:pk>',views.deletestudent.as_view()),
    path('admissionletter/',views.admissionletterlist.as_view()),
    path('detail/<int:pk>',views.admissionletterdetail.as_view()),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
