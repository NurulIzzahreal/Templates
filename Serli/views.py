from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import TableReservationForm

def Serli(request):
  template = loader.get_template('artika.html')
  return HttpResponse(template.render())

def reserve_table(request):
    if request.method == 'POST':
        form = TableReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')  # Ganti dengan nama URL yang sesuai
    else:
        form = TableReservationForm()
    return render(request, 'reserve_table.html', {'form': form})