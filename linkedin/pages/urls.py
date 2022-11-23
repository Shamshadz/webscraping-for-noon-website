from django.urls import path
from pages import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('home',login_required(views.StateListView.as_view()),name='home'),
    path('search',login_required(views.search),name='search'),
    path('<slug:slug>/categorey',login_required(views.CategoreyView.as_view()),name='categorey-list'),
    path('<slug:state_slug>/<slug:cat_slug>/subcategorey',login_required(views.SubCategoreyView.as_view()),name='subcategorey-list'),
    path('<slug:state_slug>/<slug:sub_cat_slug>/jobDetail',login_required(views.JobDetailView.as_view()),name='jobDetail-list'),
]
