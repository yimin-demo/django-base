from django.shortcuts import render

from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import redirect

import json

from django.views.generic import View



def index(request: HttpRequest) -> HttpResponse:
    context = {'title':'test', 'content':'click'}
    return  render(request, 'book/index.html', context)

def shop(request: HttpRequest, id1, id2):
    query_params = request.GET
    print(query_params.get('order'))
    return HttpResponse('1111')
    # return JsonResponse({'id1':id1, 'id2':id2})

def post(request: HttpRequest):
    data = request.POST
    print(data)
    a = request.POST.get('a')
    b = request.POST.get('b')
    alist = request.POST.getlist('a')
    print(a)
    print(b)
    print(alist)
    return HttpResponse('post OK')

def post_json(request: HttpRequest):
    json_str = request.body
    print(json_str)
    # json_str = json_str.decode()  # python>=3.6 无需执行此步
    req_data = json.loads(json_str)
    print(req_data)

    print(request.META['REMOTE_ADDR'])
    return HttpResponse('post json OK')

def response(request: HttpRequest):

    # return HttpResponse('response')

    info = {'name':'yimin', 'address':'local'}

    friends = [
        {
            'name': 'rose',
            'address': 'here'
        },
        {
            'name': 'sherry',
            'address':'there'
        }
    ]
    return JsonResponse(data=friends, safe=False)

def test_redirect(request: HttpRequest):
    return redirect('/index')

def set_cookie(request: HttpRequest):
    response = HttpResponse('set_cookie')
    username = request.GET.get("username")
    password = request.GET.get("password")

    response.set_cookie('name', username)
    response.set_cookie('pwd', password)
    return response

def get_cookie(request: HttpRequest):
    print(request.COOKIES)
    name=request.COOKIES.get('name')
    return HttpResponse(name)


def set_session(request: HttpRequest):
    username = request.GET.get("username")
    password = request.GET.get("password")

    user_id = 1
    request.session['user_id'] = user_id
    request.session['username'] = username
    request.session['password'] = password

    return HttpResponse('set_session')


def get_session(request: HttpRequest):

    user_id = request.session.get('user_id')
    username = request.session.get('username')
    password = request.session.get('password')
    
    content = '{}, {}, {}'.format(user_id, username, password)

    return HttpResponse(content)


def login(request: HttpRequest):
    print(request.method)
    if request.method == 'GET':
        return HttpResponse('GET method')
    if request.method == 'POST':
        return HttpResponse('POST method')
    return HttpResponse('login')


class LoginView(View):

    def get(self, request):

        return HttpResponse('GET')
    
    def post(self, request):
        
        return HttpResponse('POST')