from django.contrib import admin
from blog.models import Post# models.py에서 Post 모델을 가져온다.
# Register your models here.

admin.site.register(Post) # Post를 관리자 페이지에 등록한다
