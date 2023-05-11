from rest_framework.routers import SimpleRouter
from app import views


router = SimpleRouter()

router.register(r'category', views.CategoryViewSet, 'Category')
router.register(r'region', views.RegionViewSet, 'Region')
router.register(r'tender', views.TenderViewSet, 'Tender')
router.register(r'company', views.CompanyViewSet, 'Company')
router.register(r'documentbid', views.DocumentBidViewSet, 'DocumentBid')

urlpatterns = router.urls
