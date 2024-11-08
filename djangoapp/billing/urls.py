from django.urls import path
from .views import (
    BillingView, PackView, PackCreateView, PackUpdateView,
    PackOrderFormView, SubscriptionView, SubscriptionCreateView,
    SubscriptionUpdateView, PaymentView, PaymentUserView,
    PaymentCreateView, PaymentUpdateView, PaymentDeleteView
)

app_name = 'billing'

urlpatterns = [
    # Billing
    path('billing/', BillingView.as_view(), name='billing_home'),
    # Pack
    path('pack/', PackView.as_view(), name='pack_home'),
    path('pack/create/', PackCreateView.as_view(), name='pack_create'),
    path('pack/update/<int:pk>/', PackUpdateView.as_view(),
         name='pack_update'),
    path('pack/order/', PackOrderFormView.as_view(), name='pack_order'),
    # Subscription
    path('subscription/', SubscriptionView.as_view(),
         name='subscription_home'),
    path('subscription/create/', SubscriptionCreateView.as_view(),
         name='subscription_create'),
    path('subscription/update/<int:pk>/', SubscriptionUpdateView.as_view(),
         name='subscription_update'),
    # Payment
    path('payment/', PaymentView.as_view(), name='payment_home'),
    path('payment/user/<int:pk>/', PaymentUserView.as_view(),
         name='payment_user'),
    path('payment/create/<int:pk>', PaymentCreateView.as_view(),
         name='payment_create'),
    path('payment/update/<int:pk>/', PaymentUpdateView.as_view(),
         name='payment_update'),
    path('payment/delete/<int:pk>/', PaymentDeleteView.as_view(),
         name='payment_delete'),
]
