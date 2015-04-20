
from django.shortcuts import render, get_object_or_404,render_to_response,render_to_response
from django.http import HttpResponse,Http404
from django.template import RequestContext, loader

from .models import Business
from .utils import printme

# Create your views here.

def index(request):
    #r = requests.get('http://httpbin.org/status/418')
    #times = int(os.environ.get('TIMES', 3))
    #b = printme("My input.")
    #print(r.text)
    #return HttpResponse("<pre> %s </pre>" %r.text)
    template = loader.get_template('search/index.html')
    context = RequestContext(request,{'Title':'Yelp Refiner'})
    return render(request,'search/index.html',context)

def all_business(request):
    business_db = Business.objects.all()
    return render(request,'search/all_business.html',{'business_db':business_db})



def results(request):
    #business = get_object_or_404(Business, pk=b_id)
    #try:
    #    founded = business.choi
    #kw = ['delicious','good atmosphere','good for dinner','inexpensive', 'fantastic']
    #return render(request,'search/results.html',{'Business':business, 'Keyword':kw})
    if 'business_name' in request.GET and request.GET['business_name']:
        business_name=request.GET['business_name']
        if 'zipcode' in request.GET and request.GET['zipcode']:
            zipcode=request.GET['zipcode']
            business=Business.objects.filter(b_name__icontains=business_name)[0]
            return render_to_response('results.html',{'business':business})
        else:
            return HttpResponse('Please submit a search term.')
