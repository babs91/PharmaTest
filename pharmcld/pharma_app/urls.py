from django.urls import path
from . import views



urlpatterns = [

    path('regist/', views.registe, name='signin'),
    path('logn/', views.logpage, name='loginp'),
    path('logO/', views.Logout, name='logof'),
    path('', views.Home, name='Home1'),
    path('adm/', views.administrator, name='admns'),
    path('itm/', views.itempage, name='itmp'),
    path('itm2/',views.itempage2, name='itmp1'),
    path('itm3/', views.itempage3, name='itmp2'),
    path('itm4/', views.itempage4, name='itmp3'),
    path('entry/', views.admnEntry, name='entF'),
    path('entry2/', views.entries, name='entF2'),
    path('val/', views.values, name='vlu'),
    path('delete/<int:id>', views.Delete, name='delt'),
    path('profl/', views.profile, name='prfl'),
    path('updt/<int:id>', views.Update, name='upt'),

]