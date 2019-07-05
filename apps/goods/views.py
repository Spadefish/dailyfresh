from django.shortcuts import render


# Create your views here.

def index(request):
    # 商品首页
    return render(request, 'index.html')
