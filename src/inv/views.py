from datetime import datetime, date
from django.shortcuts import render, redirect

from inv.models import Item
from .forms import ItemForm


def home(request):
    '''
        cette vue prend une request et qui va return la valeur donnée par
      render qui va assembler notre template inv/home.html
    '''

    items = Item.objects.all()
    today = date.today()
    date_30 =date(today.year, today.month + 1,today.day)
    items_date_less30 = [Item.objects.get(id=item.id) for item in items if item.date_exp < date_30]
    return render(request, "inv/home.html", context={'items': items_date_less30})

def show(request):
    '''
            cette vue prend une request et qui va return la valeur donnée par
          render qui va assembler notre template inv/show.html
        '''

    items = Item.objects.all()
    return render(request, "inv/show.html", context={'items': items})

def add(request):
    '''
            cette vue prend une request et qui va return la valeur donnée par
          render qui va assembler notre template inv/add_item.html
        '''

    form =ItemForm()
    if request.method =='POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form,}

    return render(request, "inv/add_item.html",context)

def update(request,pk):
    '''
    NON finalisé
    '''

    item = Item.objects.get(id=pk)
    form =ItemForm(instance=item)

    if request.method =='POST':
        form = ItemForm(request.POST, instance==item)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form,}
    #items = Item.objects.all()
    #myfilter = ItemFiltre(request.Get, queryset=items)
    #myfilter = ItemFiltre()
    return render(request, "inv/show.html",context)


