from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")



def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    countch = request.POST.get('countch', 'off')


    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
       # params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
       # return render(request, 'analyze.html', params)
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed =analyzed + char.upper()
        #params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    # if countch=="on":
    #     count=0
    #     for char in djtext:
    #         if not(char==" "):
    #             count+=1;
    #     #params = {'purpose':'count characters','analyzed_text':count}
    #     djtext =djtext +count
    #  #   return render(request,'analyze.html',params)

    params = {'purpose': 'count characters', 'analyzed_text': djtext}

    return render(request, 'analyze.html', params)


