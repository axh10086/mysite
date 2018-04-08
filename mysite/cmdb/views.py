from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

n=[]

def index(request):
    #request.POST
    #request.GET
    #return HttpResponse("Hello World")
    if request.method == "post":
        n1 = request.POST.get("n1",int)
        n2 = request.POST.get("n2", int)
        global n
        n.append(n1+n2)
    return render(request,"index.html",{"data":n})