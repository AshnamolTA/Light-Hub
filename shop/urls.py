from django.urls import path

from shop import views


urlpatterns = [
    path("register/",views.SignUpView.as_view(),name="signup"),
    path("",views.SignInView.as_view(),name="signin"),
    path("index/",views.IndexView.as_view(),name="index"),
    path('logout',views.LogoutView.as_view(),name="signout"),
    path('profile/change/',views.UserProfileEditView.as_view(),name="profile_edit"),
    path("category/<int:pk>/lights/",views.CategoryDetailView.as_view(),name='category_list'),
    path("lights/",views.LightListView.as_view(),name='light_list'),
    path("lights/<int:pk>/detail/",views.LightDetailView.as_view(),name='light_detail'),
    path("light/<int:pk>/wishlist/",views.AddToWishlistItemView.as_view(),name='wishlist'),
]
