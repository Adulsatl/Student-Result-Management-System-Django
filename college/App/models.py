from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#################College##########################

class college_regi(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    HEAD_NAME=models.CharField(max_length=50,null=True)
    ADDRESS=models.CharField(max_length=50 ,null=True)
    C_BASE=models.TextField(max_length=50 ,null=True)
    PHONE=models.IntegerField(null=True)
    is_approved=models.CharField(max_length=50,default='waiting')
    def __str__(self):
        return self.user.username+'  '+ self.is_approved 

#################College##########################

#################Teacher##########################
    
class teacher_regi(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   tr_user=models.ForeignKey(college_regi,on_delete=models.CASCADE) 
   TEACHER_NAME=models.TextField(max_length=50 ,null=True)
   TEACHER_PHONE=models.IntegerField(null=True) 
   TEACHER_ADDRESS=models.CharField(max_length=50 ,null=True)
   TEACHER_AGE=models.CharField(max_length=50 ,null=True)
   TEACHER_GENDER=models.CharField(max_length=50 ,null=True)
   TEACHER_QULIFICATION=models.ImageField(upload_to='teacher_qulification')
   TEACHER_DEPARTMENT=models.CharField(max_length=50 ,null=True)
   TEACHER_SUBJECT=models.CharField(max_length=50 ,null=True)
   is_approved=models.CharField(max_length=50,default='waiting')

#################Teacher##########################

#################Student########################## 
     
class student_regi(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   st_user=models.ForeignKey(college_regi,on_delete=models.CASCADE) 
   STUDENTS_NAME=models.TextField(max_length=50 ,null=True)
   STUDENTS_ROLL=models.TextField(max_length=50 ,null=True)
   STUDENTS_SEM=models.TextField(max_length=50 ,null=True)
   STUDENTS_PHONE=models.IntegerField(null=True) 
   STUDENTS_ADDRESS=models.CharField(max_length=50 ,null=True)
   STUDENTS_AGE=models.CharField(max_length=50 ,null=True)
   STUDENTS_GENDER=models.CharField(max_length=50 ,null=True)
   STUDENTS_QULIFICATION=models.ImageField(upload_to='student_qulification')
   STUDENTS_DEPARTMENT=models.CharField(max_length=50 ,null=True)
   PIC=models.ImageField(upload_to='student_register')
   is_approved=models.CharField(max_length=50,default='waiting')
   def __str__(self):
        return self.user.username

#################Student##########################
   
#################Parent###########################
class parent_reg(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   std_user=models.ForeignKey(student_regi,on_delete=models.CASCADE)
   PARENT_NAME=models.CharField(max_length=50 ,null=True)
   PARENT_PHONE=models.CharField(max_length=50 ,null=True)
   PARENT_RELATION=models.CharField(max_length=50 ,null=True)
   is_approved=models.CharField(max_length=50,default='waiting')
   
#################Parent###########################  

#################MARK#####################
class SUB(models.Model):
   year=models.CharField(max_length=10,default='waiting')
   sem =models.CharField(max_length=10,default='waiting')
   SUB1=models.CharField(max_length=10,default='waiting')
   SUB2=models.CharField(max_length=10,default='waiting')
   SUB3=models.CharField(max_length=10,default='waiting')
   SUB4=models.CharField(max_length=10,default='waiting')
   SUB5=models.CharField(max_length=10,default='waiting')
   def __str__(self):
        return self.sem
   
    
class AD_MAR(models.Model):
   user=models.ForeignKey(student_regi,on_delete=models.CASCADE)
   sub=models.ForeignKey(SUB,on_delete=models.CASCADE)
   AD_MAR1=models.CharField(max_length=10,default='waiting')
   AD_MAR2=models.CharField(max_length=10,default='waiting')
   AD_MAR3=models.CharField(max_length=10,default='waiting')
   AD_MAR4=models.CharField(max_length=10,default='waiting')
   AD_MAR5=models.CharField(max_length=10,default='waiting')
   def __str__(self):
        return self.user.user.username
   
  

class TR_MAR(models.Model):
   st=models.ForeignKey(student_regi,on_delete=models.CASCADE)
   sub=models.ForeignKey(SUB,on_delete=models.CASCADE)
   ad_mar=models.ForeignKey(AD_MAR,on_delete=models.CASCADE)
   TR_MAR1=models.CharField(max_length=10,default='waiting')
   TR_MAR2=models.CharField(max_length=10,default='waiting')
   TR_MAR3=models.CharField(max_length=10,default='waiting')
   TR_MAR4=models.CharField(max_length=10,default='waiting')
   TR_MAR5=models.CharField(max_length=10,default='waiting')   
  
#################MARK#####################
    