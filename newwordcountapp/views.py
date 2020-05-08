from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split() #words는 단어들이 담겨있는 리스트
    word_dictionary = {} #<단어: 몇번, 단어: 몇번>으로 저장되어 있음
    check_duplicate = {} #중복된 문자열

    for word in words:  #word는 반복문 변수임.
        if word in word_dictionary: 
            #increase
            word_dictionary[word]+=1
            check_duplicate[word]+=1
        else:
            #add to dictionary
            word_dictionary[word]=1
            check_duplicate[word]=0

    return render(request, 'result.html', {'full': text, 'total': len(words), 'dictionary': word_dictionary.items(), 'duplication': check_duplicate.items()})