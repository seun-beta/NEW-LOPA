from django.urls import path

from . import views

urlpatterns = [
    path('cause', views.CauseData.as_view()),
    path('cause_barrier', views.CauseBarrierData.as_view()),
    path('consequence', views.ConsequenceData.as_view()),
    path('consequence_barrier', views.ConsequenceBarrierData.as_view()),
    path('event', views.EventData.as_view()),
]