from django.urls import path
from .views import HomePage, showrec

urlpatterns = [
    path('', HomePage.as_view()),
    path('showrec/<int:pk>', showrec.as_view())
]
