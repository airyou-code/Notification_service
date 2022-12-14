from .api.views import ClientAPIView, MailingAPIView, MessageAPIList

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'client', ClientAPIView, basename='client')
router.register(r'mailing', MailingAPIView, basename='mailing')
router.register(r'message', MessageAPIList, basename='message')

urlpatterns = router.urls