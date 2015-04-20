# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.core.context_processors import csrf

from .models import Business
from .single import listkeywords

# form
def search_form(request):
	return render_to_response('search/search_form.html')

# recieve request
def search(request):  
	request.encoding='utf-8'
	if 'b_name' in request.GET:
		if 'zipcode' in request.GET:
			n = request.GET['b_name']
			z = request.GET['zipcode']
			possible_name = Business.objects.filter(b_name__icontains=n)
			b = Business.objects.filter(b_name__icontains=n, b_zipcode__icontains=z)
			if len(b) != 0:
				b = b[0]
				message = "Business detail:" + b.b_id + "\t" + b.b_name+ "\t"+str(b.b_zipcode)
				keywords = listkeywords(b.b_id)
				return render(request,'search/results.html',{'business':b,"keywords":keywords})
				#return HttpResponse(message)
			else:
				return render(request,"search/all_business.html",{'business_db':possible_name})
		else:
			message = "please input zipcode"
	else:
		message = 'You input nothing'
	return HttpResponse(message)

# 接收POST请求数据
def search_post(request):
	ctx ={}
	ctx.update(csrf(request))
	if request.POST:
		ctx['rlt'] = request.POST['q']
		ctx['rrr'] = request.POST['qw']
	return render(request, "search/post.html", ctx)