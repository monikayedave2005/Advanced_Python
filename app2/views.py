from django.shortcuts import render,redirect
from django.http import HttpResponse


data={}
def admission(request):
    if request.method=="POST":
        data["id"]=request.POST.get("id")
        data["name"]=request.POST.get("name")

        data["dsa"]=int(request.POST.get("dsa"))
        data["cpp"]=int(request.POST.get("cpp"))
        data["python"]=int(request.POST.get("python"))
        data["java"]=int(request.POST.get("java"))
        data["html"]=int(request.POST.get("html"))
        

        total= (
            data["dsa"]+
            data["cpp"]+
            data["python"]+
            data["java"]+
            data["html"]
        )

        percentage=total/5
        
        if percentage>=90:
            grade="A"
        elif percentage>=70:
            grade="B"
        elif percentage>=50:
            grade="C"
        else:
            grade="Fail"
            
        data["total"]=total
        data["percentage"]=percentage
        data["grade"]=grade
        
       
        return redirect("/result/")

    return render(request,"student_registration.html")

def result(request):
    return render(request,"result.html",data)

