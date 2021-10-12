from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
import jobs.views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',jobs.views.home, name='home'),
    path('blog/',include('blog.urls')),
    path('dash/',include('dash.urls')),
    path('accounts/',include('accounts.urls')),
   
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    