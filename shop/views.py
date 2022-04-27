from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator,InvalidPage,EmptyPage

# Create your views here.

def home(request,c_slug=None):
    c_page =None
    prodt=None
    if c_slug!=None:
        c_page = get_object_or_404(categ,slug=c_slug)
        prodt = product.objects.filter(category=c_page, available=True).order_by('name')
    else:
        prodt = product.objects.all().filter(available=True).order_by('name')
    cat=categ.objects.all()
    # creating paginator object
    p=Paginator(prodt,6)
    try:
        # getting page number if int  otherwise return to page one
        page_no=int(request.GET.get('page','1'))
    except:
        page_no=1
    try:
        pro=p.page(page_no)
    except(EmptyPage,InvalidPage):
        # inavalid or empty page return last page
        pro=p.page(p.num_pages)
    return render(request, 'index.html', {'pr':prodt,'ct':cat,'pro':pro})

def prodDetails(request,c_slug,product_slug):
    try:
        prod=product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'item.html',{'prod':prod})

def searching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=product.objects.all().filter(Q(name__contains=query)|Q(author__contains=query))
    return render(request,'search.html',{'qr':query,'prod':prod})
