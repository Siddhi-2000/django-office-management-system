from django.contrib import admin
#from .employee import Employee, Role, Department
from .models import Employee, Role, Department


# Register your models here.
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)
