from django.contrib import admin
from .models import Word # Word 모델 가져오기

admin.site.register(Word) # 관리자 페이지에서 보기 위해 Word 모델 등록
