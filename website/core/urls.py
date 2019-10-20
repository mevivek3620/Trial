from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^postsign/$',views.postsign),
    url(r'^logout/',views.logout,name="log"),
    url(r'^$',views.home),
    url(r'^postsignup/',views.postsignup,name='postsignup'),
    url(r'^create/',views.create,name='create'),
    url(r'^upload/',views.upload,name='upload'),
    url(r'^post_create/',views.post_create,name='post_create'),
    url(r'^upload_save/',views.upload_save,name='upload_save'),
    url(r'^postsign/dept/$',views.departments, name='dept'),
    url(r'^postsign/club/$',views.club, name='club'),
    url(r'^postsign/dept/civil/$',views.civil, name='civil'),
    url(r'^postsign/dept/mech/$',views.mech, name='mech'),
    url(r'^postsign/dept/ece/$',views.ece, name='ece'),
    url(r'^postsign/dept/eee/$',views.eee, name='eee'),
    url(r'^postsign/dept/mnc/$',views.mnc, name='mnc'),
    url(r'^postsign/dept/bio/$',views.bio, name='bio'),
    url(r'^postsign/dept/cse/$',views.cse, name='cse'),
    url(r'^postsign/dept/chem/$',views.chem, name='chem'),
    url(r'^postsign/dept/civil/civcourse/$',views.civilcourse, name='civcourse'),
    url(r'^postsign/dept/mech/mccourse/$',views.mechcourse, name='mccourse'),
    url(r'^postsign/dept/ece/eccourse/$',views.ececourse, name='eccourse'),
    url(r'^postsign/dept/eee/eecourse/$',views.eeecourse, name='eecourse'),
    url(r'^postsign/dept/mnc/mnccourse/$',views.mnccourse, name='mnccourse'),
    url(r'^postsign/dept/bio/biocourse/$',views.biocourse, name='biocourse'),
    url(r'^postsign/dept/cse/csecourse/$',views.csecourse, name='csecourse'),
    url(r'^postsign/dept/chem/chemcourse/$',views.chemcourse, name='chemcourse'),

]