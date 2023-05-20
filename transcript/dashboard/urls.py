from django.urls import path, include
from django.contrib import admin
from . import views
from .views import grades_pdf
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="home"),
    path("login/", views.login, name="login"),
    path('logout/', views.logout, name='logout'),
    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/grades_pdf', views.grades_pdf, name='grades_pdf'),

]


