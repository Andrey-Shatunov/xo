from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404,render,redirect
from django.http import Http404
from .models import Steps,Room

def index(request):
    style=r' style="font:46pt Arial, Helvetica, sans-serif; width:100px;height:100px" '
    s=r'http://127.0.0.1:8000/xo/xo/'
    rooms = Room.objects.all()
    for i in rooms:
        print(i.id)
    #return HttpResponse("Hello. Use <p><a href="+s+">This</a></p>")
    return render(request, 'xo/index.html',{'room': rooms})

def check_full_room(request_user, room_id):
    print("check_full_room")
    Room.object.filter(pk=room_id)

def xo(request,room_id):
    check_full_room(request.user,room_id)
    if request.user.is_authenticated():
        #print(request.user)
        room = get_object_or_404(Room, pk=room_id)
        if len(request.GET) > 0:
            if request.GET.__getitem__("id") == "NewGame":
                print("NewGame")
                steps = Steps.objects.filter(room=room)
                steps.delete()
            else:
                #print("Kol-vo shagov")
                #print(len(list(Steps.objects.filter(room=room))))
                if not Steps.objects.filter(room=room, x=request.GET.__getitem__("id")):
                    if (len(list(Steps.objects.filter(room=room)))) % 2 == 0:
                        # room = get_object_or_404(Room, pk=room_id)
                        # room=Room.objects.filter(id=room_id)
                        # print(room.id)
                        p = Steps(room=room,player=request.user, x=request.GET.__getitem__("id"), y=0, type=1)
                        p.save()
                    elif (len(list(Steps.objects.filter(room=room)))) % 2 == 1:
                        # room = get_object_or_404(Room, pk=room_id)
                        # room = Room.objects.filter(id=room_id)
                        p = Steps(room=room,player=request.user, x=request.GET.__getitem__("id"), y=0, type=0)
                        p.save()

                        # room = Room.objects.filter()

                        # for i in room:
                        #  print(i.room_name)
                        # print(i.user_one)
        print(room.user_one)

        steps = Steps.objects.filter(room=room)
        entry_list = list(steps)
        my_list = [2 for i in range(9)]
        for i in steps:
            my_list[i.x] = i.type
        # context = {'my_steps0': my_list,'my_steps': my_list[0:3],'my_steps1': my_list[3:6],'my_steps2': my_list[6:9]}
        context = {'my_steps0': my_list}
        return render(request, 'xo/my.html', context)
    else:
        return redirect("/loginsys/")

def add_win(request):
    if request.user.is_authenticated():
        print("111add_win")
        print(request.user.username)
        username = request.user.username
        user_info=Statistics.objects.get(player=username)
        user_info.win = F('win') + 1
        user_info.save()
        return HttpResponse("olo")