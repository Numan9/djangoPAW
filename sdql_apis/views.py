from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import myFunctions
import format_1
import main_format_2
import format_3
import jwt
from .serializers import UserSerializer
from .models import User
import datetime

# Create your views here.
@api_view(['GET', 'POST'])
def query_result(req):
    htmlStr = ""
    queryString = req.data.get("query")
    sport = req.data.get("sport")
    json_data, format_no, grouper = myFunctions.get_data(queryString, sport)
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
    return response


@api_view(['GET', 'POST'])
def login(req):
    email = req.data.get('email')
    password = req.data.get('password')
    print(email, password)
    user = User.objects.filter(email=email).first()

    if user is None:
        #raise AuthenticationFailed('User not found')
        return Response({'message': 'Not Found'})
    
    if not user.check_password(password):
        #raise AuthenticationFailed('Incorrect password')
        return Response({'message': 'Incorrect'})
    
    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, 'secret', algorithm='HS256')

    res = Response()
    res.set_cookie(key='jwt', value=token, httponly=True)

    res.data = {
        'message': 'Logged In', "payload": payload, "token": token
    }

    return res


@api_view(['GET', 'POST'])
def register(req):
    if not User.objects.filter(email=req.data.get('email')).exists():
        serializer = UserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'R'})
    else:
        return Response({'message': 'A'})


@api_view(['GET'])
def checkAuthentication(req):
    token = req.COOKIES.get('jwt')
    if not token:
        return Response({"message": "No Token", "token": token})
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return Response({"message": "Expired Token", "token": token})
    return Response({"message": "OK", "token": token})


@api_view(['GET'])
def logout(req):
    res = Response()
    res.delete_cookie('jwt')
    res.data = {
        'message': 'Logged Out'
    }
    return res