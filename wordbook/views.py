from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Word
from .forms import WordForm

def word_list(request):
    words = Word.objects.filter(reg_date__lte = timezone.now()).order_by('reg_date')
    return render(request, 'wordbook/word_list.html',{'words': words})

def word_new(request):
    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.save(commit=False)
            word.author = request.user
            word.reg_date = timezone.now()
            word.save()
            return redirect('word_list')
    else:
        form = WordForm()
    return render(request, 'wordbook/word_edit.html', {'form': form})
