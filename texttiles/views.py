from django.http import HttpResponse
from django.shortcuts import render
def index(request):
	return render(request,'index.html')
def keshav(request):
	djtext=request.GET.get('text','default')
	djchecki=request.GET.get('esehi','off')
	Punctuation='''""{}[]<,>.?/!@#$%^&*()_+=|\`~;:'''
	analyzed=""
	for char in djtext:
		if char not in Punctuation:
			analyzed=analyzed+char
	params={'purpose':'Remove Punctuation','analyze_text':analyzed}
	return render(request,'analyize.html',params)
	return HttpResponse("Hello Keshav <a href='/'>Back</a>")
def chinu(request):
	return HttpResponse("Hello Chinu")