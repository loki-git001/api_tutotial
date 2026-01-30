from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path("", views.api_root),
#     path("snippets/", views.SnippetList.as_view(), name="snippet-list"),
#     path("snippets/<int:pk>/", views.SnippetDetail.as_view(), name="snippet-detail"),
#     path(
#         "snippets/<int:pk>/highlight/",
#         views.SnippetHighlight.as_view(),
#         name="snippet-highlight",
#     ),
#     path("users/", views.UserList.as_view(), name="user-list"),
#     path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)



router = DefaultRouter()
router.register(r"snippets", views.SnippetViewSet, basename="snippet")
router.register(r"users", views.UserViewSet, basename="user")


urlpatterns = [
    path("", include(router.urls)),
    path(
        "snippets/<int:pk>/login/",
        views.OwnerOnlyLoginView.as_view(),
        name="snippet-owner-login",
    ),
]