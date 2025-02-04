from django import forms

class ContactForm(forms.Form):
    title = forms.CharField(max_length=255)
    # email = forms.EmailField()
    # message = forms.CharField(widget=forms.Textarea)