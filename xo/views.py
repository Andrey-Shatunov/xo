from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404,render
from django.http import Http404
from .models import Steps

def index(request):
    style=r' style="font:46pt Arial, Helvetica, sans-serif; width:100px;height:100px" '
    s=r'http://127.0.0.1:8000/xo/xo/'
    return HttpResponse("Hello. Use <p><a href="+s+">This</a></p>")

def xo(request):
    if len(request.GET) > 0:
        if request.GET.__getitem__("id")=="NewGame":
            print("NewGame")
            steps = Steps.objects.all()
            steps.delete()
        else:
            if not Steps.objects.filter(x=request.GET.__getitem__("id")):
                if(len(list(Steps.objects.all()))%2==0):
                    p=Steps(x=request.GET.__getitem__("id"),y=0,type=1)
                    p.save()
                elif(len(list(Steps.objects.all()))%2==1):
                    p=Steps(x=request.GET.__getitem__("id"),y=0,type=0)
                    p.save()
            
    steps = Steps.objects.all()
    entry_list = list(steps)
    my_list=[2 for i in range(9)]
    for i in steps:
        my_list[i.x]=i.type
    #context = {'my_steps0': my_list,'my_steps': my_list[0:3],'my_steps1': my_list[3:6],'my_steps2': my_list[6:9]}
    context = {'my_steps0': my_list}
    return render(request, 'xo/my.html',context)
