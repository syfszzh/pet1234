from django.shortcuts import render, redirect
from django.contrib import messages
from .models import EntrustApplication



def entrust_form(request):
    # 处理宠物寄养申请表单提交的核心视图函数
    # 参数说明:
    #   request: Django标准HTTP请求对象，包含用户提交的表单数据或GET请求信息
    # 返回值:
    #   渲染后的HTML模板（GET请求或表单验证失败时）
    #   重定向响应（表单提交成功时）
    if request.method == 'POST':
        # 从POST请求中提取表单字段数据（对应HTML表单中name属性值）
        name = request.POST.get('name')          # 申请人姓名（文本输入）
        phone = request.POST.get('phone')        # 联系电话（文本输入）
        pet_name = request.POST.get('pet_name')  # 宠物名称（文本输入）
        pet_age = request.POST.get('pet_age')    # 宠物年龄（文本输入，建议格式：数字+单位如'3岁'）
        pet_species = request.POST.get('pet_species')  # 宠物品种（文本输入，如'中华田园猫'）
        description = request.POST.get('description')  # 宠物描述（文本区域，可填写健康状况等）
        pet_image = request.FILES.get('pet_image')     # 宠物图片（文件上传字段，需处理文件存储）

        # 使用all()函数验证所有必填字段是否非空（包括文件上传是否存在）
        # 注：all()会检查可迭代对象中所有元素是否为True（非空字符串、非None、非空文件对象等）
        if all([name, phone, pet_name, pet_age, pet_species, description, pet_image]):
            # 通过模型类创建数据库记录，自动处理文件上传到MEDIA_ROOT目录
            # 字段与数据库表列一一对应，pet_image会存储文件相对路径
            EntrustApplication.objects.create(
                name=name,
                phone=phone,
                pet_name=pet_name,
                pet_age=pet_age,
                pet_species=pet_species,
                description=description,
                pet_image=pet_image
            )
            # 使用Django消息框架添加成功提示，该消息会在前端模板中显示
            messages.success(request, '已成功提交，请等待管理员审核！')
            # 重定向回表单页面（避免F5重复提交表单的问题）
            return redirect('entrust_form')
        else:
            # 任意必填字段缺失时添加错误提示，前端模板需支持显示messages
            messages.error(request, '请填写所有必填字段并上传宠物图片！')

    # 处理GET请求时（首次访问页面或重定向后），渲染空表单模板
    return render(request, 'entrust/entrust_form.html')
