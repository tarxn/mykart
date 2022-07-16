from django.contrib import admin
from django.urls import path


from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index , name = "ShopHome"),
    path("about/",views.about , name = "About us"),
    path("contact/", views.contact,name ="Contact us"),
    path("search/", views.search, name = "search"),
    path("track/", views.tracker, name = "tracker"),
    path("products/<int:myid>", views.prodView, name = "prodView"),
    path("checkout/", views.checkout, name = "checkout")

]