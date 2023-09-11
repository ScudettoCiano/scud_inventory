from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Scud',
        'class': 'PBP E',
        'amount' : "12",
    }

    return render(request, "templates.html", context)