from django.shortcuts import render, redirect, reverse
from .models import *
from django.contrib.auth import logout
from django.contrib.auth.models import User, auth

# Create your views here.


def index(request):
    return render(request, "index.html")

################# College##########################


def clg_home(request):
    users = User.objects.get(username=request.user)
    clg = college_regi.objects.get(user__username=users)

    return render(request, "college_home.html", {'key': clg})


def clg_log(request):
    if request.method == "POST":
        clg_name = request.POST['clg_name']
        passs = request.POST['pass']
        if college_regi.objects.filter(user__username=clg_name).exists():
            coll = college_regi.objects.get(user__username=clg_name)
            print(coll.is_approved)
            if coll.is_approved == 'yes':
                u = auth.authenticate(username=clg_name, password=passs)
                if u is not None:
                    auth.login(request, u)
                    return redirect(clg_home)
                else:
                    context = {
                        'key': 'invailed user'
                    }
                    return render(request, 'college_log.html', context)
            elif coll.is_approved == 'no':
                context = {
                    'key': 'user is rejected'
                }
                return render(request, 'college_log.html', context)
            else:
                context = {
                    'key': 'Waiting for Approval '
                }
                return render(request, 'college_log.html', context)

        else:
            context = {
                'key': 'invailed user'
            }
        return render(request, 'college_log.html', context)

    return render(request, 'college_log.html')


def clg_reg(request):
    if request.method == "POST":
        college_name = request.POST['clg_name']
        college_head = request.POST['clg_hm']
        college_email = request.POST['clg_email']
        college_phone = request.POST['clg_ph']
        address = request.POST['address']
        course_base = request.POST['base']
        password = request.POST['password']
        conpass = request.POST['conpass']
        if password == conpass:
            if college_regi.objects.filter(user__username=college_name).exists() or User.objects.filter(username=college_name).exists():
                context = {
                    'key': 'username exists'
                }
                return render(request, 'college_reg.html', context)
            else:
                User.objects.create_user(
                    username=college_name, email=college_email, password=password).save()
                user = User.objects.get(username=college_name)
                college_regi(user=user, HEAD_NAME=college_head, ADDRESS=address,
                             PHONE=college_phone, C_BASE=course_base).save()
                context = {
                    'key': 'successfully register '
                }
                return render(request, 'college_reg.html', context)
        else:
            context = {
                'key': 'password does not match'
            }
            return render(request, 'college_reg.html', context)

    return render(request, "college_reg.html")


def clg_tr_lists(request):
    main = User.objects.get(username=request.user)
    tr_lists = teacher_regi.objects.filter(
        tr_user__user__username=main, is_approved="waiting")
    return render(request, "college_tr_lists.html", {'key': tr_lists})


def clg_tr_onelist(request, pk):
    tr_list = teacher_regi.objects.get(id=pk)
    return render(request, "college_tr_onelist.html", {'key': tr_list})


def clg_tr_accept(request, pk):
    tr_list = teacher_regi.objects.get(id=pk)
    tr_list.is_approved = "yes"
    tr_list.save()
    return redirect(clg_tr_lists)


def clg_tr_reject(request, pk):
    tr_list = teacher_regi.objects.get(id=pk)
    tr_list.is_approved = "no"
    tr_list.save()
    return redirect(clg_tr_lists)


def clg_profile(request):
    users = User.objects.get(username=request.user)
    clg = college_regi.objects.get(user__username=users)

    return render(request, 'college_profile.html', {'key': clg})


def clg_update_profile(request):
    users = User.objects.get(username=request.user)
    clg = college_regi.objects.get(user__username=users)

    if request.method == 'POST':
        tabb = User.objects.get(username=request.user)
        tabb.email = request.POST['clg_emails']
        clg.HEAD_NAME = request.POST['clg_hms']
        clg.PHONE = request.POST['clg_phs']
        tabb.save()
        clg.save()
        return redirect(clg_profile)
    return render(request, 'college_update_profile.html', {'key': clg})


def clg_tr_all_listsss(request):
    users = User.objects.get(username=request.user)
    clg = college_regi.objects.get(user__username=users)
    tr = teacher_regi.objects.filter(tr_user__user__username=clg.user.username)
    return render(request, 'college_tr_all_list.html', {'key': tr})

################# College##########################

################# Teacher##########################


def tr_home(request):
    main = User.objects.get(username=request.user)
    tr = teacher_regi.objects.get(user__username=main)

    return render(request, "teacher_home.html", {'key': tr})


def tr_log(request):

    if request.method == "POST":
        tr_name = request.POST['user_name']
        passs = request.POST['pass']
        if teacher_regi.objects.filter(user__username=tr_name).exists():
            tr = teacher_regi.objects.get(user__username=tr_name)
            print(tr.is_approved)
            if tr.is_approved == 'yes':
                u = auth.authenticate(username=tr_name, password=passs)
                if u is not None:
                    auth.login(request, u)
                    return redirect(tr_home)
                else:
                    context = {
                        'key': 'invailed user'
                    }
                    return render(request, 'teacher_log.html', context)
            elif tr.is_approved == 'no':
                context = {
                    'key': 'user is rejected'
                }
                return render(request, 'teacher_log.html', context)
            else:
                context = {
                    'key': 'Waiting for Approval '
                }
                return render(request, 'teacher_log.html', context)

        else:
            context = {
                'key': 'invailed user'
            }
            return render(request, 'teacher_log.html', context)

    return render(request, 'teacher_log.html')


def tr_reg(request):
    if request.method == "POST":
        teacher_name = request.POST['tr_name']
        teacher_username = request.POST['tr_user']
        teacher_email = request.POST['tr_email']
        teacher_phone = request.POST['tr_ph']
        teacher_address = request.POST['tr_address']
        teacher_age = request.POST['tr_age']
        teacher_sex = request.POST['gender']
        teacher_qulification = request.FILES['tr_qulifi']
        teacher_subject = request.POST['sub']
        teacher_department = request.POST['tr_dep']
        teacher_college = request.POST['clg_name']
        password = request.POST['password']
        conpassword = request.POST['conpass']
        if password == conpassword:
            if teacher_regi.objects.filter(user__username=teacher_username).exists() or User.objects.filter(username=teacher_username).exists():
                context = {
                    'key': 'username exists'
                }
                return render(request, 'teacher_reg.html', context)
            else:
                User.objects.create_user(
                    username=teacher_username, email=teacher_email, password=password).save()
                user = User.objects.get(username=teacher_username)
                collge_us = college_regi.objects.get(
                    user__username=teacher_college)
                teacher_regi(user=user, tr_user=collge_us, TEACHER_NAME=teacher_name, TEACHER_ADDRESS=teacher_address, TEACHER_PHONE=teacher_phone, TEACHER_AGE=teacher_age,
                             TEACHER_GENDER=teacher_sex, TEACHER_QULIFICATION=teacher_qulification, TEACHER_DEPARTMENT=teacher_department, TEACHER_SUBJECT=teacher_subject).save()
                context = {
                    'key': 'successfully register '
                }
                return render(request, 'teacher_reg.html', context)
        else:
            context = {
                'key': 'password does not match'
            }
            return render(request, 'teacher_reg.html', context)

    return render(request, 'teacher_reg.html')


def tr_st_lists(request):
    main = User.objects.get(username=request.user)
    tr = teacher_regi.objects.get(user__username=main)
    print(main.username)
    print(tr.TEACHER_DEPARTMENT)
    print(tr.tr_user.user.username)
    st_lists = student_regi.objects.filter(
        st_user__user__username=tr.tr_user.user.username, STUDENTS_DEPARTMENT=tr.TEACHER_DEPARTMENT, is_approved="waiting")
    return render(request, "teacher_st_lists.html", {'key': st_lists})


def tr_st_onelist(request, pk):
    st_list = student_regi.objects.get(id=pk)
    return render(request, 'teacher_st_onelist.html', {'key': st_list})


def tr_st_accept(request, pk):
    st_list = student_regi.objects.get(id=pk)
    st_list.is_approved = "yes"
    st_list.save()
    return redirect(tr_st_lists)


def tr_st_reject(request, pk):
    st_list = student_regi.objects.get(id=pk)
    st_list.is_approved = "no"
    st_list.save()
    return redirect(tr_st_lists)

def tr_pt_lists(request):
    main = User.objects.get(username=request.user)
    tr = teacher_regi.objects.get(user__username=main)
    print(main.username)
    print(tr.TEACHER_DEPARTMENT)
    print(tr.tr_user.user.username)
    pt_lists = parent_reg.objects.filter(
        std_user__st_user__user__username=tr.tr_user.user.username, std_user__STUDENTS_DEPARTMENT=tr.TEACHER_DEPARTMENT, is_approved="waiting")
    
    return render(request,'teacher_pt_lists.html',{'key': pt_lists})

def tr_pt_onelist(request, pk):
    pt_list = parent_reg.objects.get(id=pk)
    return render(request, 'teacher_pt_onelist.html', {'key': pt_list})

def tr_pt_accept(request, pk):
    pt_list = parent_reg.objects.get(id=pk)
    pt_list.is_approved = "yes"
    pt_list.save()
    return redirect(tr_pt_lists)


def tr_pt_reject(request, pk):
    pt_list = parent_reg.objects.get(id=pk)
    pt_list.is_approved = "no"
    pt_list.save()
    return redirect(tr_pt_lists)


def tr_profile(request):
    users = User.objects.get(username=request.user)
    tr = teacher_regi.objects.get(user__username=users)

    return render(request, 'teacher_profile.html', {'key': tr})


def tr_update_profile(request):
    users = User.objects.get(username=request.user)
    tr = teacher_regi.objects.get(user__username=users)
    if request.method == 'POST':
        tabb = User.objects.get(username=request.user)
        tabb.email = request.POST['tr_emailS']
        tr.TEACHER_PHONE = request.POST['tr_phS']
        tr.TEACHER_AGE = request.POST['tr_ageS']
        tr.TEACHER_QULIFICATION = request.FILES['tr_qulifieS']
        tr.TEACHER_ADDRESS = request.POST['tr_addressS']
        tr.TEACHER_DEPARTMENT = request.POST['tr_deps']
        tr.TEACHER_SUBJECT = request.POST['subs']
        tabb.save()
        tr.save()
        return redirect(tr_profile)
    return render(request, 'teacher_update_profile.html', {'key': tr})


def tr_view_students(request):
    tr = teacher_regi.objects.get(user=request.user)
    studs = student_regi.objects.filter(
        st_user__user__username=tr.tr_user.user.username, STUDENTS_DEPARTMENT=tr.TEACHER_DEPARTMENT,is_approved="yes")
    print(tr.TEACHER_DEPARTMENT)

    context = {
        'Studs': studs
    }
    return render(request, 'tr_view_students.html', context)


def tr_add_mark(request, pk):
    sts = student_regi.objects.get(id=pk)
    subs = SUB.objects.get(sem=sts.STUDENTS_SEM)

    context = {
        'st': sts,
        'sub': subs
    }
    print(sts.STUDENTS_NAME)
    if request.method == "POST":
        subb1 = request.POST['sub1']
        subb2 = request.POST['sub2']
        subb3 = request.POST['sub3']
        subb4 = request.POST['sub4']
        subb5 = request.POST['sub5']
        if AD_MAR.objects.filter(user=sts, sub__sem=sts.STUDENTS_SEM):
            print(sts.STUDENTS_SEM)
            ad_markk = AD_MAR.objects.get(user=sts, sub__sem=sts.STUDENTS_SEM)

            TR_MAR(st=sts, sub=subs, ad_mar=ad_markk, TR_MAR1=subb1, TR_MAR2=subb2,
                   TR_MAR3=subb3, TR_MAR4=subb4, TR_MAR5=subb5).save()
            return redirect(tr_view_students)
        else:
            context = {
                'st': sts,
                'sub': subs,
                'msg': 'mark already entered'
            }
            return render(request, "teacher_add_mark.html", context)

    return render(request, "teacher_add_mark.html", context)


def tr_view_mark(request, pk):
    sts = student_regi.objects.get(id=pk)
    if TR_MAR.objects.filter(st__user__username=sts,st__STUDENTS_SEM=sts.STUDENTS_SEM):
        ad_markk = TR_MAR.objects.get(st__user__username=sts,st__STUDENTS_SEM=sts.STUDENTS_SEM)
        return render(request, 'tr_view_mark.html', {"key": ad_markk})
    else:
        return render(request, 'tr_view_mark.html')


def tr_mark_update(request, pk):
    sts = student_regi.objects.get(id=pk)
    tr_mar = TR_MAR.objects.get(st=sts)
    if request.method == 'POST':
        tr_mar.TR_MAR1 = request.POST['subj1']
        tr_mar.TR_MAR2 = request.POST['subj2']
        tr_mar.TR_MAR3 = request.POST['subj3']
        tr_mar.TR_MAR4 = request.POST['subj4']
        tr_mar.TR_MAR5 = request.POST['subj5']
        tr_mar.save()
        return redirect(reverse('tr_view_mark', kwargs={'pk': pk}))

    return render(request, 'tr_view_mark_update.html', {"key": tr_mar})


################## Teacher##########################

################## Student##########################

def st_home(request):
    users = User.objects.get(username=request.user)
    st = student_regi.objects.get(user__username=users)
    return render(request, 'student_home.html', {'key': st})


def st_log(request):
    if request.method == "POST":
        st_name = request.POST['user_name']
        passs = request.POST['pass']
        if student_regi.objects.filter(user__username=st_name).exists():
            st = student_regi.objects.get(user__username=st_name)
            print(st.is_approved)
            if st.is_approved == 'yes':
                u = auth.authenticate(username=st_name, password=passs)
                if u is not None:
                    auth.login(request, u)
                    return redirect(st_home)
                else:
                    context = {
                        'key': 'invailed user'
                    }
                    return render(request, 'student_log.html', context)
            elif st.is_approved == 'no':
                context = {
                    'key': 'user is rejected'
                }
                return render(request, 'student_log.html', context)
            else:
                context = {
                    'key': 'Waiting for Approval '
                }
                return render(request, 'student_log.html', context)

        else:
            context = {
                'key': 'invailed user'
            }
            return render(request, 'student_log.html', context)
    return render(request, 'student_log.html')


def st_reg(request):
    if request.method == "POST":
        student_name = request.POST['st_name']
        student_roll = request.POST['st_rollno']
        student_semm = request.POST['st_sem']
        student_username = request.POST['st_user']
        student_email = request.POST['st_email']
        student_phone = request.POST['st_ph']
        student_address = request.POST['st_address']
        student_age = request.POST['st_age']
        student_sex = request.POST['gender']
        student_qulification = request.FILES['st_qulifi']
        year = request.FILES['yr']
        student_department = request.POST['st_dep']
        student_college = request.POST['clg_name']
        password = request.POST['password']
        conpassword = request.POST['conpass']
        if password == conpassword:
            if student_regi.objects.filter(user__username=student_username).exists() or User.objects.filter(username=student_username).exists():
                context = {
                    'key': 'username exists'
                }
                return render(request, 'student_reg.html', context)
            else:
                User.objects.create_user(
                    username=student_username, email=student_email, password=password).save()
                user = User.objects.get(username=student_username)
                collge_us = college_regi.objects.get(
                    user__username=student_college)
                student_regi(user=user, st_user=collge_us, STUDENTS_NAME=student_name, STUDENTS_ADDRESS=student_address, STUDENTS_PHONE=student_phone, STUDENTS_AGE=student_age,
                             STUDENTS_GENDER=student_sex, STUDENTS_QULIFICATION=student_qulification, STUDENTS_DEPARTMENT=student_department, PIC=year, STUDENTS_ROLL=student_roll, STUDENTS_SEM=student_semm).save()
                context = {
                    'key': 'successfully register '
                }
                return render(request, 'student_reg.html', context)
        else:
            context = {
                'key': 'password does not match'
            }
            return render(request, 'student_reg.html', context)
    return render(request, 'student_reg.html')


def st_profile(request):
    users = User.objects.get(username=request.user)
    st = student_regi.objects.get(user__username=users)
    return render(request, 'student_profile.html', {'key': st})


def st_update_profile(request):
    users = User.objects.get(username=request.user)
    st = student_regi.objects.get(user__username=users)
    if request.method == 'POST':
        tabb = User.objects.get(username=request.user)
        tabb.email = request.POST['st_emails']
        st.STUDENTS_PHONE = request.POST['st_phs']
        st.STUDENTS_AGE = request.POST['st_ages']
        st.STUDENTS_SEM = request.POST['st_sems']
        st.STUDENTS_ADDRESS = request.POST['st_addresss']

        tabb.save()
        st.save()
        return redirect(st_profile)
    return render(request, 'student_update_profile.html', {'key': st})


def student_mark_view(request):
    users = User.objects.get(username=request.user)
    stss = student_regi.objects.get(user__username=users)
    print(stss.STUDENTS_NAME)
    ad_ma = AD_MAR.objects.filter(
        user__user__username=stss.user.username, sub__sem=stss.STUDENTS_SEM)
    tr_ma = TR_MAR.objects.filter(
        st__user__username=stss.user.username, sub__sem=stss.STUDENTS_SEM)
    li=[]
    for i in ad_ma:

        mark1=int(i.AD_MAR1)
        mark2=int(i.AD_MAR2)
        mark3=int(i.AD_MAR3)
        mark4=int(i.AD_MAR4)
        mark5=int(i.AD_MAR5)
        li.append(mark1)
        li.append(mark2)
        li.append(mark3)
        li.append(mark4)
        li.append(mark5)
    for i in tr_ma:

        mark1=int(i.TR_MAR1)
        mark2=int(i.TR_MAR2)
        mark3=int(i.TR_MAR3)
        mark4=int(i.TR_MAR4)
        mark5=int(i.TR_MAR5)
        li.append(mark1)
        li.append(mark2)
        li.append(mark3)
        li.append(mark4)
        li.append(mark5)

        print(mark1)
    s1=sum(li)

    print(s1)  
    cg=s1/50
    print(cg)

    

    context = {
        'key': ad_ma,
        'key1': tr_ma,
        'cg':cg,
        
       

    }

    return render(request, 'student_mark_view.html', context)


################## Student##########################

 ################# Parent###########################
def pt_home(request):
    users = User.objects.get(username=request.user)
    pt = parent_reg.objects.get(user__username=users)
    return render(request, 'parent_home.html',{"key": pt})


def pt_log(request):
    if request.method == "POST":
        pt_name = request.POST['pt_name']
        passs = request.POST['pass']
        if parent_reg.objects.filter(user__username=pt_name).exists():
            pt = parent_reg.objects.get(user__username=pt_name)
            print(pt.is_approved)
            if pt.is_approved == 'yes':
                u = auth.authenticate(username=pt_name, password=passs)
                if u is not None:
                    auth.login(request, u)
                    return redirect(pt_home)
                else:
                    context = {
                        'key': 'invailed user'
                    }
                    return render(request, 'parent_login.html', context)
            elif pt.is_approved == 'no':
                context = {
                    'key': 'user is rejected'
                }
                return render(request, 'parent_login.html', context)
            else:
                context = {
                    'key': 'Waiting for Approval '
                }
                return render(request, 'parent_login.html', context)

        else:
            context = {
                'key': 'invailed user'
            }
            return render(request, 'parent_login.html', context)
    return render(request,'parent_login.html')


def pt_reg(request):
    if request.method == "POST":
        parent_name = request.POST['pt_name']
        parent_username = request.POST['pt_usname']
        parent_email = request.POST['pt_email']
        parent_phone = request.POST['pt_ph']
        parent_relation = request.POST['pt_std']
        parent_st_us = request.POST['pt_stdusername']
        password = request.POST['password']
        conpassword = request.POST['conpass']
        if password == conpassword:
            if parent_reg.objects.filter(user__username=parent_username).exists() or User.objects.filter(username=parent_username).exists():
                context = {
                    'key': 'username exists'
                }
                return render(request, 'parent_register.html', context)
            else:
                User.objects.create_user(
                    username=parent_username, email=parent_email, password=password).save()
                user = User.objects.get(username=parent_username)
                student_us = student_regi.objects.get(
                    user__username=parent_st_us)
                parent_reg(user=user, std_user=student_us, PARENT_NAME=parent_name,
                           PARENT_PHONE=parent_phone, PARENT_RELATION=parent_relation).save()
                context = {
                    'key': 'successfully register '
                }
                return render(request, 'parent_register.html', context)
        else:
            context = {
                'key': 'password does not match'
            }
            return render(request, 'parent_register.html', context)
    return render(request, 'parent_register.html')



def pt_profile(request):
    users = User.objects.get(username=request.user)
    pt = parent_reg.objects.get(user__username=users)
    return render(request, 'parent_profile.html', {'key': pt})


def pt_update_profile(request):
    users = User.objects.get(username=request.user)
    pt = parent_reg.objects.get(user__username=users)
    if request.method == 'POST':
        tabb = User.objects.get(username=request.user)
        tabb.email = request.POST['pt_emails']
        pt.PARENT_PHONE = request.POST['pt_phs']
        pt.PARENT_NAME = request.POST['pt_name']
       
        tabb.save()
        pt.save()
        return redirect(pt_profile)
    return render(request, 'parent_update_profile.html', {'key': pt})

def pt_child_details(request):
    users = User.objects.get(username=request.user)
    pt = parent_reg.objects.get(user__username=users)
    print(pt.std_user.user.username)
    st=student_regi.objects.get(user__username=pt.std_user.user.username)
    return render(request,'parent_child_details.html',{'key': st})

def pt_teacher(request):
    users = User.objects.get(username=request.user)
    pt = parent_reg.objects.get(user__username=users)
    print(pt.std_user.user.username)
    print(pt.std_user.STUDENTS_DEPARTMENT)
    tr=teacher_regi.objects.filter(tr_user__user__username=pt.std_user.st_user.user.username,TEACHER_DEPARTMENT=pt.std_user.STUDENTS_DEPARTMENT)
   
    return render(request,'parent_teacher_list.html',{'key': tr})

def pt_mark_view(request):
    users = User.objects.get(username=request.user)
    pt = parent_reg.objects.get(user__username=users)
    print(pt.PARENT_NAME)
    print(pt.std_user.user.username)
    ad_ma = AD_MAR.objects.filter(user__user__username=pt.std_user.user.username)
        
    tr_ma = TR_MAR.objects.filter(st__user__username=pt.std_user.user.username )
    li=[]
    for i in ad_ma:

        mark1=int(i.AD_MAR1)
        mark2=int(i.AD_MAR2)
        mark3=int(i.AD_MAR3)
        mark4=int(i.AD_MAR4)
        mark5=int(i.AD_MAR5)
        li.append(mark1)
        li.append(mark2)
        li.append(mark3)
        li.append(mark4)
        li.append(mark5)
    for i in tr_ma:

        mark1=int(i.TR_MAR1)
        mark2=int(i.TR_MAR2)
        mark3=int(i.TR_MAR3)
        mark4=int(i.TR_MAR4)
        mark5=int(i.TR_MAR5)
        li.append(mark1)
        li.append(mark2)
        li.append(mark3)
        li.append(mark4)
        li.append(mark5)

        print(mark1)
    s1=sum(li)

    print(s1)  
    cg=s1/50
    print(cg)

    context = {
        'key': ad_ma,
        'key1': tr_ma,
        'cg':cg,

    }

    return render(request, 'parent_mark_view.html', context)



 ################# Parent###########################


def log_out(request):
    logout(request)
    return redirect(index)
def admin_logout_view(request):
    logout(request)
    return redirect(index)

