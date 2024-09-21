
from django.contrib import admin
from django.urls import path
from ws_rollibit.views import FingersView,A

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pushfingers/", FingersView.as_view()),
    path('abc/', A.as_view())
]
