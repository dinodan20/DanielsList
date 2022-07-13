from django.contrib import admin
from django.urls import path, include
from .views import RingViewSet, UserViewSet, GroupViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'ringset', RingViewSet, basename="ringview")
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

ring_list = RingViewSet.as_view({
    'get':'list',
    'post':'create'
})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]

'''
urlpatterns = format_suffix_patterns([
    #path('', api_root),
    path('ringset/', ring_list, name='ring-list'),
])
'''
