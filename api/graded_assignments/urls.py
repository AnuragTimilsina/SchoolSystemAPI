from api.views import GradedAssignmentListView, GradedAssignmentCreateView
from django.urls import path

urlpatterns = [
    path('', GradedAssignmentListView.as_view()),
    path('create/', GradedAssignmentListView.as_view()),
]