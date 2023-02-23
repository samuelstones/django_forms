from django.shortcuts import render

from . forms import UserReg

from.forms import PeopleReg

from.forms import StudentsReg



def reg(request):
    submit_button = request.POST.get("stones")
    name = ''
    email = ''
    password = ''

    rForm = UserReg(request.POST or None)
    if rForm.is_valid():
        name = rForm.cleaned_data.get("name")
        email = rForm.cleaned_data.get("email")
        password = rForm.cleaned_data.get("password")

    context = {'rForm': rForm, 'name': name, 'email':email, 'submit_button':submit_button }

    return render(request, 'register.html', context)


def reg_people(request):
    submit_people_button =request.POST.get("peoplebtn")
    name = ''
    age = ''
    phone = ''
    city = ''

    people_form = PeopleReg(request.POST or None)
    if people_form.is_valid():
        name = people_form.cleaned_data.get("name")
        age = people_form.cleaned_data.get("age")
        phone = people_form.cleaned_data.get("phone")
        city = people_form.cleaned_data.get("city")


    context = {'people_form': people_form,
                'name': name,
                'age': age,
                'phone': phone,
                'city': city,
                'submit_people_button': submit_people_button

                }
    return render(request, 'people.html', context)

def reg_students(request):
    submit_students_button = request.POST.get("studentsbtnbtn")
    name = ''
    gender = ''
    school = ''
    parent = ''
    phone = ''

    students_form = StudentsReg(request.POST or None)
    if students_form.is_valid():
        name = students_form.cleaned_data.get("name")
        gender = students_form.cleaned_data.get("gender")
        school = students_form.cleaned_data.get("school")
        parent = students_form.cleaned_data.get("parent")
        phone = students_form.cleaned_data.get("phone")

    context = {'students_form': students_form,
               'name': name,
               'gender': gender,
               'school': school,
               'parent': parent,
               'phone': phone,
               'submit_students_button': submit_students_button

               }
    return render(request, 'students.html', context)


