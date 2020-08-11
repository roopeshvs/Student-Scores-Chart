from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from ScoresAPI import views

urlpatterns = [
  path(r'students/', views.get_students),
  path(r'scores/<int:id>/', views.get_scores),
  path(r'add-score/', views.put_score)
]