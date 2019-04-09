import json

from django.core.serializers import serialize
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from updates.mixins import JsonResponseMixin
from django.views.generic import View

from .models import Updates

def detail_view(request):
    return HttpResponse(get_template(), render())


def update_model_detail_view(request):
    data = {
        "count":100,
        "content":"Some new content"
    }
    json_data = json.dumps(data)
    #return JsonResponse(data)
    return HttpResponse(json_data, content_type='application/json')

class JsonCBV(View):

    def get(self, request, *args, **kwargs):

        data = {
            "count":100,
            "content":"Some new content"
        }
        json_data = json.dumps(data)
        #return JsonResponse(data)
        
        return HttpResponse(json_data, content_type='application/json')

class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):

        data = {
            "count":100,
            "content":"Some new content"
        }
        return self.render_to_json_response(data)


class SerializedDetailView(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        obj = Updates.objects.get(id=1)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        json_data = Updates.objects.all().serialize()
        return HttpResponse(json_data, content_type='application/json')
 
