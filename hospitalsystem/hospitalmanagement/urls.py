




from django.contrib import admin
from django.urls import path,include
from hospital import views
from django.contrib.auth.views import LoginView,LogoutView
from donor import views as d
from patient import views as p
from blood import views as b

#-------------FOR ADMIN RELATED URLS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),

    # path('accounts/', include('django.contrib.auth.urls')),
    # path(r'^accounts/login/$', include('django.contrib.auth.urls')),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),


    path('adminclick', views.adminclick_view),
    path('doctorclick', views.doctorclick_view),
    path('patientclick', views.patientclick_view),

    path('adminsignup', views.admin_signup_view),
    path('doctorsignup', views.doctor_signup_view,name='doctorsignup'),
    path('patientsignup', views.patient_signup_view),
    
    
    path('adminlogin', LoginView.as_view(template_name='hospital/adminlogin.html')),
    path('doctorlogin', LoginView.as_view(template_name='hospital/doctorlogin.html')),
    path('patientlogin', LoginView.as_view(template_name='hospital/patientlogin.html')),


    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='hospital/index.html'),name='logout'),


    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('admin-doctor', views.admin_doctor_view,name='admin-doctor'),
    path('admin-view-doctor', views.admin_view_doctor_view,name='admin-view-doctor'),
    path('delete-doctor-from-hospital/<int:pk>', views.delete_doctor_from_hospital_view,name='delete-doctor-from-hospital'),
    path('update-doctor/<int:pk>', views.update_doctor_view,name='update-doctor'),
    path('admin-add-doctor', views.admin_add_doctor_view,name='admin-add-doctor'),
    path('admin-approve-doctor', views.admin_approve_doctor_view,name='admin-approve-doctor'),
    path('approve-doctor/<int:pk>', views.approve_doctor_view,name='approve-doctor'),
    path('reject-doctor/<int:pk>', views.reject_doctor_view,name='reject-doctor'),
    path('admin-view-doctor-specialisation',views.admin_view_doctor_specialisation_view,name='admin-view-doctor-specialisation'),


    path('admin-patient', views.admin_patient_view,name='admin-patient'),
    path('admin-view-patient', views.admin_view_patient_view,name='admin-view-patient'),
    path('delete-patient-from-hospital/<int:pk>', views.delete_patient_from_hospital_view,name='delete-patient-from-hospital'),
    path('update-patient/<int:pk>', views.update_patient_view,name='update-patient'),
    path('admin-add-patient', views.admin_add_patient_view,name='admin-add-patient'),
    path('admin-approve-patient', views.admin_approve_patient_view,name='admin-approve-patient'),
    path('approve-patient/<int:pk>', views.approve_patient_view,name='approve-patient'),
    path('reject-patient/<int:pk>', views.reject_patient_view,name='reject-patient'),
    path('admin-discharge-patient', views.admin_discharge_patient_view,name='admin-discharge-patient'),
    path('discharge-patient/<int:pk>', views.discharge_patient_view,name='discharge-patient'),
    path('download-pdf/<int:pk>', views.download_pdf_view,name='download-pdf'),


    path('admin-appointment', views.admin_appointment_view,name='admin-appointment'),
    path('admin-view-appointment', views.admin_view_appointment_view,name='admin-view-appointment'),
    path('admin-add-appointment', views.admin_add_appointment_view,name='admin-add-appointment'),
    path('admin-approve-appointment', views.admin_approve_appointment_view,name='admin-approve-appointment'),
    path('approve-appointment/<int:pk>', views.approve_appointment_view,name='approve-appointment'),
    path('reject-appointment/<int:pk>', views.reject_appointment_view,name='reject-appointment'),
        # path('bloodbank/admin/', admin.site.urls),

    
    path('donor/',include('donor.urls')),
    path('patient/',include('patient.urls')),

    
    path('bloodbank/',b.home_view,name=''),
    path('bloodbank/logout', LogoutView.as_view(template_name='blood/logout.html'),name='blood-logout'),

    path('bloodbank/afterlogin', b.afterlogin_view,name='blood-afterlogin'),
    path('bloodbank/adminlogin', LoginView.as_view(template_name='blood/adminlogin.html'),name='blood-adminlogin'),
    path('bloodbank/admin-dashboard', b.admin_dashboard_view,name='blood-admin-dashboard'),
    path('bloodbank/admin-blood', b.admin_blood_view,name='admin-blood'),
    path('bloodbank/admin-donor', b.admin_donor_view,name='admin-donor'),
    path('bloodbank/admin-patient', b.admin_patient_view,name='admin-patient'),
    path('bloodbank/update-donor/<int:pk>', b.update_donor_view,name='update-donor'),
    path('bloodbank/delete-donor/<int:pk>', b.delete_donor_view,name='delete-donor'),
    path('bloodbank/admin-request', b.admin_request_view,name='admin-request'),
    path('bloodbank/update-patient/<int:pk>', b.update_patient_view,name='update-patient'),
    path('bloodbank/delete-patient/<int:pk>', b.delete_patient_view,name='delete-patient'),
    path('bloodbank/admin-donation', b.admin_donation_view,name='admin-donation'),
    path('bloodbank/approve-donation/<int:pk>', b.approve_donation_view,name='approve-donation'),
    path('bloodbank/reject-donation/<int:pk>', b.reject_donation_view,name='reject-donation'),
    path('bloodbank/admin-request-history', b.admin_request_history_view,name='admin-request-history'),
    path('bloodbank/update-approve-status/<int:pk>', b.update_approve_status_view,name='update-approve-status'),
    path('bloodbank/update-reject-status/<int:pk>', b.update_reject_status_view,name='update-reject-status'),
]


#---------FOR DOCTOR RELATED URLS-------------------------------------
urlpatterns +=[
    path('doctor-dashboard', views.doctor_dashboard_view,name='doctor-dashboard'),
    path('search', views.search_view,name='search'),

    path('doctor-patient', views.doctor_patient_view,name='doctor-patient'),
    path('doctor-view-patient', views.doctor_view_patient_view,name='doctor-view-patient'),
    path('doctor-view-discharge-patient',views.doctor_view_discharge_patient_view,name='doctor-view-discharge-patient'),

    path('doctor-appointment', views.doctor_appointment_view,name='doctor-appointment'),
    path('doctor-view-appointment', views.doctor_view_appointment_view,name='doctor-view-appointment'),
    path('doctor-delete-appointment',views.doctor_delete_appointment_view,name='doctor-delete-appointment'),
    path('delete-appointment/<int:pk>', views.delete_appointment_view,name='delete-appointment'),
]




#---------FOR PATIENT RELATED URLS-------------------------------------
urlpatterns +=[

    path('patient-dashboard', views.patient_dashboard_view,name='patient-dashboard'),
    path('patient-appointment', views.patient_appointment_view,name='patient-appointment'),
    path('patient-book-appointment', views.patient_book_appointment_view,name='patient-book-appointment'),
    path('patient-view-appointment', views.patient_view_appointment_view,name='patient-view-appointment'),
    path('patient-view-doctor', views.patient_view_doctor_view,name='patient-view-doctor'),
    path('searchdoctor', views.search_doctor_view,name='searchdoctor'),
    path('patient-discharge', views.patient_discharge_view,name='patient-discharge'),
    path('doctor-view-patient', views.doctor_view_patient_view,name='doctor-view-patient'),

]

# Nurse URLS

urlpatterns +=[
    path('nurseclick', views.nurseclick_view),
    path('nursesignup', views.nurse_signup_view),
    path('nurselogin', LoginView.as_view(template_name='hospital/nurselogin.html')),
    path('nurse-dashboard', views.nurse_dashboard_view,name='nurse-dashboard'),
    path('nurse-appointment', views.nurse_appointment_view,name='nurse-appointment'),
    path('nurse-book-appointment', views.nurse_book_appointment_view,name='nurse-book-appointment'),
    path('nurse-view-appointment', views.nurse_view_appointment_view,name='nurse-view-appointment'),
    path('nurse-approve-appointment', views.nurse_approve_appointment_view,name='nurse-approve-appointment'),
    path('searchdoctor', views.search_doctor_view,name='searchdoctor'),
    path('nurse-patient', views.nurse_patient_view,name='nurse-patient'),
    path('search', views.search_view,name='search'),
    path('nurse-view-patient', views.nurse_view_patient_view,name='nurse-view-patient'),
    path('nurse-view-discharge-patient',views.nurse_view_discharge_patient_view,name='nurse-view-discharge-patient'),

    path('nurse-delete-appointment',views.nurse_delete_appointment_view,name='nurse-delete-appointment'),
    path('delete-appointment/<int:pk>', views.delete_appointment_view_,name='delete-appointment'),
]

