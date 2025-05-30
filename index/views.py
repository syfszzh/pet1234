from django.shortcuts import render



def index(request):
    # 渲染网站首页的视图函数
    # 参数: request - HTTP请求对象
    # 功能: 处理首页的GET请求，返回渲染后的首页模板
    # 返回: 渲染后的index.html模板（网站首页）
    return render(request, 'index.html')