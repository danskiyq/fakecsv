import os
from time import sleep

from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .owner import OwnerListView, OwnerUpdateView, OwnerDeleteView, parse_instructions, save_schema, gen_fake_csv
from fakecsv.tasks import generate_fake_data


class SchemaCreateView(LoginRequiredMixin, CreateView):
    model = Schema
    fields = ['name', 'separator', 'string']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['names'] = serialize("json", Schema.objects.filter(owner=self.request.user))
        context['separator'] = None
        context['string'] = None
        context['objects'] = None
        context['mode'] = 'Create'
        return context

    def post(self, request, **kwargs):
        owner = request.user
        items = request.POST

        save_schema(items, owner)

        return redirect('fakecsv:edit')


class SchemaListView(OwnerListView):
    model = Schema


class SchemaDeleteView(OwnerDeleteView):
    model = Schema

    def post(self, request, *args, **kwargs):
        path = settings.MEDIA_ROOT + '/' + str(self.request.user.id) + '/' + f'{self.get_object().name}.csv'
        if self.get_object().created_date:
            os.remove(path)
        return super().post(request)


class SchemaUpdateView(OwnerUpdateView):
    model = Schema
    fields = ['name', 'separator', 'string']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = str(self.get_object().name)
        context['separator'] = self.get_object().separator
        context['string'] = self.get_object().string
        objects = parse_instructions(self.get_object().read_instructions)
        context['objects'] = objects
        context['names'] = serialize("json", Schema.objects.filter(owner=self.request.user))
        context['mode'] = 'Update'
        return context

    def post(self, request, **kwargs):
        owner = request.user
        items = request.POST

        save_schema(items, owner, schema=self.get_object(), update=True)

        return redirect('fakecsv:edit')


class GenerateCsvView(OwnerListView):
    model = Schema
    template_name = 'fakecsv/generate_csv_list.html'

    def post(self, request):
        owner = request.user
        rows = int(request.POST.get('rows'))
        generate_fake_data.delay(owner.id, rows)
        return super(GenerateCsvView, self).get(request)

