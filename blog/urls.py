from django.urls import path
from .views import index, about, contact,product, remot, video, videodetailView, remotdetailView

urlpatterns = [
    path("product<int:id>", remotdetailView, name="remot_list_view"),
    path("video<int:id>", videodetailView, name="video_list_view"),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('product/', product, name='product'),
    path('remot/', remot, name='remot'),
    path('video/', video, name='video'),
]