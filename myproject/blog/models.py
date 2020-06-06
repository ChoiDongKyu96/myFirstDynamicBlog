from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 필드를 외래키로 만들며 다른테이블과 연결됨을 뜻한다.
    # 기본적으로 AUTH_USER_MODEL은 내장되어있다.글들을 작성자 목록과 연결한것
    title = models.CharField(max_length=100)
    # 글 제목 CharFiled는 글자 수가 제한된 텍스트 필드를 뜻한다. 글제목과 같이 짧은 문자열 정보를 젖아할때 사용한다.
    # 100자까지허용한다.
    content = models.TextField(blank=True)
    # 글 내용, blank옵션은 비어있는경우 처리하는가이다.
    created_date = models.DateTimeField(auto_now_add=True)
    # 글 작성날짜
    published_date = models.DateTimeField(blank=True, null=True)
    # 글 게시 날짜auto는 처음 생성될때 시간 자동저장
    # null은 비어있는값을 데이터베이스에 Null로 저장할지 여부
    def __str__(self):
        return self.title
