from django.shortcuts import render
from django.views import View
from .utils import flames

class IndexView(View):
    def get(self,request):
        return render(request,'myapp/index.html')
    
    def post(self,request):
        name1 = request.POST.get('name1')
        name2 = request.POST.get('name2')
        result = flames(name1,name2)
        return render(request,'myapp/index.html',{'result':result})
