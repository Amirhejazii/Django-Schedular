from django.test import TestCase
from .models import Task
from django.contrib.auth.models import Group
import datetime
from django.utils import timezone

from user.models import User
class TestApi(TestCase):
    def setUp(self):
        now = timezone.now()
        admin_group = Group.objects.get_or_create(name = 'admin')
        user1 = User.objects.create(first_name = 'test',last_name='test',email = 'hejaziamirmohammad5@gmail.com')
        user1.groups.set(admin_group)
        task1 = Task.objects.create(title = "task1",description = "task2",owner=user1,time_to_send=now)
        task2 = Task.objects.create(title="task2",description = "task2",owner=user1,time_to_send=now+datetime.timedelta(seconds = 120))
        task2.precondition_tasks.add(task1)
        
        
    def test_api_return_true(self):
        response = self.client.get('/task/api/check/')
        content = str(response.content)
        self.assertEquals(content,"b' ALL THE TASKS ARE OK '")
        self.assertEquals(response.status_code,200)
        
    def test_api_return_false(self):
        now = timezone.now()
        user1= User.objects.get(id=1)
        task2 = Task.objects.get(title="task2")
        task3 = Task.objects.create(title="task3",description="task3",owner=user1,time_to_send=now+datetime.timedelta(seconds=80))
        task3.precondition_tasks.add(task2)
        response = self.client.get('/task/api/check/')
        content = str(response.content)
        self.assertEquals(content,"b'THERE IS PROBLEM IN TASK WITH ID 3 AND TITLE task3'")
        self.assertEquals(response.status_code,404)
