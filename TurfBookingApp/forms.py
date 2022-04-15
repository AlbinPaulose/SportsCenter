from django import forms
from .models import *


class TurfReviewForm(forms.ModelForm):
    class Meta:
        model = TurfReview
        fields = ['user', 'rating', 'feedback', 'image']
