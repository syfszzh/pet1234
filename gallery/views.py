from django.shortcuts import render, get_object_or_404
from .models import GalleryImage



def gallery(request):
    # 渲染宠物画廊列表页面的视图函数
    # 参数: request - HTTP请求对象
    # 功能: 查询数据库中所有画廊图片记录，传递给模板显示
    # 返回: 渲染后的gallery.html模板，包含所有图片数据
    # 查询GalleryImage模型的所有记录（即所有上传的画廊图片）
    # 获取随机排序的前5张图片（使用order_by('?')实现随机排序，[:5]取前5条）
    images = GalleryImage.objects.all().order_by('?')[:5]
    return render(request, 'gallery.html', {'images': images})



def gallery_detail(request, image_id):
    # 渲染单个宠物图片详情页面的视图函数
    # 参数:
    #   request - HTTP请求对象
    #   image_id - 要查看详情的图片ID（来自URL参数）
    # 功能: 根据ID查询具体图片记录，若不存在则返回404错误
    # 返回: 渲染后的gallery_detail.html模板，包含单张图片详细信息
    # 使用get_object_or_404快捷函数：查询到则返回对象，未找到则返回404页面
    image = get_object_or_404(GalleryImage, id=image_id)
    return render(request, 'gallery_detail.html', {'image': image})