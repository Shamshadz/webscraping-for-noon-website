from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from jobData.models import State,Categorie,SubCategorie,JobDetail

# Create your views here.

class StateListView(ListView):
    template_name = "pages/home.html"
    queryset = State.objects.all()
    context_object_name = 'states'


class CategoreyView(View):

    def get(self,request,slug):
        
        state = State.objects.filter(slug=slug)
      
        queryset = Categorie.objects.filter()
        if queryset.exists():
            queryset = queryset
        else:
            print("queryset not found")

        context = {'categories':queryset,'state':state[0]}
        return render(request,"pages/categorey.html",context)



class SubCategoreyView(View):

    def get(self,request,state_slug,cat_slug):
        
        state = State.objects.filter(slug=state_slug)
        cat = Categorie.objects.filter(slug=cat_slug)
        
        queryset = SubCategorie.objects.filter(job_categorey=cat[0])
        if queryset.exists():
            queryset = queryset
        else:
            print("queryset not found")
        context = {'sub_categories':queryset,'state':state[0],'cat':cat[0]}
        return render(request,'pages/subcategorey.html',context)


class JobDetailView(View):

    def get(self,request,state_slug,sub_cat_slug):
        
        state = State.objects.filter(slug=state_slug)
        # cat = Categorie.objects.filter(slug=cat_slug)
        sub = SubCategorie.objects.filter(slug=sub_cat_slug)
        queryset = JobDetail.objects.filter(job_sub_categorey=sub[0])
        if queryset.exists():
            queryset = queryset
        else:
            print("queryset not found")
        
        
        context = {'jobs':queryset,'sub':sub[0],'state':state[0]}
        return render(request,'pages/jobs.html',context)


def search(request):

    query = request.GET['query']
    print(query)

    if len(query) <2 or len(query) > 50:
        query = []
    else:
        cat = Categorie.objects.filter(job_categorey__icontains=query)
        sub_cat = SubCategorie.objects.filter(job_sub_categorey__icontains=query)
        job = JobDetail.objects.filter(job_position__icontains=query)
        # job = job.union(sub_cat)

    if job.exists():
        job = job
    else:
        print("queryset not found")

    context = {'job':job,'cat':cat,'sub_cat':sub_cat,'query':query}
    return render(request,'pages/search.html',context)