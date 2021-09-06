from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
import myFunctions
import format_1
import main_format_2
import format_3
import time

# Create your views here.
@api_view(['GET', 'POST'])
def query_result(req):
    htmlStr = ""
    queryString = req.data.get("query")
    sport = req.data.get("sport")
    #time1 = time.time()
    json_data, format_no, grouper = myFunctions.get_data(queryString, sport)
    #time2 = time.time()
    #print("Time 1:", time2 - time1)
    if len(json_data["headers"]) == 0:
        return HttpResponse(JSONRenderer().render({'htmlString': "<h1 id=\"invalid-query\">Invalid Query</h1>"}), content_type='application/json')
    elif format_no == 1:
        htmlStr = format_1.get_output_format(json_data, grouper)
    elif format_no == 2:
        htmlStr = main_format_2.get_output_format(json_data)
    elif format_no == 3:
        htmlStr = format_3.get_output_format(json_data)
    else:
        return HttpResponse(JSONRenderer().render({'htmlString': "<h1 id=\"invalid-query\">Invalid Query</h1>"}), content_type='application/json')
    data = JSONRenderer().render({'htmlString': htmlStr})
    response = HttpResponse(data, content_type='application/json')
    # response["Access-Control-Allow-Origin"] = "*"
    # response["Access-Control-Allow-Methods"] = "GET, OPTIONS, POST"
    #time3 = time.time()
    #print("End: ", time3 - time1)
    return response