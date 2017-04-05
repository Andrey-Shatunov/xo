from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404,render,redirect
from django.http import Http404
from .models import Steps,Room,Statistics
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

def index(request):
    style=r' style="font:46pt Arial, Helvetica, sans-serif; width:100px;height:100px" '
    s=r'http://127.0.0.1:8000/xo/xo/'
    rooms = Room.objects.all()
    #for i in rooms:
        #print(i.id)
    #return HttpResponse("Hello. Use <p><a href="+s+">This</a></p>")
    rooms = Room.objects.all()
    for room in rooms:
        print(room.user_one)
        print(room.user_two)
        if str(request.user) == str(room.user_one):
            room.user_one = "0"
            room.save()
        elif str(request.user) == str(room.user_two):
            room.user_two = "0"
            room.save()

    return render(request, 'xo/index.html',{'room': rooms})

def check_full_room(request, room_id):
    #exit from room
    rooms=Room.objects.exclude(pk=room_id)
    for room in rooms:
        print(room.user_one)
        print(room.user_two)
        if str(request.user)==str(room.user_one):
            room.user_one="0"
            room.save()
        elif str(request.user)==str(room.user_two):
            room.user_two = "0"
            room.save()

    if request.user.is_authenticated():
        room = Room.objects.get(pk=room_id)
        user = User.objects.all()
        if str(room.user_one)=="0" and str(room.user_two)!=str(request.user):
            room.user_one=str(request.user)
            room.save()
        elif str(room.user_two)=="0":
            if str(room.user_one)==str(request.user):
                #return HttpResponse("You are in the room")
                return redirect("/xo/xo/" + room_id)
            else:
                room.user_two = str(request.user)
                room.save()
        else:
            if str(room.user_one) == str(request.user):
                #return HttpResponse("You are in the room")
                return redirect("/xo/xo/" + room_id)
            elif str(room.user_two) == str(request.user):
                #return HttpResponse("You are in the room")
                return redirect("/xo/xo/"+room_id)
            else:
                return HttpResponse("room is full")

        #return HttpResponse(room.room_name+str(room.user_one)+str(room.user_two))
        return redirect("/xo/xo/" + room_id)
    else:
        return redirect("/loginsys/")

def ckeck_steps(request,room_id,room):
    #room = get_object_or_404(Room, pk=room_id)
    if len(request.GET) > 0:
        if request.GET.__getitem__("id") == "NewGame":
            print("NewGame")
            steps = Steps.objects.filter(room=room)
            steps.delete()
            return 1
        else:
            # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
            if not Steps.objects.filter(room=room, x=request.GET.__getitem__("id")):
                if (len(list(Steps.objects.filter(room=room)))) % 2 == 0:
                    if (len(list(Steps.objects.filter(room=room))))  == 0:
                        p = Steps(room=room, player=request.user, x=request.GET.__getitem__("id"), y=0, type=1)
                        p.save()
                        return 1
                    else:
                        steps_x = Steps.objects.filter(room=room,type=1).distinct().values_list('player')
                        if str(steps_x[0][0]) == str(request.user):
                            p = Steps(room=room, player=request.user, x=request.GET.__getitem__("id"), y=0, type=1)
                            p.save()
                        return 1
                    # room = get_object_or_404(Room, pk=room_id)
                    # room=Room.objects.filter(id=room_id)
                    # print(room.id)

            # NULL NULL NULL NULL NULL
                elif (len(list(Steps.objects.filter(room=room)))) % 2 == 1:
                    if (len(list(Steps.objects.filter(room=room))))  == 1:
                        steps_x=Steps.objects.filter(room=room).distinct().values_list('player','type')
                        if str(steps_x[0][0])!=str(request.user):
                            p = Steps(room=room, player=request.user, x=request.GET.__getitem__("id"), y=0, type=0)
                            p.save()
                        return 1
                    else:
                        steps_x = Steps.objects.filter(room=room,type=0).distinct().values_list('player')
                        if str(steps_x[0][0]) == str(request.user):
                            p = Steps(room=room, player=request.user, x=request.GET.__getitem__("id"), y=0, type=0)
                            p.save()
                        return 1
    return 0

def xo(request,room_id):
    if request.user.is_authenticated():
        room = get_object_or_404(Room, pk=room_id)
        if ckeck_steps(request,room_id,room) ==1:
           return redirect("/xo/xo/" + room_id)
        steps = Steps.objects.filter(room=room)
        entry_list = list(steps)
        my_list = [2 for i in range(9)]
        for i in steps:
            my_list[i.x] = i.type
        statistic=Statistics.objects.filter(player=request.user).values_list('player','win','loose')
        room = Room.objects.filter(pk=room_id).values_list('user_one', 'user_two')
        context = {'my_steps0': my_list,'player':statistic[0][0],'win':statistic[0][1],'loose':statistic[0][2],'user_one':room[0][0],'user_two':room[0][1]}
        return render(request, 'xo/my.html', context)
    else:
        return redirect("/loginsys/")

def add_win(request,room_id):
    if request.user.is_authenticated():
        room = get_object_or_404(Room, pk=room_id)
        x = request.GET.__getitem__("type")
        steps_x = Steps.objects.filter(room=room,type=x).distinct().values_list('player', 'type')
        print(str(x)+"x")
        print(str(steps_x)+"steps_x")
        if str(request.user.username)==str(steps_x[0][0]):
            username = request.user.username
            print("user_info")
            try:
                user_info=Statistics.objects.get(player=username)
                user_info.win = user_info.win + 1
                user_info.save()
            except ObjectDoesNotExist:
                print("iskl")
                p = Statistics(player=request.user,win=1)
                p.save()

        else:
            username = request.user.username
            try:
                user_info = Statistics.objects.get(player=username)
                user_info.loose = user_info.loose + 1
                user_info.save()
            except ObjectDoesNotExist:
                print("iskl")
                p = Statistics(player=request.user,loose=1)
                p.save()

        return HttpResponse("olo")