from django.http import HttpResponse
from django.shortcuts import render
def index(request):
	return render(request,'index.html')
def keshav(request):
	djtext=request.GET.get('text','default')
	djchecki=request.GET.get('esehi','off')
	djchecki2=request.GET.get('UPPER','off')
	Punctuation='''""{}[]<,>.?/!@#$%^&*()_+=|\`~;:'''
	if(djchecki=='on'):
			if(djchecki2=="on"):
				analyzed=""
				bua=""
				for char in djtext:
					if char not in Punctuation:
						analyzed=analyzed+char
				for char in analyzed:
					bua=bua+char.upper()
				params={'purpose':'Both Operations','analyze_text':bua}
				return render(request,'analyize.html',params)
			else:
				analyzed=""
				for char in djtext:
					if char not in Punctuation:
						analyzed=analyzed+char
				params={'purpose':'Remove Punctuation','analyze_text':analyzed}
				return render(request,'analyize.html',params)
	elif(djchecki2=="on"):
		analyzed=""
		for char in djtext:
			analyzed=analyzed+char.upper()
		params={'purpose':'For Converting in Upper case','analyze_text':analyzed}
		return render(request,'analyize.html',params)
	else:
		request(HttpResponse('error404'))
def chinu(request):
	return HttpResponse("Hello Chinu")