from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    
    path('admin/logout/',auth_views.LogoutView.as_view(next_page='/'), name='admin_logout'),
    path("",views.index),
    path("log_out",views.log_out),
    
    #################College##########################
    
    path("clg_reg",views.clg_reg),
    path("clg_log",views.clg_log),
    path("clg_home",views.clg_home),
    path("clg_tr_lists",views.clg_tr_lists),
    path("clg_tr_onelist<str:pk>",views.clg_tr_onelist,name='clg_tr_onelist'),
    path("clg_tr_accept<str:pk>",views.clg_tr_accept, name="clg_tr_accept"),
    path("clg_tr_reject<str:pk>",views.clg_tr_reject,name="clg_tr_reject"),
    path("clg_profile",views.clg_profile),
    path("clg_update_profile",views.clg_update_profile),
    path('clg_tr_all_listsss',views.clg_tr_all_listsss),

    #################College##########################

    #################Teacher##########################

    path("tr_reg",views.tr_reg),
    path("tr_log",views.tr_log),
    path("tr_home",views.tr_home),
    path("tr_st_lists",views.tr_st_lists),
    path("tr_st_onelist<str:pk>",views.tr_st_onelist,name='tr_st_onelist'),
    path("tr_st_accept<str:pk>",views.tr_st_accept, name="tr_st_accept"),
    path("tr_st_reject<str:pk>",views.tr_st_reject,name="tr_st_reject"),
    path('tr_pt_lists',views.tr_pt_lists),
    path("tr_pt_onelist<str:pk>",views.tr_pt_onelist,name='tr_pt_onelist'),
    path("tr_pt_accept<str:pk>",views.tr_pt_accept, name="tr_pt_accept"),
    path("tr_pt_reject<str:pk>",views.tr_pt_reject,name="tr_pt_reject"),
    
    path("tr_profile",views.tr_profile),
    path("tr_update_profile",views.tr_update_profile),
    path("tr_view_students",views.tr_view_students),
    path('tr_add_mark<str:pk>',views.tr_add_mark,name="tr_add_mark"),
    path('tr_view_mark<str:pk>',views.tr_view_mark,name="tr_view_mark"),

    path('tr_mark_update<str:pk>',views.tr_mark_update,name="tr_mark_update"),
    
    
    #################Teacher##########################


    #################Student##########################

    path("st_reg",views.st_reg),
    path("st_log",views.st_log),
    path("st_home",views.st_home),
    path("st_profile",views.st_profile),
    path("st_update_profile",views.st_update_profile),
    path("student_mark_view",views.student_mark_view),
   
    
    #################Student##########################

    #################Parent###########################
    path("pt_reg",views.pt_reg),
    path("pt_log",views.pt_log),
    path("pt_home",views.pt_home),
    path("pt_profile",views.pt_profile),
    path("pt_update_profile",views.pt_update_profile),
    path("pt_child_details",views.pt_child_details),
    path('pt_teacher',views.pt_teacher),
    path('pt_mark_view',views.pt_mark_view),

    #################Parent###########################

    ####################Admin#########################
    
    
]
