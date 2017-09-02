from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
# 단어
class Word(models.Model):
    author = models.ForeignKey('auth.User') # 등록자
    text = models.CharField(max_length=200) # 단어
    reg_date = models.DateTimeField('default=timezone.now') # 등록일
    check_date = models.DateField(null=True, blank=True) # 암기일

    def __str__(self):
        return self.text
