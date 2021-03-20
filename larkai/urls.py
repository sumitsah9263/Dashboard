from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doc_reg', views.doc_reg, name='doc_reg'),
    path('', include('login.urls')),
    path('home', views.home, name='home'),
    # path('reading',views.reading,name='reading'),
    #path('fetch_value', views.fetch_value, name='fetch_value'),
    # url(r'^fetch_value/$', views.fetch_value, name='fetch_value'),
    # path('fetch_value2', views.fetch_value2, name='fetch_value2'),
    #path('fetch_ecg', views.fetch_ecg, name='ecg'),
    # path('loading', views.loading, name='loading'),
    # path('loading_r', views.loader_reading, name='loading_reading'),
    # path('final', views.final, name='final'),
    path('patient', include('patient.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name="profie"),
    path('final/', views.final, name="final")
]
