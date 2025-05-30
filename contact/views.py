from django.shortcuts import render, redirect
from .models import ContactMessage



def contact(request):
    # 处理用户联系信息提交的视图函数
    # 参数: request - HTTP请求对象
    # 功能:
    # - 处理POST请求: 获取表单提交的姓名、邮箱、消息
    # - 验证必填字段是否存在
    # - 验证通过则保存到ContactMessage模型
    # - 重定向回联系页面（可根据需求改为成功提示页面）
    # - 处理GET请求: 渲染联系页面模板
    if request.method == 'POST':
        # 获取POST请求中的表单字段值
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # 验证必填字段是否均有值（非空）
        if name and email and message:
            # 创建并保存新的ContactMessage记录到数据库
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message
            )
            # 保存成功后重定向回联系页面（避免表单重复提交）
            return redirect('contact')
    # 处理GET请求或POST验证失败时，渲染联系页面模板
    return render(request, 'contact.html')