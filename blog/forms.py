from django import forms
from .models import ResumeSubmission

class ResumeSubmissionForm(forms.ModelForm):
    class Meta:
        model = ResumeSubmission
        fields = ['name', 'email', 'resume']