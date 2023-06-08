
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("HOME.urls")),
    path('CONTACTS/', include("CONTACTS.urls"))
]