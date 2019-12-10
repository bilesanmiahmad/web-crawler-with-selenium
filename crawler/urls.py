from django.urls import path
from crawler.views import BookingView

urlpatterns = [
    path('bookings/', BookingView.as_view()),
]