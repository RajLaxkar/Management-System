from django.shortcuts import render ,HttpResponse ,redirect
from .models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,('index.html'))

def view_employee(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    
    return render(request,'view.html',context)

def add_employee(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp =Employee(first_name = first_name , last_name = last_name , salary = salary, bonus = bonus , phone = phone, dept_id = dept, role_id = role , hire_date = datetime.now() )
        new_emp.save()
        return redirect("view_employee")
    elif request.method == "GET":
        return render(request,'add.html')
    else:
        return HttpResponse("An exception occured ! not added") 

def remove_employee(request, emp_id = 0):       # emp_id: An optional parameter (default is 0). If provided, it identifies the employee to be deleted.
    if emp_id:                                  # If emp_id is greater than 0, it means the user wants to remove a specific employee.
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return redirect("view_employee")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove.html',context)


def filter_employee(request):  
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name : 
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role: 
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps' : emps
        }
        return render(request,'view.html',context)
    elif request.method == 'GET':
        return render(request,'filter.html')
    else:
        return HttpResponse("An Exeption Occured")





# "POST" is used when submitting form data to the server (e.g., adding an employee).
# "GET" is used when simply requesting a page from the server (e.g., opening the Add Employee form).
# If the request method is "GET", it means the user is opening the Add Employee page but has not submitted the form yet.
# The render(request, 'add.html') function loads and displays the add.html template (which is likely your employee registration form).

# How It Works in a Web App?
# User visits the URL linked to add_employee view (e.g., /add-employee/).
# Since no form is submitted yet, request.method is "GET".
# The server responds by rendering the add.html template, which likely contains a form where the user can enter employee details.
# Once the user fills out the form and clicks "Submit", the form sends a "POST" request with the entered data.
# Now, the "POST" section of the function executes, adding the new employee to the database.
