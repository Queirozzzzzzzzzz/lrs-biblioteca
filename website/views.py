from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages

def home(request):
    all_members = Member.objects.all
    return render(request, 'home.html', {'all':all_members})

def join(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            name = request.POST['name']
            email = request.POST['email']
            number = request.POST['number']
            occupation = request.POST['occupation']
            passwd = request.POST['passwd']

            messages.success(request, ('Houve um erro no seu formulário'))
            return render(request, 'join.html', {
                    'name': name,
                    'email': email,
                    'number': number,
                    'occupation': occupation,
                    'passwd': passwd,
                })
        messages.success(request, ('Seu formulário foi enviado'))
        return redirect('home')

    else:
        return render(request, 'join.html', {})