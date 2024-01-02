# forms.py
from django import forms
from .models import TableReservation

class TableReservationForm(forms.ModelForm):
    class Meta:
        model = TableReservation
        fields = ['name', 'number_of_guests', 'reservation_date', 'reservation_time', 'contact_number']
