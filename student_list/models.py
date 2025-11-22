from django.db import models

class Personal_Background(models.Model):
    name = models.CharField(max_length=40)
    age = models.CharField(max_length=3)
    choice = {
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Rather not say', 'Rather not say'),
    }
    
    gender = models.CharField(choices=choice,default='Male')
    address = models.CharField(max_length=155)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Education_Background(models.Model):
    person = models.ForeignKey(Personal_Background, related_name='education', on_delete=models.CASCADE,null=True)
    education_level = models.CharField(max_length=40,null=True)
    school_name = models.CharField(max_length=40,null=True)
    school_address = models.CharField(max_length=155,null=True)
    choice = {
        ('BSIT', 'BSIT'),
        ('BSPA', 'BSPA'),
        ('BSSW', 'BSSW'),
        ('BTVTE', 'BTVTE'),
        ('BSAIS', 'BSAIS'),
    }
    course = models.CharField(choices=choice,default='BSIT',null=True)
    year = models.CharField(max_length=155,null=True)

    def __str__(self):
        return self.education_level
    
class Family_Background(models.Model):
    person = models.ForeignKey(Personal_Background, related_name='family', on_delete=models.CASCADE,null=True)
    father_name = models.CharField(max_length=40,null=True)
    mother_name = models.CharField(max_length=40,null=True)
    number_of_siblings = models.CharField(max_length=3,null=True)
    guardian_name = models.CharField(max_length=40,null=True)
    guardian_contact = models.CharField(max_length=155,null=True)

    def __str__(self):
        return self.guardian_name
    
class Course(models.Model):
    person = models.ForeignKey(Personal_Background, related_name='course', on_delete=models.CASCADE,null=True)
    course_id = models.CharField(max_length=40,null=True)
    course_code = models.CharField(max_length=40,null=True)
    course_name = models.CharField(max_length=3,null=True)
    department = models.CharField(max_length=40,null=True)
    units = models.CharField(max_length=155,null=True)

    def __str__(self):
        return self.course_name

class Tuition(models.Model):
    person = models.ForeignKey(Personal_Background, related_name='tuition', on_delete=models.CASCADE,null=True)
    payment_id = models.CharField(max_length=40,null=True)
    course_id = models.CharField(max_length=40,null=True)
    semester = models.CharField(max_length=3,null=True)
    amount = models.CharField(max_length=40,null=True)
    Due_date = models.DateField()

    def __str__(self):
        return self.semester

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    photo = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.user.username
