from django.shortcuts import render
from .models import Pet, CorporatePet
from entrust.models import EntrustApplication  # 导入寄养申请模型



def about(request):
    # 渲染关于页面的视图函数
    # 参数: request - HTTP请求对象
    # 返回: 渲染后的about.html模板
    return render(request, 'about.html')  # 修正后的模板路径



def adoption(request):
    # 渲染宠物领养页面的视图函数
    # 功能: 获取审核通过的寄养申请作为可领养宠物数据，传递给模板
    # 参数: request - HTTP请求对象
    # 返回: 渲染后的adoption.html模板，包含可领养宠物列表
    # 获取审核状态为'approved'的寄养申请（即已通过审核可领养的宠物）
    approved_entrusts = EntrustApplication.objects.filter(status='approved')
    return render(request, 'adoption.html', {'pets': approved_entrusts})



from django.contrib import messages
from .models import AdoptionApplication
from django.shortcuts import get_object_or_404, redirect
from entrust.models import EntrustApplication


def pet_detail(request, pk):
    # 宠物详情页视图
    pet = get_object_or_404(EntrustApplication, pk=pk)
    return render(request, 'pet_detail.html', {'pet': pet})


def adoption_apply(request, pet_id):
    # 领养申请提交视图
    pet = get_object_or_404(EntrustApplication, pk=pet_id)
    if request.method == 'POST':
        AdoptionApplication.objects.create(
            pet=pet,
            applicant_name=request.POST['name'],
            applicant_phone=request.POST['phone'],
            applicant_address=request.POST['address']
        )
        messages.success(request, '已提交管理员审核，请等待通过')
        return render(request, 'adoption_apply.html', {'pet': pet})
    return render(request, 'adoption_apply.html', {'pet': pet})


def corporate_adoption(request):
    # 渲染企业领养（工作犬）页面的视图函数
    # 功能: 获取所有待领养的工作犬数据，传递给模板
    # 参数: request - HTTP请求对象
    # 返回: 渲染后的corporate_adoption.html模板，包含工作犬列表
    # 查询所有工作犬记录（可根据实际需求添加过滤条件如'available=True'）
    corporate_pets = CorporatePet.objects.all()
    return render(request, 'corporate_adoption.html', {'corporate_pets': corporate_pets})