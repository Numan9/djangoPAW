from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def query_result(req):
    data = JSONRenderer().render({'htmlString': '12345'})
    response = HttpResponse(data, content_type='application/json')
    # response["Access-Control-Allow-Origin"] = "*"
    # response["Access-Control-Allow-Methods"] = "GET, OPTIONS, POST"
    return response