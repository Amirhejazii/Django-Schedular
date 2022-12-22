from task.models import Task
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from user.models import User
from django.http import HttpResponse

@api_view(['GET'])
def check_tasks(request):
    all_task = Task.objects.all().order_by('id')
    for i in all_task:
        all_pre = i.precondition_tasks.all().values('id')
        if all_pre.count()== 0 :
            return HttpResponse("ok")
        if all_pre.count == 1:
            obj = all_pre.first()
            if obj>i.id:
                return HttpResponse("fasle")
            else:
                return HttpResponse("ok")
            
        if all_pre.count >1 :
            for j in all_pre:
                if j >i.id:
                    return HttpResponse("FALSE")
                else:
                    pass
            return HttpResponse("ok")
            
    