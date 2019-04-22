from django.shortcuts import render
from listproperty.forms import PropertyForm


def PropertyView(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'listproperty.html', {'form':form} )
    else:
        form = PropertyForm()
        return render(request, 'listproperty.html', {'form':form})

