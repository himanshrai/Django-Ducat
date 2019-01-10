from django.shortcuts import render,HttpResponse

def homepage(request):
	a=" Hello world"
	return HttpResponse(f"<h1>This is first view.{a} {request}</h1>")

# Create your views here.
