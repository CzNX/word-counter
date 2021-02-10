from django.shortcuts import render
import operator

def home(request):
  return render(request,'home.html')


def count(request):
  fulltext = request.GET['fulltext']
  wordlist = fulltext.split()

  dic = {}

  for word in wordlist:
    if word in dic:
      #increase (times)
      dic[word] =dic[word]+1  #or dic[word] += 1  i.e adding 1 to pre-existing value of that specific word
    else:
      #add
      dic[word] = 1  #where key = word and value = 1

    sort = sorted(dic.items(),key=operator.itemgetter(1),reverse=True) # operator.itemgetter(0) i.e taking 'key' of         dictionary in account and  operator.itemgetter(1) i.e taking 'value' of dictionary in account .

  return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sort':sort})

def about(request):
  return render(request,'about.html')