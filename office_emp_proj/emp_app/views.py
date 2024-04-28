from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404



# Create your views here.
def index(request):
    return render(request, 'index.html' )


def all_emp(request):
    emps = Employee.objects.all()
    context ={
        'emps': emps
    }
    print(context)
    return render(request, 'view_all_emp.html', context)


def emp_details(request, emp_id):
    emp = get_object_or_404(Employee, id=emp_id)
    context = {
        'emp': emp,
        'emps': Employee.objects.all()  # Pass the list of all employees as well
    }
    return render(request, 'view_all_emp.html', context)


# def add_emp(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['first_name']
#         salary = int(request.POST['first_name'])
#         bonus = int(request.POST['first_name'])
#         phone = int(request.POST['first_name'])
#         dept = int(request.POST['first_name'])
#         role = int(request.POST['first_name'])
#         new_emp= Employee(first_name= first_name, last_name= last_name, salary= salary, bonus=bonus, phone=phone, dept_id= dept, role_id= role, hire_date = datetime.now())
#         new_emp.save()
#         return HttpRespnse('Employee added Successfully')
#     elif request.method=='GET':
#         return render(request, 'add_emp.html')
#     else:
#         return HttpResponse("An Exception occured! Employee has not been added")

# def add_emp(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         salary = int(request.POST['salary'])
#         bonus = int(request.POST['bonus'])
#         phone = int(request.POST['phone'])
#         dept = int(request.POST['dept'])
#         role = int(request.POST['role'])
#         # Create and save the new employee object
#         new_emp = Employee(first_name= first_name, last_name= last_name, salary=salary, bonus=bonus, phone= phone, dept_id= dept, role_id= role, hire_date= datetime.now())
#         new_emp.save()
#         return HttpResponse('Employee added successfully') 
    
#     elif request.method == 'GET':
#         return render(request, 'add_emp.html')
#     else:
#         return HttpResponse("An Exception occurred! Employee has not been added")

def add_emp(request):
    if request.method == 'POST':
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            salary = int(request.POST['salary'])
            bonus = int(request.POST['bonus'])
            phone = int(request.POST['phone'])
            dept_id = int(request.POST['dept'])
            role_id = int(request.POST['role'])

            # Check if the department and role IDs exist
            if not Department.objects.filter(id=dept_id).exists() or not Role.objects.filter(id=role_id).exists():
                return HttpResponseBadRequest('Invalid department or role ID')

            # Create and save the new employee object
            new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id=dept_id, role_id=role_id, hire_date=datetime.now())
            new_emp.save()
            return HttpResponse('Employee added successfully')
        
        except ValueError:
            return HttpResponseBadRequest('Invalid data provided')

    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponseBadRequest("An Exception occurred! Employee has not been added")



def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee removed successfully")
        except:
            return HttpResponse("Please entered a valide Emp_id")
    emps = Employee.objects.all()
    context ={
        'emps':emps
    }
    return render(request, 'remove_emp.html', context)

from django.http import HttpResponseBadRequest


# def remove_emp(request, emp_id=0):
#     if emp_id:
#         try:
#             emp_to_be_removed = Employee.objects.get(id=emp_id)
#             emp_to_be_removed.delete()
#             return HttpResponse("Employee deleted successfully")
#         except Employee.DoesNotExist:
#             return HttpResponse("Please enter a valid Employee ID")
#     else:
#         return HttpResponseBadRequest("Employee ID is required")


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        dept = request.POST.get('dept', '')
        role = request.POST.get('role', '')

        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(firstname__icontains=name)) #| Q(lastname__icontains=name)
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)

        context = {
            'emps': emps,
            'name': name,
            'dept': dept,
            'role': role,
        }
        return render(request, 'view_all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')

    else:
        return HttpResponse('An Exception occurred')