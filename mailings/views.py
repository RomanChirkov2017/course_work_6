import random

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from blog.models import Blog
from mailings.forms import MailingForm, ClientForm, MessageForm
from mailings.models import MailingSettings, Client, Message, Log


class IndexView(TemplateView):
    template_name = 'mailings/index.html'
    extra_context = {
        'title': 'Главная'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['total_mailings'] = MailingSettings.objects.count()
        context_data['active_mailings'] = MailingSettings.objects.filter(is_active=True).count()
        context_data['unique_clients'] = Client.objects.count()
        context_data['object_list'] = random.sample(list(Blog.objects.all()), min(3, len(Blog.objects.all())))
        return context_data


class MailingListView(ListView):
    model = MailingSettings
    extra_context = {
        'title': 'Ваши рассылки'
    }


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = MailingSettings
    form_class = MailingForm
    success_url = reverse_lazy('mailings:mailing_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class MailingDetailView(DetailView):
    model = MailingSettings

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = MailingSettings.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f'{category_item.title}'

        return context_data


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingSettings
    form_class = MailingForm
    success_url = reverse_lazy('mailings:mailing_list')


class MailingDeleteView(DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailings:mailing_list')


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:client_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientListView(ListView):
    model = Client
    extra_context = {
        'title': 'Ваши клиенты'
    }


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:client_list')


class ClientDetailView(DetailView):
    model = Client

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Client.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f'{category_item.FIO}'

        return context_data


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailings:client_list')


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailings:message_list')


class MessageListView(ListView):
    model = Message
    extra_context = {
        'title': 'Ваши сообщения'
    }


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailings:message_list')


class MessageDetailView(DetailView):
    model = Message

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Message.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f'{category_item.title}'

        return context_data


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailings:message_list')


class LogCreateView(CreateView):
    model = Log
    success_url = reverse_lazy('mailings:log_list')


class LogListView(ListView):
    model = Log
    extra_context = {
        'title': 'Отчеты о рассылках'
    }


class LogDeleteView(DeleteView):
    model = Log
    success_url = reverse_lazy('mailings:log_list')
