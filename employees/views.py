from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
from .forms import EmployeeForm

# Create your views here.

# Update Employees View.
def employees_update(request):
    data = {}
    if request.is_ajax() and request.method == 'POST':

        # get the data send from the Browser.
        get_id = request.POST.get('id')
        get_first_name = request.POST.get('first_name')
        get_last_name = request.POST.get('last_name')

        # get the Employee have the same info.
        get_employee = Employee.objects.get(id=get_id)

        # if found the employee.
        if get_employee:

            # change the first_name of ths employee.
            get_employee.first_name = get_first_name

            # change the last_name of this employee.
            get_employee.last_name = get_last_name

            # save the change.
            get_employee.save()

            # set the response inside a dictionry
            data['update_success'] = 'Employee has been update his info'

            # send the response to the Browser
            return JsonResponse(data)

        # if not found the employee
        else:

            # set the response inside a dictionry
            data['update_error'] = 'Employee info not update'

            # send the response to the Browser
            return JsonResponse(data)
  
        



# function to get the employee info.
def get_employee_info(request):
    data = {}
    if request.is_ajax() and request.method == 'POST':
        
        # get the id it was send by the Browser using ajax.
        get_id = int(request.POST.get('id'))

        # get the Employee have The same ID.
        get_employee = Employee.objects.get(id=get_id)

        # if found the Employee
        if get_employee:
            # set the response inside a dictionry
            data['id'] = get_employee.id
            data['first_name'] = get_employee.first_name
            data['last_name'] = get_employee.last_name

            # send the response to the Browser.
            return JsonResponse(data)





# Remove Employees View.
def employees_delete(request):
    data = {}
    if request.is_ajax() and request.method == 'POST':

        get_id = int(request.POST.get('id'))
        getEmployee = Employee.objects.get(id=get_id)

        # if Employee is Found.
        if getEmployee:

            # delete the employee was found.
            getEmployee.delete()

            # set the response inside a dictionry
            data['delete_success'] = 'Employee has Been deleted'

            # send the response to the Browser.
            return JsonResponse(data)

        # if the Employee not found.
        else:

            # set the response inside a dictionry
            data['delete_employee_error'] = 'Employee not deleted try again'

            # send the response to the Browser.
            return JsonResponse(data)





# Employees List View.
def employees_list(request):
    form = EmployeeForm()
    data = {}
    # get all employee in database.
    employees = Employee.objects.all()

    if request.is_ajax() and request.method == 'POST':
        # put the request inside form.
        form = EmployeeForm(request.POST)

        # find the Employee.
        getEmployee = Employee.objects.filter(first_name=request.POST['first_name'], last_name=request.POST['last_name']).exists()

        # if the form is valid.
        if form.is_valid():

            # if the employee is found.
            if not getEmployee:
                
                # save the form.
                form.save()
                # set the response inside a dictionry
                data['success'] = 'Employee Has Been Add'

                # send the response to the Browser.
                return JsonResponse(data)
            else:
                # set the response inside a dictionry
                data['error'] = 'Employee already exists'

                # send the response to the Browser.
                return JsonResponse(data)
        else:
            # set the response inside a dictionry
            data['error'] = 'Oops! someThing Is Wrong, Try again'

            # send the response to the Browser.
            return JsonResponse(data)

    # The context.
    context = {
        'form': form,
        'developer': 'Mohammed ELkhamlichi',
        'employees': employees,
    }
    return render(request, 'employees/employees_list.html', context)