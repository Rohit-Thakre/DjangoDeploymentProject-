from django.shortcuts import render
from django.views import View
from sub_app import models
from sub_app import forms 

# Create your views here.
class HomeView(View):
    def get(self, request):
        images = models.Images.objects.all()
        return render(request, 'home.html', {'images': images})
    
    
    
class ImageView(View):
    def get(self, request):
        return render(request, 'sub_app/image_upload_form.html', {'form': forms.ImageForm()})
    
    def post(self, request):
        form = forms.ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'sub_app/image_upload_form.html', {'form': forms.ImageForm()})
        return render(request, 'sub_app/image_upload_form.html', {'form': form})
    