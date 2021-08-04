from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
import myFunctions
import format_1
import main_format_2

# Create your views here.
@api_view(['GET', 'POST'])
def query_result(req):
    htmlStr = ""
    queryString = req.data.get("query")
    print(queryString)
    json_data = myFunctions.get_data(queryString)
    if(json_data["headers"] == ['date', 'season', 'day', 'site', 'week', 'line', 'total', 'overtime', 't:team', 't:points', 't:rushes', 't:rushing yards', 't:passes', 't:passing yards', 't:completions', 't:quarter scores', 't:turnovers', 'o:team', 'o:points', 'o:rushes', 'o:rushing yards', 'o:passes', 'o:passing yards', 'o:completions', 'o:quarter scores', 'o:turnovers']):
        htmlStr = main_format_2.get_output_format(json_data)
    elif (json_data["headers"] == ['t:team', 't:points', 'o:points', 't:line', 'total']):
        htmlStr = format_1.get_output_format(json_data)
    else:
        return HttpResponse(JSONRenderer().render({'htmlString': "<h1>Invalid Query</h1>"}), content_type='application/json')
    data = JSONRenderer().render({'htmlString': htmlStr})
    response = HttpResponse(data, content_type='application/json')
    # response["Access-Control-Allow-Origin"] = "*"
    # response["Access-Control-Allow-Methods"] = "GET, OPTIONS, POST"
    return response