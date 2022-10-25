from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='result'),
    # ex: /polls/5/results/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # ex: /polls/5/vote/
]

# Ancien Routage
# urlpatterns = [
#     path('', views.IndexView, name='index'),
#     path('<int:question_id>/', views.DetailView, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.ResultsView, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]
