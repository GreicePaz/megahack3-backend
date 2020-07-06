from django.urls import path
from megahack import *
from api.views import *

urlpatterns = [
    path('', HelloWord.as_view()),
    path('ong', OngAPI.as_view()),
    path('ong/<int:id>', OngAPI.as_view()),
    path('ongs', OngAPIList.as_view()),
    path('need/product', NeedProductAPI.as_view()),
    path('need/product/<int:id>', NeedProductAPI.as_view()),
    path('need/bill', NeedBillAPI.as_view()),
    path('need/bill/<int:id>', NeedBillAPI.as_view()),
    path('tags/', TagAPI.as_view()),
    path('search', ProductsMeli.as_view()),
    path('grantor', GrantorAPI.as_view()),   
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.conf.urls.static import static

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)