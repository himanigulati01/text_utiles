from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    
    return render(request,'index.html')
def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')
    
    if removepunc=='on':
        analyzed=""
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        para={'purpose':"removing punctuations",'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',para)

    if fullcaps=='on':
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        para={'purpose':"uppercase",'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',para)
    if newlineremover=='on':
        analyzed=""
        for char in djtext:
            if char!='\n'and char!='\r':
                analyzed=analyzed+char
        para={'purpose':"newlineRemoved",'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',para)
    if extraspaceremover=="on":
        
        analyzed = " "
        for i in range (len(djtext)-1):
            if not(djtext[i]==" " and djtext[i+1]==" "):
                 analyzed=analyzed+djtext[i]
                 
        para={'purpose':"extraspaceremover",'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',para)
    if charcount=="on":
        c=0
        for i in djtext:
            if i!=" ":
                c+=1
        para={'purpose':"charcount",'analyzed_text': c}
        djtext=c

        #return render(request,'analyze.html',para
    if(removepunc!='on' and fullcaps!='on' and newlineremover!='on'and extraspaceremover!="on" and charcount!="on"):
    
        return render(request,'error.html')

    
    return render(request,'analyze.html',para)
    
        



        
    
    

