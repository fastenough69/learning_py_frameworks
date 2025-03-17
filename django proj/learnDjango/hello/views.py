from django.shortcuts import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, render
from django.http import HttpRequest, JsonResponse
from random import randint as r
from django.core.serializers.json import DjangoJSONEncoder
# from django.template.response import TemplateResponse
# Create your views here.

class Worker:
    def __init__(self, name: str="Undef"):
        self.name = name
        self.id = r(100_000, 999_999)

class WorkerEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if(isinstance(obj, Worker)):
            return {"name": obj.name, "id": obj.id}
        
        return super().default(obj)
    
def index(request: HttpRequest):
    worker = Worker("Ivan")
    data = {"header": "Hello Django, privet lisa", "message": "my first template", "worker": worker}
    return render(request, "index.html", context=data)

def about(request: HttpRequest):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path = request.path

    return HttpResponse(f"""
        <p>Host: {host}</p>
        <p>Path: {path}</p>
        <p>User-agent: {user_agent}</p>
    """)

def help(request: HttpRequest):
    return HttpResponse("<h2>error code 400<h2>", headers={"SecretCode": "21234567"}, status=400, reason="incorrect", content_type="text/plain")

def user(request: HttpRequest, name: str="Undef", age: int=0):
    return HttpResponse(f"<h2>Your name is {name} {age} yearss")

def products(request: HttpRequest, id: int):
    return HttpResponse(f"Товар номер {id}")

def info_product(request: HttpRequest, id: int):
    return HttpResponse(f"О товаре под номером {id}")

def first_hendler(request: HttpRequest):
    age: int = request.GET.get("age", 0)
    name: str = request.GET.get("name", "Undef")
    return HttpResponse(f"{name}: {age} years old")

def help_info(request: HttpRequest):
    return HttpResponseRedirect("/help")

def details(reauest: HttpRequest):
    return HttpResponsePermanentRedirect("/")

def json_out(request: HttpRequest):
    ivan = Worker("Ivan")
    return JsonResponse(ivan, safe=False, encoder=WorkerEncoder)

def set_cck(request: HttpRequest):
    username = request.GET.get("username", "Undef")
    response = HttpResponse(f"Develop {username}")
    response.set_cookie("username", username)
    return response

def get_cck(request: HttpRequest):
    username = request.COOKIES["username"]
    return HttpResponse(f"Ты получил свои куки {username}")
