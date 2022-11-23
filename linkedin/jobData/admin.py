from django.contrib import admin
from jobData.models import State,Categorie,SubCategorie,CompanyDetail,JobDetail

# Register your models here.
@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['state']
    
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['job_categorey']
    
@admin.register(SubCategorie)
class SubCategorieAdmin(admin.ModelAdmin):
    list_display = ['job_sub_categorey','job_categorey']

@admin.register(CompanyDetail)
class CompanyDetailAdmin(admin.ModelAdmin):
    list_display = ['name','description','state','job_sub_categorey']

@admin.register(JobDetail)
class JobDetailAdmin(admin.ModelAdmin):
    list_display = ['job_position','company','location','job_sub_categorey']