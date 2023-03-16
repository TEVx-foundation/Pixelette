from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import pixelizer

app_name = "api"
urlpatterns = [
     path("encode/", pixelizer.encode, name = "encode"),
     path("decode/", pixelizer.decode, name = "decode"),
     path("list/", pixelizer.listAll, name = "listAll"),
]