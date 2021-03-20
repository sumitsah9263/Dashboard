from django.urls import path
from . import views
from larkai import views as v

urlpatterns = [
    path('/', views.pat, name='patient'),
    path('/new', v.home, name='patient_reg'),
    path('/visit/<str:patient_id>', views.visit, name='visit'),
    path('/visit/detail/<str:visit_id>', views.detail, name='detail')
]
