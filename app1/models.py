from django.db import models
from django.urls import reverse
# Create your models here.

class EdsysClass(models.Model):
    name = models.CharField(max_length = 50)
    fee = models.IntegerField()
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse ('view class')

class Subject(models.Model):
    marks = models.IntegerField()
    sub_category = models.CharField(max_length=30)
    class_name = models.ForeignKey(EdsysClass, on_delete=models.CASCADE, default="")
    def __str__(self):
        return self.sub_category
    def get_absolute_url(self):
        return reverse ('subject list')

class Student(models.Model):
    GENDER_CHOICES = (('male','Male'),('female','Female'),('other','Other'))
    RELIGION_CHOICES = (('buddhism','Buddhism'),('christianity','Christianity'),('hinduism','Hinduism'),('islam','Islam'),('jainism','Jainism'),('sikhism','Sikhism'),('other','Other'))
    stu_name = models.CharField(max_length = 30)
    registration_num = models.IntegerField()
    Admission_date = models.DateField()
    photo = models.FileField(upload_to = "student_images",default = "student_icon.png")
    mobile_num = models.IntegerField(null=False, blank=False, unique=True)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length = 20,choices = GENDER_CHOICES,default = "male")
    caste = models.CharField(max_length = 30)
    previous_school = models.CharField(max_length = 50)
    orphan_student = models.BooleanField(blank = True)
    religion = models.CharField(max_length = 20,choices = RELIGION_CHOICES,default = "hinduism")
    address = models.TextField()
    father_name = models.CharField(max_length = 20)
    father_education = models.CharField(max_length = 20,null=True, blank=True)
    father_occupation = models.CharField(max_length = 20,null=True, blank=True)
    father_income = models.FloatField(null=True, blank=True)
    father_mobile = models.IntegerField()
    mother_name = models.CharField(max_length = 20)
    mother_education = models.CharField(max_length = 20,null=True, blank=True)
    mother_occupation = models.CharField(max_length = 20,null=True, blank=True)
    mother_income = models.FloatField(null=True, blank=True)
    mother_mobile = models.IntegerField(null=True, blank=True)
    name_of_class = models.ForeignKey(EdsysClass,on_delete = models.CASCADE)
    def __str__(self):
        return self.stu_name
    def get_absolute_url(self):
        return reverse('students list')
