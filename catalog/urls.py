from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contact, IndexView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contact, name='contact'),
    path('product/<pk>', ProductDetailView.as_view(), name='product')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
