from django.shortcuts import render
from . forms import EmployeeForm
from . forms import StudentForm

# Create your views here.
def employee_form(request):
    form = EmployeeForm()
    return render(request,'employee_form.html',{'form':form})
def employee_list(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form= StudentForm
    return render(request,'employee_list.html',{'form':form})