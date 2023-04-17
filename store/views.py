from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator

from .models import Store
from .forms import StoreForm
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request,'store/index.html',{
        'store':Store.objects.all()
    })
def view_store(request,id):
    store = store.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index')) 
def add(request):
    if request.method == 'POST':
        form = StoreForm(request.POST ,request.FILES)
        if form.is_valid():
           new_part_number =form.cleaned_data['part_number']
           new_purchase_order =form.cleaned_data['purchase_order']
           new_mat_code =form.cleaned_data['mat_code']
           new_description=form.cleaned_data['description']
           new_quantity=form.cleaned_data['quantity']
           new_qty_consumed=form.cleaned_data['qty_consumed']
           new_location=form.cleaned_data['location']
           new_gate_pass=form.cleaned_data['gate_pass']
           new_Date =form.cleaned_data['Date']
           new_image = form.cleaned_data['image']

           new_Store = Store(
           part_number = new_part_number,
           purchase_order = new_purchase_order,
           mat_code = new_mat_code,
           description = new_description,
           quantity = new_quantity,
           qty_consumed = new_qty_consumed,
           location = new_location,
           gate_pass = new_gate_pass,
           Date = new_Date,
           image = new_image
           )
           new_Store.save()
           return render(request,'store/add.html',{
            'form': 'StoreForm()',
            'success': 'True'
           })
    else:
         form = StoreForm()
    return render(request,'store/add.html',{
        'form' : StoreForm()
    })



def edit(request, id):
    if request.method == 'POST':
      store = Store.objects.get(pk=id)
      form=StoreForm(request.POST,instance=store,files=request.FILES)
      if form.is_valid():
        form.save()
        return render(request,'store/edit.html',{
            'form':form,
            'success':True
        })
    else:
       store = Store.objects.get(pk=id)
       form = StoreForm(instance=store)
    return render(request,'store/edit.html',{
        'form':form
    })
def delete(request,id):
    if request.method == 'POST':
        store = Store.objects.get(pk=id)
        store.delete()
    return HttpResponseRedirect(reverse('index'))

def index(request):
   
    store = Store.objects.all()
    p = Paginator(store, 5)
    store = request.GET.get('page')
    store=p.get_page(store)

    contex = {'store' : store}
    return render(request,'store/index.html', contex)

def search(request):
    q=request.GET['q']
    #store = Store.objects.filter(part_number__icontains=q)
    multiple_q = Q(Q(part_number__icontains = q) | Q(description__icontains = q) | Q(gate_pass__icontains = q) | Q(mat_code__icontains = q))
    store = Store.objects.filter(multiple_q)
    params = {'store':store}
    return render(request, 'store/search.html',params)
 