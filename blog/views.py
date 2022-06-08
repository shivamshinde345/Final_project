from django.shortcuts import render
from . models import Post, crudst,crudst1
from . forms import stform,stform1
from django.contrib import messages
from django.http import JsonResponse

# import request

from django.views.decorators.csrf import csrf_exempt
from django.http import StreamingHttpResponse




import json
def graph(request):
      # return render(request,'index.html') 
     context = {
       'data_b'   : [12, 3, 4, 2, 12, 3,7,3,5,6,13,1],
       'data_c'   : [2, 9, 3, 17, 6, 3, 7,4,13,12,6,12]

                } 
     return render(request,'blog/graph.html',context)               
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/c.html')

# def landing(request):
#     # context = {
#     #     'posts': Post.objects.all()
#     # }
#     return render(request, 'blog/landing.html')


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def main(request):
    return render(request,'blog/c.html')

def contact(request):
    return render(request,'blog/contact.html')

@csrf_exempt
def service(request):
    global idx
    idx=request.GET.get('idx')
    print("hit",idx )
    return render(request,'blog/service.html')

def page1_1(request):
    return render(request,'blog/page1_1.html')


def page1_2(request):
    return render(request,'blog/page1_2.html') 

def page1_3(request):
    return render(request,'blog/page1_3.html')             

def service(request):
    return render(request,'blog/service.html')

def charts(request):
    return render(request,'blog/charts.html')    


def dashboard(request):
    return render(request,'blog/dashboard.html')

def index(request):
    return render(request,'blog/index.html')
# def index1(request):
#     return render(request,'blog/index1.html')    

def stdisplay(request):
    results=crudst.objects.all()
    return  render(request,'blog/disp.html',{"crudst":results})

def stinsert(request):
    if request.method=="POST":
        if request.POST.get('stname') and request.POST.get('stemail') and request.POST.get('staddress') and request.POST.get('stmobile') and request.POST.get('stgender'):
            savest=crudst()
            savest.stname=request.POST.get('stname')
            savest.stemail=request.POST.get('stemail')
            savest.staddress=request.POST.get('staddress')
            savest.stmobile=request.POST.get('stmobile')
            savest.stgender=request.POST.get('stgender')
            savest.save()
            messages.success(request,"The Record "+savest.stname+" is saved successfully")
            return render(request,"blog/create.html")
        else:
            return render(request,"blog/create.html")    
    else:
            return render(request,"blog/create.html")

def stedit(request,id):
    getstudentdetails=crudst.objects.get(id=id)
    return render(request,'blog/edit.html',{"crudst":getstudentdetails})

def stupdate(request,id):
    stupdate=crudst.objects.get(id=id)
    form=stform(request.POST,instance=stupdate)
    if form.is_valid():
        form.save()
        messages.success(request,"The member record is updated successfully")
        return render(request,"blog/edit.html",{"crudst":stupdate})
    
def stdel(request,id):
    delstudent=crudst.objects.get(id=id)
    delstudent.delete()
    results=crudst.objects.all()
    return  render(request,'blog/disp.html',{"crudst":results})

# from django.http import JsonResponse
# from .models import Students
  
def jsondata(request):
    data = list(crudst.objects.values())
    return JsonResponse(data,safe = False)
    



def stdisplay1(request):
    results1=crudst1.objects.all()
    return  render(request,'blog/disp1.html',{"crudst1":results1})

def stinsert1(request):
    if request.method=="POST":
        if request.POST.get('dname') and request.POST.get('dversion') and request.POST.get('nameofcustomer') and request.POST.get('customermobileno') and request.POST.get('dateofselling'):
            savest1=crudst1()
            savest1.dname=request.POST.get('dname')
            savest1.dversion=request.POST.get('dversion')
            savest1.nameofcustomer=request.POST.get('nameofcustomer')
            savest1.customermobileno=request.POST.get('customermobileno')
            savest1.dateofselling=request.POST.get('dateofselling')
            savest1.save()
            messages.success(request,"The Record "+savest1.dname+" is saved successfully")
            return render(request,"blog/create1.html")
        else:
            return render(request,"blog/create1.html")    
    else:
            return render(request,"blog/create1.html")

def stedit1(request,id):
    getstudentdetails1=crudst1.objects.get(id=id)
    return render(request,'blog/edit1.html',{"crudst":getstudentdetails1})

def stupdate1(request,id):
    stupdate1=crudst1.objects.get(id=id)
    form1=stform1(request.POST,instance=stupdate1)
    if form1.is_valid():
        form1.save()
        messages.success(request,"The member record is updated successfully")
        return render(request,"blog/edit1.html",{"crudst1":stupdate1})
    
def stdel1(request,id):
    delstudent1=crudst1.objects.get(id=id)
    delstudent1.delete()
    results1=crudst1.objects.all()
    return  render(request,'blog/disp1.html',{"crudst1":results1})
    

@csrf_exempt
def main_page(request):
    if request.method=="POST":
        global received_json_data
        data = request.body.decode('utf-8')
        received_json_data=json.loads(request.body)
        savest=Data()
        savest.id=received_json_data["MemberID"]
        savest.name=received_json_data['Name']
        savest.milktype=received_json_data['MilkType']
        savest.fat=received_json_data['Fat']
        savest.snf=received_json_data['SNF']
        savest.clr=received_json_data['CLR']
        savest.water=received_json_data['Water']
        savest.temp=received_json_data['Temp']
        savest.weight=received_json_data['Weight']
        savest.price=received_json_data['Price']
        savest.time=received_json_data['Time']
        savest.save()
        # print(fat)
            # messages.success(request,"The Record "+savest.stname+" is saved successfully")
        return render(request,"blog/data.html")
@csrf_exempt
def data(request):
    # results=data.objects.all()
    return  render(request,'blog/data.html')
    
        
        