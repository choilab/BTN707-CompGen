'''
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
import os
# Create your views here.

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        flist = request.FILES.getlist('file')
        for f in flist:
            tmp = open(os.path.join(os.getcwd(),'media',f.name),'wb+')
            for chunk in f.chunks():
                tmp.write(chunk)
        return HttpResponse("file upload complete")
    else:
        form = UploadFileForm()
    return render(request, 'administration/upload.html',{'form' : form})
'''


from django.shortcuts import render, redirect
import os
from .forms import UploadFileForm
from django.http import HttpResponse

def handle_uploaded_file(f):
    with open(os.path.join(os.getcwd(),"media", f.name),'w+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# Create your views here.
def upload_file(request):
    form = UploadFileForm()
    if request.method == 'POST':
        print(os.getcwd())
        print("POST method")
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print("Valid")
            for x in request.FILES.getlist("file"):
                os.system('touch %s/%s' %(os.path.join(os.getcwd(),"media"),x))
                def handle_uploaded_file(f):
                    with open(os.path.join(os.getcwd(),"media", f.name),'wb+') as destination:
                        for chunk in f.chunks():
                            destination.write(chunk)
                print(x)
                handle_uploaded_file(x)
            context = {'form':form,}
            #return render(request, 'administration/upload.html', context)
            return HttpResponse(" File uploaded! ")
    else:
        form = UploadFileForm()

    return render(request, 'administration/upload.html', {'form': form})
