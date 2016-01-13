from django.conf.urls import url
from views import ShopList, SignUpView

urlpatterns = [
    url(r'^shoplist/', ShopList.as_view(), name='shoplist'),
    #url(r'^register/', SignUpView.as_view(), name='signup'),
]
