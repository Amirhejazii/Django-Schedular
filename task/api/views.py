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
        for i in all_task:
            
            if i.precondition_tasks.all().count() == 0:
                pass
            
            elif i.precondition_tasks.all().count() == 1:
                precondition_tasks = i.precondition_tasks.all().first()
                compare_result = self.compare_two_task(first_task = i,second_task = precondition_tasks)
                if compare_result:
                    return HttpResponse("ok")
                else:
                    #print("here")
                    return HttpResponse(f" this set of tasks is not possible beacuse of task with id {i.id} and the precondition_tasks with id {precondition_tasks.id}",status=404)
                
            
            elif i.precondition_tasks.all().count() >1:
                precondition_tasks = i.precondition_tasks.all()
                for j in precondition_tasks:
                    compare_result = self.compare_two_task(first_task = i,second_task=j)
                    if compare_result:
                        pass
                    else:
                        return HttpResponse(f"this set of tasks is not possible beacuse of task with id {i.id} and the precondition_task with id {j.id}",status=404)
                    
                return HttpResponse("True")