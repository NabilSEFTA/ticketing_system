from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from ticketsManagement import urls as ticketsUrls

urlpatterns = [
    
    path(r'ticketManagement/', include('ticketsManagement.urls'))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
