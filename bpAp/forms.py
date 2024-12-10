from django import forms
from .models import ContestSubmission

class ContestSubmissionForm(forms.ModelForm):
    class Meta:
        model = ContestSubmission
        fields = ['name', 'email', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
