from sub_app import models
from django import forms

class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Images
        fields = '__all__'