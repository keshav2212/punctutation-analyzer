from django.http import HttpResponse
from django.shortcuts import render
def index(request):
	return render(request,'index.html')
def keshav(request):
	djtext=request.POST.get('text','default')
	djchecki=request.POST.get('esehi','off')
	djchecki2=request.POST.get('UPPER','off')
	djchecki3=request.POST.get('newlineremover','off')
	djchecki4=request.POST.get('extraspaceremover','off')
	Punctuation='''""{}[]<,>.?/!@#$%^&*()_+=|\`~;:'''
	if(djchecki=='on'):
		analyzed=""
		bua=""
		for char in djtext:
			if char not in Punctuation:
				analyzed=analyzed+char
		djtext=analyzed
		params={'purpose':'Remove Punctuation','analyze_text':analyzed}
	if(djchecki2=="on"):
		analyzed=""
		for char in djtext:
			analyzed=analyzed+char.upper()
		params={'purpose':'To Upper Case','analyze_text':analyzed}
		djtext=analyzed
				#return render(request,'analyize.html',params)
	if(djchecki3=='on'):
		analyzed=""
		for char in djtext:
			if (char!='\n' and char!='\r'):
				analyzed=analyzed+char
		params={'purpose':'New line remover','analyze_text':analyzed}
		djtext=analyzed
		#return render(request,'analyize.html',params)
	if(djchecki4=='on'):
		analyzed=""
		for index,char in enumerate(djtext):
			if (djtext[index]==' ' and djtext[index+1]==' '):
				pass
			else:
				analyzed=analyzed+char
		params={'purpose':'Extra Space remover','analyze_text':analyzed}
	if(djchecki!='on' and djchecki2!='on' and djchecki3!='on' and djchecki4!='on' ):
		return HttpResponse("Error404")
	return render(request,'analyize.html',params)
	
def chinu(request):
	return HttpResponse("Hello Chinu")