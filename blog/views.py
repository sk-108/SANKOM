from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request) :
    return render(request,'blog/index.html')


def analyze(request) :
    # Get the text
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charactercounter = request.POST.get('charactercounter','off')
    
    if removepunc == "on" :
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext :
            if char not in punctuations :
                analyzed = analyzed + char 
        params = { 'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed

    if(fullcaps=="on") :
        analyzed = ""
        for char in djtext :
            analyzed = analyzed + char.upper()
        params = { 'purpose':'Changed to Uppercase ','analyzed_text':analyzed}
        djtext = analyzed

    if(newlineremover == "on") :
        analyzed = ""
        for char in djtext :
            if char!="\n" :
                analyzed = analyzed + char
        params = { 'purpose':'Removed NewLine ','analyzed_text':analyzed}
        djtext = analyzed
    
    if(extraspaceremover == "on") :
        analyzed = ""
        for index,char in enumerate(djtext) :
            if not (djtext[index] == " " and djtext[index+1]) == " ":
                analyzed = analyzed + char
        params = { 'purpose':'Removed NewLine ','analyzed_text':analyzed}
        djtext = analyzed

    if(charactercounter == "on") :
        analyzed = ""
        count = 0
        for char in djtext :
            count=count+1
        params = { 'purpose':'character count is ','analyzed_text':count}
    if(charactercounter!="on" and extraspaceremover!="on" and newlineremover!="on" and removepunc!="on" and fullcaps!="on") :
        return HttpResponse("Please select the operation ")

    return render(request,'blog/analyze.html',params)

