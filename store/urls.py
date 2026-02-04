from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet,basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts',views.CartViewSet)
router.register('customers',views.CustomerViewSet)
router.register('orders',views.OrderViewSet)

# creating child route
products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet,
                         basename='product-review')

# creating child router for carts

cart_item_router = routers.NestedDefaultRouter(router,'carts',lookup='cart')
cart_item_router.register('items',views.CartItemViewSet,basename='cart-item')

# url configuration
urlpatterns = router.urls + products_router.urls +cart_item_router.urls
