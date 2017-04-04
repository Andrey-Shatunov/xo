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
    return render(request, 'xo/index.html',{'room': rooms})

def check_full_room(request, room_id):
    #check_full_room(request.user, room_id)
    #print("check_full_room")
    #room=Room.objects.filter(pk=room_id)
    #room = Room.objects.get(pk=room_id)
    #print(room)
    #print(room.user_one)
    if request.user.is_authenticated():
        room = Room.objects.get(pk=room_id)
        user = User.objects.all()
        if str(room.user_one)=="0":
            room.user_one=str(request.user)
            room.save()
        elif str(room.user_two)=="0":
            if str(room.user_one)==str(request.user):
                return HttpResponse("You are in the room")
            else:
                room.user_two = str(request.user)
                room.save()
        else:
            if str(room.user_one) == str(request.user):
                return HttpResponse("You are in the room")
            elif str(room.user_two) == str(request.user):
                return HttpResponse("You are in the room")
            else:
                return HttpResponse("room is full")

        print(user[2].username)
        return HttpResponse(room.room_name+str(room.user_one)+str(room.user_two))
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
            # print("Kol-vo shagov")
            # print(len(list(Steps.objects.filter(room=room))))
            # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
            if not Steps.objects.filter(room=room, x=request.GET.__getitem__("id")):
                if (len(list(Steps.objects.filter(room=room)))) % 2 == 0:
                    #print((len(list(Steps.objects.filter(room=room)))))
                    #print("len")
                    if (len(list(Steps.objects.filter(room=room))))  == 0:
                        #print(Steps.objects.filter(room=room, player=request.user).distinct().values_list('player','type'))
                        p = Steps(room=room, player=request.user, x=request.GET.__getitem__("id"), y=0, type=1)
                        p.save()
                        return 1
                    else:
                        #print(Steps.objects.filter(room=room, player=request.user).distinct().values_list('player','type'))
                        steps_x = Steps.objects.filter(room=room,type=1).distinct().values_list('player')
                        #print(steps_x)
                        #print("krestik")
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
                        #print(steps_x[0][1])
                        #print(request.user)
                        if str(steps_x[0][0])!=str(request.user):
                            p = Steps(room=room, player=request.user, x=request.GET.__getitem__("id"), y=0, type=0)
                            p.save()
                        return 1
                    # room = get_object_or_404(Room, pk=room_id)
                    # room = Room.objects.filter(id=room_id)
                    else:
                        steps_x = Steps.objects.filter(room=room,type=0).distinct().values_list('player')
                        #print(steps_x)
                        #print("nolik")
                        if str(steps_x[0][0]) == str(request.user):
                            p = Steps(room=room, player=request.user, x=request.GET.__getitem__("id"), y=0, type=0)
                            p.save()
                        return 1
                    # room = Room.objects.filter()
    return 0
                    # for i in room:
                    #  print(i.room_name)
                    # print(i.user_one)
                    # print(room.user_one)

def xo(request,room_id):
    if request.user.is_authenticated():
        #check_full_room(request.user, room_id)
        #print(request)
        room = get_object_or_404(Room, pk=room_id)
        if ckeck_steps(request,room_id,room) ==1:
           return redirect("/xo/xo/" + room_id)
        #redirect("/xo/xo/" + room_id)
       #return(ckeck_steps(request,room_id,room))
        steps = Steps.objects.filter(room=room)
        entry_list = list(steps)
        my_list = [2 for i in range(9)]
        for i in steps:
            my_list[i.x] = i.type
        # context = {'my_steps0': my_list,'my_steps': my_list[0:3],'my_steps1': my_list[3:6],'my_steps2': my_list[6:9]}
        statistic=Statistics.objects.filter(player=request.user).values_list('player','win','loose')
        print(statistic)
        context = {'my_steps0': my_list,'player':statistic[0][0],'win':statistic[0][1],'loose':statistic[0][2]}
        return render(request, 'xo/my.html', context)
    else:
        return redirect("/loginsys/")

def add_win(request,room_id):
    if request.user.is_authenticated():
        #print("111add_win")
        #print(request.user.username)
        #print(room_id)
        room = get_object_or_404(Room, pk=room_id)
        x = request.GET.__getitem__("type")
        steps_x = Steps.objects.filter(room=room,type=x).distinct().values_list('player', 'type')
        print(str(x)+"x")
        print(str(steps_x)+"steps_x")
        if str(request.user.username)==str(steps_x[0][0]):
            username = request.user.username
            print("user_info")
            #print(user_info)
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
                #print(user_info)
                user_info.loose = user_info.loose + 1
                user_info.save()
            except ObjectDoesNotExist:
                print("iskl")
                p = Statistics(player=request.user,loose=1)
                p.save()

        return HttpResponse("olo")