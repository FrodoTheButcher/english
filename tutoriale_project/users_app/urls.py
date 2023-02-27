
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", views.registerUser,name='register'),
    path("", views.loginUser,name='login'),
    path("logout/",views.logoutUser,name='logout'),
    path("account/<str:pk>/",views.account,name='account'),    
    path("edit_profile/<str:pk>/",views.update_profile,name="update_profile"),
    path("delete_profile/<str:pk>/",views.delete_account,name="delete_user"),
]

urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

