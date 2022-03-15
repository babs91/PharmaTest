from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import CreateUserForm, ProfileForm, CustorderForm, entryForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import products, customers, adminEntry, customer_orders
from .filters import itmFilters, clnFilters, odrFilters
# Create your views here.


def registe(request):

    if request.user.is_authenticated:

        return redirect('Home1')

    frm = CreateUserForm()

    if request.method == 'POST':

        frm = CreateUserForm(request.POST)
        if frm.is_valid():
            user=frm.save()
            username = frm.cleaned_data.get('username')
            messages.success(request, "Account has been created for " + username)
            group = Group.objects.get(name='Customer')
            user.groups.add(group)
            customers.objects.create(user=user,)
            templates = loader.get_template("pharma_app/Logn.html")
            return HttpResponse(templates.render({}, request))

    else:
         dict = {'form':frm}
         templates = loader.get_template("pharma_app/signup.html")
         return HttpResponse(templates.render(dict, request))



def logpage(request):

    if request.user.is_authenticated:

        return redirect('Home1')

    else:

        if request.method == "POST":

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                login(request, user)
                templates = loader.get_template('pharma_app/Home.html')
                return HttpResponse(templates.render({}, request))

            else:
                messages.info(request,' Username or Password is incorrect')

        templates = loader.get_template('pharma_app/Logn.html')
        return HttpResponse(templates.render({}, request))


def Logout(request):

    logout(request)
    return redirect('loginp')

@login_required(login_url='loginp')
def Home(request):

    data = customers.objects.all()
    dict ={'obj':data}
    templates = loader.get_template('pharma_app/Home.html')
    return HttpResponse(templates.render(dict, request))

@login_required(login_url='loginp')
def administrator(request):

    templates = loader.get_template('pharma_app/Adminpage.html')
    return HttpResponse(templates.render({}, request))

@login_required(login_url='loginp')
def profile(request):


    pForm = ProfileForm(instance=request.user.customers)

    if request.method == 'POST':

        pForm = ProfileForm(request.POST, request.FILES, instance=request.user.customers)

        if pForm.is_valid():
            pForm.save()
            templates = loader.get_template('pharma_app/Home.html')
            return HttpResponse(templates.render({}, request))

    else:
         dict = {'form': pForm}
         templates = loader.get_template('pharma_app/profile.html')
         return HttpResponse(templates.render(dict, request))

@login_required(login_url='loginp')
def itempage(request):
    frm = CustorderForm()
    if request.method == 'POST':
        frm = CustorderForm(request.POST)
        if frm.is_valid():
            frm.save()
            templates = loader.get_template('pharma_app/Home.html')
            return HttpResponse(templates.render({}, request))

    else:
            data = products.objects.all()
            myFilters = itmFilters(request.GET, queryset=data)
            data = myFilters.qs
            dict = {'obj1': data, 'obj6':frm, 'myFilters': myFilters}
            templates = loader.get_template('pharma_app/sub_pro1.html')
            return HttpResponse(templates.render(dict, request))

@login_required(login_url='loginp')
def itempage2(request):

    frm = CustorderForm()
    if request.method == 'POST':
        frm = CustorderForm(request.POST)
        if frm.is_valid():
            frm.save()
            templates = loader.get_template('pharma_app/Home.html')
            return HttpResponse(templates.render({}, request))

    else:
            data = products.objects.all()
            data2 = data.filter(status='PharmaceuticalDrugs')
            myFilters = itmFilters(request.GET, queryset=data2)
            data2 = myFilters.qs
            dict = {'obj2': data2, 'obj6':frm, 'myFilters': myFilters}
            templates = loader.get_template('pharma_app/sub_pro2.html')
            return HttpResponse(templates.render(dict, request))

@login_required(login_url='loginp')
def itempage3(request):

    frm = CustorderForm()
    if request.method == 'POST':
        frm = CustorderForm(request.POST)
        if frm.is_valid():
            frm.save()
            templates = loader.get_template('pharma_app/Home.html')
            return HttpResponse(templates.render({}, request))

    data = products.objects.all()
    data3 = data.filter(status='Tradomedicals')
    myFilters = itmFilters(request.GET, queryset=data3)
    data3 = myFilters.qs
    dict = {'obj3': data3,'obj6':frm, 'myFilters': myFilters}
    templates = loader.get_template('pharma_app/sub_pro3.html')
    return HttpResponse(templates.render(dict, request))

@login_required(login_url='loginp')
def itempage4(request):

    frm = CustorderForm()
    if request.method == 'POST':
        frm = CustorderForm(request.POST)
        if frm.is_valid():
            frm.save()
            templates = loader.get_template('pharma_app/Home.html')
            return HttpResponse(templates.render({}, request))

    data = products.objects.all()
    data4 = data.filter(status='skincare')
    myFilters = itmFilters(request.GET, queryset=data4)
    data4 = myFilters.qs
    dict = {'obj4': data4,'obj6':frm, 'myFilters': myFilters}
    templates = loader.get_template('pharma_app/sub_pro4.html')
    return HttpResponse(templates.render(dict, request))

@login_required(login_url='loginp')
def admnEntry(request):

    frm = entryForm()
    if request.method == 'POST':
        frm = entryForm(request.POST)
        if frm.is_valid():
            frm.save()
            templates = loader.get_template('pharma_app/Home.html')
            return HttpResponse(templates.render({}, request))
    else:
         dict = {'obj6': frm}
         templates = loader.get_template('pharma_app/Entry.html')
         return HttpResponse(templates.render(dict, request))

@login_required(login_url='loginp')
def entries(request):

    data = customer_orders.objects.all()
    myFilters = odrFilters(request.GET, queryset=data)
    data = myFilters.qs
    dict = {'obj':data, 'myFilters':myFilters}
    templates = loader.get_template('pharma_app/new1.html')
    return HttpResponse(templates.render(dict, request))

@login_required(login_url='loginp')
def values(request):

    data = adminEntry.objects.all()
    myFilters = clnFilters(request.GET, queryset=data)
    data = myFilters.qs
    data2 = data.filter(status = 'Delivered').count
    data3 = data.filter(status = 'Out for delivery').count
    data4 = data.filter(status = 'Pending').count
    dict = {'obj': data, 'obj2': data2, 'obj3': data3, 'obj4': data4, 'myFilters': myFilters}
    templates = loader.get_template('pharma_app/new.html')
    return HttpResponse(templates.render(dict, request))

@login_required(login_url='loginp')
def Delete(request, id):

    data = adminEntry.objects.get(pk = id)

    if request.method == 'POST':
        data.delete()
        data = adminEntry.objects.all()
        dict = {'obj':data}
        templates = loader.get_template('pharma_app/new.html')
        return HttpResponse(templates.render(dict, request))

    else:
        dict = {'obj':data}
        templates = loader.get_template('pharma_app/confirm.html')
        return HttpResponse(templates.render(dict, request))

@login_required(login_url='loginp')
def Update(request, id):

    data = adminEntry.objects.get(pk = id)
    frm = entryForm(instance=data)
    if request.method == 'POST':
        frm = entryForm(request.POST, instance=data)
        if frm.is_valid():
            frm.save()
            return redirect('vlu')

    dict = {'obj6': frm}
    templates = loader.get_template('pharma_app/Entry.html')
    return HttpResponse(templates.render(dict, request))























