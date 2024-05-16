from django.urls import path
from django.views.decorators.cache import cache_page

from mailings.apps import MailingsConfig
from mailings.views import IndexView, MailingCreateView, MailingListView, ClientCreateView, ClientListView, \
    MessageListView, MessageCreateView, LogListView, MailingDetailView, MailingUpdateView, MailingDeleteView, \
    LogDeleteView, ClientUpdateView, ClientDetailView, ClientDeleteView, MessageUpdateView, MessageDetailView, \
    MessageDeleteView

app_name = MailingsConfig.name

urlpatterns = [
    path('', cache_page(60)(IndexView.as_view()), name='index'),
    path('mailing_create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/update/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing_list/', MailingListView.as_view(), name='mailing_list'),
    path('<int:pk>/mailing_detail', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/delete/<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('<int:pk>/client_detail', ClientDetailView.as_view(), name='client_detail'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),
    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('message/update/<int:pk>', MessageUpdateView.as_view(), name='message_update'),
    path('<int:pk>/message_detail', MessageDetailView.as_view(), name='message_detail'),
    path('message/delete/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),
    path('log_list/', LogListView.as_view(), name='log_list'),
    path('log/delete/<int:pk>', LogDeleteView.as_view(), name='log_delete'),
]
