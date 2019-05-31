from django.http import HttpResponse
from django.shortcuts import render
def index(request):
	return render(request,'index.html')
def keshav(request):
	djtext=request.GET.get('text','default')
	djchecki=request.GET.get('esehi','off')
	djchecki2=request.GET.get('UPPER','off')
	djchecki3=request.GET.get('newlineremover','off')
	djchecki4=request.GET.get('extraspaceremover','off')
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
	elif(djchecki3=='on'):
		analyzed=""
		for char in djtext:
			if char!='\n':
				analyzed=analyzed+char
		params={'purpose':'New line remover','analyze_text':analyzed}
		return render(request,'analyize.html',params)
	elif(djchecki4=='on'):
		analyzed=""
		for index,char in enumerate(djtext):
			if (djtext[index]==' ' and djtext[index+1]==' '):
				pass
			else:
				analyzed=analyzed+char
		params={'purpose':'Extra Space remover','analyze_text':analyzed}
		return render(request,'analyize.html',params)
	else:
		return HttpResponse("Error404")

def chinu(request):
	return HttpResponse("Hello Chinu")