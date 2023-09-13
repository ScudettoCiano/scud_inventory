from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Scud',
        # 'class': 'PBP E',
        'amount' : "12",
        'description1' : "Increases DMG dealt by characters' Techniques by 200%. Technique DMG further increases by 200% of the Technique's respective character's Max HP.",
        'description2' : "structible objects will appear more frequently and rewards obtained from the are doubled.",
        'description3' : "You will obtain 10 Cosmic Fragments for each ally whose HP is at max when winning a battle.",

        
    }

    return render(request, "templates.html", context)