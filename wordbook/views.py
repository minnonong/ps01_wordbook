from django.shortcuts import render
from django.utils import timezone
from .models import Word

def word_list(request):
    words = Word.objects.filter(reg_date__lte = timezone.now()).order_by('reg_date')
    return render(request, 'wordbook/word_list.html',{'words': words})
