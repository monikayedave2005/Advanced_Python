from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here
# def home(request):
#     return HttpResponse("I am app1 homepage !")

# #get id from url
# def get_id(request,id):
#     return HttpResponse(f"Hello {id} no student")

# def get_name(request,name):
#     return HttpResponse(f"Hello I am {name}")

# def get_id_name(request,id,name):
#    return HttpResponse(f"Hello !!! roll_no : {id} name :  {name}")

# def home_html(request):
#     if request.method=="POST":
#         uname=request.POST.get("fname")
#         return render(request,"home.html",{"name": uname})
#     return render(request,"home.html")

# def view_cal(request):
#     return render(request,"calci.html")

# def calculation(request):
#     if request.method=="POST":
#         num1=int(request.POST.get("num1"))
#         num2=int(request.POST.get("num2"))
#         op=num1+num2
#         print(op)
#         data={
#             "num1": num1,
#             "num2": num2,
#             "op": op
#         }
#         return render(request,"calci.html",data)
#     return render(request,"calci.html")
data={}
def show_regi(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("pass")
        data["name"]=name
        data["email"]=email
        data["password"]=password
        print(data["name"],data["email"],data["password"])
        return redirect("/login/")

    return render(request,"registration.html")

def login(request):
    msg=""
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("pass")
        if email==data["email"] and password==data["password"]:
            return redirect("/home/")
        else:
            msg="Invalid credintials"
    return render(request,"login.html",{"msg":msg})

def home(request):
    return render(request,"home.html",data)