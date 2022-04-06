from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def result(request):
    sentence = str(request.POST.get('sentence')) # index.html textarea 에서 문자열을 받아옴
    sentence_to_list=sentence.split() # 공백을 기준으로 나눠 저장

    dictionary = {}
    #{word1:count10, word2:count2 ......}
    for word in sentence_to_list:
        if word in dictionary:
            dictionary[word]+=1
        else: dictionary[word]=1

    #[{안녕:3}, {동윤:1}]
    word_count = list(dictionary.items())

    return render(request,"result.html", {"word_count": word_count}) #result.html변수 : views.py변수
    

# Create your views here.
