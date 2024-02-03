from django.contrib import admin
from django.urls import path
from ya_afisha.views import where_to_go

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', where_to_go),
]
