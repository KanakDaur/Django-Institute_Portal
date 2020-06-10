from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from app1.forms import signup
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from app1.models import EdsysClass, Subject,Student
from django.urls import reverse,reverse_lazy
# Create your views here.

# for default page when user hits the url
def first_login_page(request):
    return HttpResponseRedirect('/accounts/login')

# logout page when user click on the logout button
def logout_view(request):
    return render(request,'app1/logout.html')

# for new user registration (sign up)
def signup_view(request):
    sform = signup()
    if request.method == "POST":
        sform = signup(request.POST)
        if sform.is_valid():
            data = sform.save(commit = False)
            data.set_password(data.password)
            data.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request, 'app1/signup.html', {'sform':sform})

@login_required
def dashboard_view(request):
    return render(request, 'app1/index.html')

# This will create a form by which we can add new classes
@method_decorator(login_required, name='dispatch')
class AddClass(CreateView):
    model = EdsysClass
    fields = '__all__'

# To see the list of all available (added) classes
@method_decorator(login_required, name='dispatch')
class AllClass(ListView):
    model = EdsysClass
    template_name = 'app1/allclass.html'
    context_object_name = 'classes'

# To update the already added classes
@method_decorator(login_required, name='dispatch')
class UpdateClass(UpdateView):
    model = EdsysClass
    fields = '__all__'

# deleting a Class
@method_decorator(login_required, name='dispatch')
class DeleteClass(DeleteView):
    model = EdsysClass
    success_url = reverse_lazy('view class')

# to show Edit or delete option for Classes
@method_decorator(login_required, name='dispatch')
class EditDeleteClass(ListView):
    model = EdsysClass
    template_name = 'app1/edit-delete_view.html'
    context_object_name = 'classes'

# to insert subjects in the classes
@method_decorator(login_required, name='dispatch')
class InsertSubject(CreateView):
    model = Subject
    fields = '__all__'

# to see the list of subjects available in classes
@login_required
def SubjectList(request):
    subjects = EdsysClass.objects.all()
    return render(request,'app1/subjectlist.html',{'subjects':subjects})

# to update the subjects of any specific class
class editsubject(UpdateView):
    model = Subject
    fields = '__all__'

# to delete the subject of any specific class
class deletesubject(DeleteView):
    model = Subject
    success_url = reverse_lazy('subject list')

# to add new students in class
class addstudent(CreateView):
    model = Student
    fields = "__all__"

# to see the list of all students of institute
def studentslist(request):
    students = Student.objects.all()
    return render(request,'app1/allstudents.html',{'students':students})

# list of students name to delete and edit their record
@method_decorator(login_required, name='dispatch')
class EditDeleteStudent(ListView):
    model = Student

class editstudent(UpdateView):
    model = Student
    fields = "__all__"

class deletestudent(DeleteView):
    model = Student
    success_url = reverse_lazy('editdeletestud')

class admissionletterlist(ListView):
    model = Student
    template_name = "app1/admissionletter.html"
    context_object_name = "studadmission"

class admissionletterdetail(DetailView):
    model = Student
