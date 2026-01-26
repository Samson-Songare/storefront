from . import views
from rest_framework.routers import SimpleRouter,DefaultRouter


router = DefaultRouter()
router.register('products',views.ProductViewSet)
router.register('collections',views.CollectionViewSet)


# url configuration
urlpatterns = router.urls
