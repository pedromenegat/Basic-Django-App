from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path("<int:id>/", views.index, name="index"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("home/", views.home, name="home"),
    path("view/", views.view, name="view"),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]