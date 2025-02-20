# forms.py

from django import forms
from .models import Review,Comment
class ContactForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review', 'image']



