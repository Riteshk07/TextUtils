from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return render(request, "index.html")

def analyze(request):
    djtext = request.POST.get("text", "default")
    capital = request.POST.get("case", "off")
    punctuate = request.POST.get("removePunc", "off")
    remvSpace = request.POST.get("removeSpace", "off")
    remvNewLine = request.POST.get("removeNewLine", "off")
    mkTitle = request.POST.get("case", "off")
    analyzed = djtext
    flag = False

    if (punctuate == "on"):
        analyzed = removePunc(analyzed)
        flag = True
    if (remvNewLine == "on"):
        analyzed = removeNewLine(analyzed)
        flag = True
    if (remvSpace=="on"):
        analyzed = removeSpace(analyzed)
        flag = True
    if (capital == "capitalize"):
        analyzed = capitalize(analyzed)
        flag = True
    if (mkTitle == "makeTitle"):
        analyzed = makeTitle(analyzed)
        flag = True
    if flag:
        params = {"purpose":"Capitalized Text", "analyzed_text":analyzed}
        return render(request, "analyze.html", params)
    return HttpResponse('''Error''')

def capitalize(text):
    newText = ""
    for i in text:
        k = ord(i)
        if k <= 122 and k >= 97:
            newText += chr(k - 32)
        else:
            newText += i
    return newText

def removeSpace(text):
    newText = ""
    l = len(text) - 1
    flag = False
    for i in range(l):
        if (text[i] != " "):
            newText += text[i]
            flag = True
        if (flag):
            if (text[i] == " " and text[i + 1] != " "):
                newText += " "
    newText += text[l]
    return newText

def removePunc(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    newText = ""
    for char in text:
        if char not in punctuations:
            newText = newText + char

    return newText

def makeTitle(text):
    newText =""
    k = ord(text[0])
    if k <= 122 and k >= 97:
        newText += chr(k - 32)
    l = len(text)
    for i in range(1,l):
        k = ord(text[i])
        m = text[i-1]
        if (m == " " or m == "\n") and (k <= 122 and k >= 97):
            newText += chr(k-32)
        elif k<=90 and k>=65:
            newText += chr(k+32)
        else:
            newText += text[i]
    return newText

def removeNewLine(text):
    newText =""
    for i in text:
        if(i != "\n" and i !="\r"):
            newText += i
    return newText


