from rest_framework import routers
from store.views import *


router = routers.DefaultRouter()

router.register(r'categories', CategoryView, basename="categories")
router.register(r'subcategories', SubCatView, basename="subcategories")
router.register(r'products', ProductView, basename="products")
router.register(r'addlike', AddLike, basename="addlike")
router.register(r'deletelike', DeleteLike, basename="deletelike")
router.register(r'bestproducts', BestProduct, basename="bestproducts")
router.register(r'sliders', SliderView, basename="slider")
router.register(r'reklama', NationalityView, basename="reklama")
router.register(r'news', NewsView, basename="news")
router.register(r'events', EventView, basename="events")
router.register(r'partners', PartnerView, basename="partners")
router.register(r'top_products', TopProductView, basename="top_products")
router.register(r'product_search', ProductSearchView, basename="product_searchs")
