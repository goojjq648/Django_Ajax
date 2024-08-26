from django.shortcuts import render

# Create your views here.


def show_register(request):
    return render(request, 'member/register.html', {'title': 'Register page'})
