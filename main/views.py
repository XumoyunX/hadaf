from django.shortcuts import render,redirect

from main.models import Gallery, News, Teachers, Courses, Users
from .forms import UsersFrom

# def user_reg(request):
#     model = Users()
#     form = UsersFrom(request.POST, instance=model)
#     print(request.POST)
#     if form.is_valid():
#         print("aaa")
#         form.save()
#     ctx = {
#         "form": form,
#
#     }
#     return render(request, "main/index.html", ctx)




def main(request):
    gle = Gallery.objects.all()
    cre = Courses.objects.all()
    tec = Teachers.objects.all()
    new = News.objects.all()
    org = Users.objects.all()
    model = Users()
    form = UsersFrom(request.POST,instance=model)
    if form.is_valid():
        form.save()
        return redirect('self')

    txs = {
        "gle": gle,
        "cre": cre,
        "tec": tec,
        "new": new,
        "form": form,
        "orgs": org
    }

    return render(request, "main/index.html", txs)




