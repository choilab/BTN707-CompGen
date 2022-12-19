from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.urls import reverse
from .forms import UploadFileForm

from .models import handle_uploaded_file, running

x = ''
class uploading:
    def upload_file(request):
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            handle_uploaded_file(request.FILES['file'])
            if str(request.FILES['file'])[-3:] == "pdb" :
                x = request.FILES['file']
                running(x)
                return HttpResponse("success! wait for processing\n{}".format(x))
            else: 
                return HttpResponse("wrong format")
        else:
            form = UploadFileForm()
        return render(request, 'old.html', {'form':form})
        
# Create your views here.
