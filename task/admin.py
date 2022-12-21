from django.contrib import admin
from .models import Task
from django.contrib.auth.models import Group,Permission
from django.contrib.auth.models import User



normal_group = Group.objects.get(name='normal')
admin_group = Group.objects.get(name='admin')


add_task = Permission.objects.get(name='Can add task')
change_task = Permission.objects.get(name='Can change task')
delete_task =  Permission.objects.get(name='Can delete task')
view_task = Permission.objects.get(name='Can view task')
add_user = Permission.objects.get(name='Can add user')
change_user = Permission.objects.get(name='Can change user')
delete_user = Permission.objects.get(name='Can delete user')
view_user = Permission.objects.get(name='Can view user')


admin_group.permissions.add(add_task)
admin_group.permissions.add(change_task)
admin_group.permissions.add(delete_task)
admin_group.permissions.add(add_user)
admin_group.permissions.add(change_user)
admin_group.permissions.add(delete_user)
admin_group.permissions.add(view_user)

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'time_to_send')
    ordering = ('time_to_send', 'title')
    search_fields = ('title', 'description', 'owner')
    list_filter = ('owner', 'time_to_send')
    # allow usser just access to his/her own objects
    def get_queryset(self, request):
        qs = super(TodoAdmin, self).get_queryset(request)
        if request.user.groups.filter(name='admin'):
            return qs
        return qs.filter(owner=request.user)

    def has_add_permission(self,request):
        return True

    def has_change_permission(self,request,obj=None):
        return True

    def has_view_permission(self,request,obj=None):
        return True

    def has_module_permission(self,request,obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    # dont allow current_user to create object for another 
    
    #exclude = ('owner',)
    def get_form(self, request, obj=None, **kwargs):
        print(request.user.groups.filter(name="admin"))
        self.exclude = []
        if not request.user.groups.filter(name="admin"):
            self.exclude.append('owner') #here!
        return super(TodoAdmin, self).get_form(request, obj, **kwargs)
    
    def save_model( self, request, obj, form, change ):
        obj.save()

    

admin.site.register(Task,TodoAdmin)