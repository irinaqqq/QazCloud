from django import forms
from .models import Post


class UploadForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['file', ]

        widgets = {
            'file': forms.FileInput(attrs={'class': 'mt-3 border-0'}),
        }