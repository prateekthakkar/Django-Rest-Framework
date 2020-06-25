from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

#Viewsets Routers & Generic Viewsets & Modal Viewsets
router = DefaultRouter()
router.register('article', views.ArticleViewSet, basename="article")

urlpatterns = [
    # path('', views.article,name="article"),
    # path('detail/<int:pk>', views.articleOne,name="articleOne"),
    
    # Class Base Api
    # path('', views.articleView.as_view(),name="article"),
    # path('detail/<int:id>', views.articleDet.as_view(),name="articleOne"),

    # REST Generic Views & Mixins
    # path('mixin/<int:id>', views.GenericApiView.as_view())
    
    #Viewsets Routers & Generic Viewsets & Modal Viewsets
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>',include(router.urls))

]