from django.shortcuts import render,HttpResponse
# Create your views here.
def home(request):
    return HttpResponse ("<center><h1><b>welcome to home page")
def aboutus(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')

def index(request):
    return render(request,'index.html')


def operations(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    num = x,y
    add = x + y 
    mul = x * y
    div = x / y
    sub = x - y
    return render(request, 'result.html', {'addi': add, 'muli': mul, 'divi':div,'subi':sub,'numi':num})











