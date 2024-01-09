from django.urls import path
from .views import token_page

urlpatterns = [
    path('tokens/', token_page, name='token_page'),
    path('tokens/<int:token_id>/', token_page, name='token_page_detail'),
]
# from django.urls import path
# from .views import TokenListView, TokenDetailView, purchase_token
#
# urlpatterns = [
#     path('tokens/', TokenListView.as_view(), name='token_list'),
#     path('tokens/<int:pk>/', TokenDetailView.as_view(), name='token_detail'),
#     path('tokens/purchase/<int:token_id>/', purchase_token, name='purchase_token'),
#     # Add other URL patterns as needed
# ]
