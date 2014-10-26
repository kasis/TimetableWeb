from django import forms

class AddEventForm(forms.Form):
    name = forms.CharField(max_length=100)
    place = forms.CharField(max_length=100)
    date = forms.DateField()
    note = forms.CharField(widget=forms.Textarea)
    time_start = forms.DateTimeField()
    time_end = forms.DateTimeField()
