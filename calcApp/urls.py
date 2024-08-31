from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),]
htmx_urlpatterns=[
    path('check_footprint/',views.home,name='check_footprint')
]

urlpatterns +=htmx_urlpatterns