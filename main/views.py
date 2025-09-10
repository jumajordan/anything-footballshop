from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'first' : 'What Do You Want to Buy?',
        'shop': 'Enter the shop',
        'desc': 'In this shop you will find everything about football',
        'aboutme': 'Juma Jordan Bimo, 2406435843'
    }

    return render(request, "main.html", context)