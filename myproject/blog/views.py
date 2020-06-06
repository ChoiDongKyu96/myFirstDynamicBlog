from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post


# Create your views here.
# def helloworld(request):
#     return render(request, 'blog/helloworld.html')
def post_list(request):
	posts = Post.objects.filter(published_date__isnull=False).order_by('-created_date')
	# posts = Post.objects.all()# ORM을 통해 쿼리셋을 가져온다. 모든 Post가 나온다.
	context = {# context라는 변수에 할당한다. render 뒤에 데이터에 넣는다.
		'posts': posts,
	}
	return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
	post = Post.objects.get(pk=pk)
	context = {
		'post' : post
	}
	return render(request, 'blog/post_detail.html', context)