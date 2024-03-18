from django.shortcuts import render
from app.models import SEO
from django.db.models import Q

from django.shortcuts import render
from django.core.paginator import Paginator
from app.models import SEO

# Create your views here.
def index(request):
    data = SEO.objects.all()
    data = SEO.objects.all().order_by('-domain')
    name_query = request.GET.get('domain')
    company_query = request.GET.get('visits')
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(
            Q(domain__icontains=q) |
            Q(visits__icontains=q)
            )
        data = SEO.objects.filter(multiple_q).order_by()
    if name_query:
        data = data.filter(domain__icontains=name_query)
    if company_query:
        data = data.filter(visits__icontains=company_query)

    for entry in data:
        entry.mainname = entry.domain.split('.')[0]
        entry.endname = entry.domain.split('.')[1]
        entry.mainnamelength = len(entry.mainname)
    paginator = Paginator(data, 100)  # 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})
def contact(request):
    return render(request, 'contact.html')

    
#def index(request):
     
    data = SEO.objects.all().order_by('-domain')
    name_query = request.GET.get('domain')
    company_query = request.GET.get('visits')
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(
            Q(domain__icontains=q) |
            Q(visits__icontains=q)
            )
        data = SEO.objects.filter(multiple_q).order_by()
    if name_query:
        data = data.filter(domain__icontains=name_query)
    if company_query:
        data = data.filter(visits__icontains=company_query)

    for entry in data:
        entry.mainname = entry.domain.split('.')[0]
        entry.endname = entry.domain.split('.')[1]
        entry.mainnamelength = len(entry.mainname)
    
   
    if company_query:
        data = data.filter(visits__icontains=company_query)
    #for entry in data:
        #entry.mainnamelength = len(entry.mainname)

    context = {
        'data': data,
    }
    print(context)
    return render(request, 'index.html',context)

def contact(request):
    return render(request, 'contact.html')
    