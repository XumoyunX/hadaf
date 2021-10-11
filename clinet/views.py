from django.shortcuts import render
from .forms import GalleryForm, UsersForm, TeachersForm, NewsForm, CoursesForm
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from main.models import Courses, Users,Teachers, News, Gallery




def login_required_decorator(f):
    return login_required(f, login_url="login")

@login_required_decorator
def dashboard(request):
    return render(request, 'dashboard/index.html')

def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/login.html')

@login_required_decorator
def dashboard_logout(request):
    logout(request)
    return redirect('logout')




@login_required_decorator
def category_list(request):
    categories = Courses.objects.all()
    ctx = {
        'categories':categories,
        "c_active": 'active'
    }
    return render(request,'dashboard/categories/list.html',ctx)

@login_required_decorator
def category_create(request):
    model = Courses()
    form = CoursesForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/categories/form.html', ctx)

@login_required_decorator
def category_edit(request, pk):
    model = Courses.objects.get(id=pk)
    form = CoursesForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('category_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/categories/form.html', ctx)

@login_required_decorator
def category_delete(request, pk):
    model = Courses.objects.get(id=pk)
    model.delete()
    return redirect('category_list')



@login_required_decorator
def galer_list(request):
    galer = Gallery.objects.all()
    ctx = {
        'galer':galer,
        "g_active": 'active'
    }
    return render(request,'dashboard/kontak/list.html',ctx)

@login_required_decorator
def galer_create(request):
    model = Gallery()
    form = GalleryForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('galer_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/kontak/form.html', ctx)

@login_required_decorator
def galer_edit(request, pk):
    model = Gallery.objects.get(id=pk)
    form = GalleryForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('galer_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/kontak/form.html', ctx)

@login_required_decorator
def galer_delete(request, pk):
    model = Gallery.objects.get(id=pk)
    model.delete()
    return redirect('galer_list')



@login_required_decorator
def product_list(request):
    pro = Teachers.objects.all()
    ctx = {
        'pro':pro,
        "p_active": 'active'
    }
    return render(request,'dashboard/products/list.html',ctx)

@login_required_decorator
def product_create(request):
    model = Teachers()
    form = TeachersForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/products/form.html', ctx)

@login_required_decorator
def product_edit(request, pk):
    model = Teachers.objects.get(id=pk)
    form = TeachersForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('product_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/products/form.html', ctx)

@login_required_decorator
def product_delete(request, pk):
    model = Teachers.objects.get(id=pk)
    model.delete()
    return redirect('product_list')



@login_required_decorator
def new_list(request):
    new = News.objects.all()
    ctx = {
        'new': new,
        "n_active": 'active'
    }
    return render(request,'dashboard/New/list.html',ctx)

@login_required_decorator
def new_create(request):
    model = News()
    form = NewsForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('new_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/New/form.html', ctx)

@login_required_decorator
def new_edit(request, pk):
    model = News.objects.get(id=pk)
    form = NewsForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('new_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/New/form.html', ctx)

@login_required_decorator
def new_delete(request, pk):
    model = News.objects.get(id=pk)
    model.delete()
    return redirect('new_list')



@login_required_decorator
def user_list(request):
    ser = Users.objects.all()
    ctx = {
        'ser': ser,
        "s_active": 'active'
    }
    return render(request,'dashboard/user/list.html',ctx)

@login_required_decorator
def user_create(request):
    model = Users()
    form = UsersForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('user_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/user/form.html', ctx)

@login_required_decorator
def user_edit(request, pk):
    model = Users.objects.get(id=pk)
    form = UsersForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('user_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/user/form.html', ctx)

@login_required_decorator
def user_delete(request, pk):
    model = Users.objects.get(id=pk)
    model.delete()
    return redirect('user_list')



