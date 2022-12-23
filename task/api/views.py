from task.models import Task
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from user.models import User
from django.http import HttpResponse


class CheckTasks(APIView):
    """
        This api checks all tasks to see if they can possible or not
    """
    def compare_two_task(self,first_task,second_task):
        if first_task.time_to_send < second_task.time_to_send:
            return True
        else:
            return False
        
        
    def get(self,request):
        all_task = Task.objects.all()
        task_true = 0
        task_false = 0 
        for i in all_task:
            if i.precondition_tasks.all().count() == 0:
                task_true+=1
                continue
            
            precondition_task = i.precondition_tasks.all()
            
            if precondition_task.count() == 1 :
                pre_task = precondition_task.first()
                if pre_task.time_to_send >= i.time_to_send:
                    return HttpResponse(f"THERE IS PROBLEM IN TASK WITH ID {i.id} AND TITLE {i.title}",status = 404 )
                else:
                    continue
                
            elif precondition_task.count() >1 :
                for pre_task in precondition_task:
                    if pre_task.time_to_send >= i.time_to_send:
                        return HttpResponse(f"THERE IS PROBLEM IN TASK WITH ID {i.id}",status = 404 )
                    else:
                        continue
                    
        return HttpResponse(" ALL THE TASKS ARE OK ",status = 200)
                