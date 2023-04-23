from django.urls import path, include
from articles import views


urlpatterns = [
    path('index/', views.index, name="index"),
    path('<int:article_id>/', views.article_view, name="article_view"),
]