from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet,basename='products')
router.register('collections', views.CollectionViewSet)

# creating child route
products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet,
                         basename='product-review')

# url configuration
urlpatterns = router.urls + products_router.urls
