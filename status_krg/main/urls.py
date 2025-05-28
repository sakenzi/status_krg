from django.urls import path
from .views import *


urlpatterns = [
    path('information/', InformationView.as_view(), name='information'),
    path('type_activity/', TypeActivityView.as_view(), name='type_activity'),
    path('activity/<int:type_activity_id>/', ActivityView.as_view(), name='activity'),
    path('repair/', RepairView.as_view(), name='repair'),
    path('certificate/', CertificateView.as_view(), name='certificate'),
    path('project/', ProjectView.as_view(), name='project'),
    path('feed_back/', FeedbackView.as_view(), name='feed-back'),
    path('link/', LinkView.as_view(), name='link'),
]