from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.apps import BlogConfig
from blog.views import

app_name = BlogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', ContactView.as_view(), name='contact'),
    path('product/<pk>', ProductDetailView.as_view(), name='product')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
