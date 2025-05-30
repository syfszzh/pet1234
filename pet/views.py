from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import login


class CustomUserCreationForm(UserCreationForm):
    # 自定义用户注册表单类，继承Django内置的UserCreationForm
    # 功能：提供用户注册时的表单字段验证和错误提示
    # 重写字段说明：
    username = UsernameField(
        label=_('用户名'),
        help_text=_('必填。150个字符以内。只能包含字母、数字和@/./+/-/_符号。')
    )
    password1 = forms.CharField(
        label=_('密码'),
        strip=False,
        widget=forms.PasswordInput,
        help_text=_('密码不能太简单，不能全部是数字，至少8个字符。'),
        error_messages={
            'min_length': _('密码必须至少包含8个字符。'),
            'common_password': _('该密码太常见，容易被猜测。'),
            'numeric_password': _('密码不能全部是数字。')
        }
    )
    password2 = forms.CharField(
        label=_('确认密码'),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_('请输入与上面相同的密码以验证。')
    )

    class Meta(UserCreationForm.Meta):
        # 自定义元数据：配置字段级别的错误提示信息
        error_messages = {
            'username': {
                'unique': _('该用户名已被注册，请尝试其他用户名。'),
                'invalid': _('用户名格式无效，请使用字母、数字或@/./+/-/_符号。'),
                'required': _('用户名不能为空。')
            },
            'password2': {
                'password_mismatch': _('两次输入的密码不一致。')
            }
        }


def subscribe_success(request):
    # 渲染订阅成功页面的视图函数
    # 参数: request - HTTP请求对象
    # 返回: 渲染后的subscribe_success.html模板
    return render(request, 'subscribe_success.html')


class CustomLoginView(LoginView):
    # 自定义登录视图类，继承Django内置的LoginView
    # 功能：配置登录页面模板路径和已认证用户重定向逻辑
    template_name = 'login.html'  # 指定登录页面使用的模板文件
    redirect_authenticated_user = True  # 已认证用户访问登录页时自动重定向



from django.contrib.auth.models import User
from django.contrib import messages


def password_reset(request):
    # 密码重置视图函数
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # 验证密码一致性
        if new_password != confirm_password:
            messages.error(request, '新密码与确认密码不一致')
            return render(request, 'password_reset.html')

        try:
            user = User.objects.get(username=username)
            # 设置新密码（Django自动哈希存储）
            user.set_password(new_password)
            user.save()
            messages.success(request, '密码修改成功！请使用新密码登录')
            return redirect('login')
        except User.DoesNotExist:
            messages.error(request, '用户不存在')

    return render(request, 'password_reset.html')


def register(request):
    # 处理用户注册逻辑的视图函数
    # 参数: request - HTTP请求对象
    # 功能:
    #   - POST请求：接收并验证注册表单数据，验证通过则创建用户并跳转登录页
    #   - GET请求：渲染空注册表单供用户填写
    # 返回: 注册页面模板（含表单数据或错误提示）或登录页重定向响应
    if request.method == 'POST':
        # 实例化自定义注册表单，绑定POST请求数据
        form = CustomUserCreationForm(request.POST)
        # 验证表单数据有效性（字段格式、密码复杂度等）
        if form.is_valid():
            # 验证通过后保存用户到数据库（自动哈希密码）
            user = form.save()
            # 注册成功后重定向到登录页面
            return redirect('login')
    else:
        # GET请求时实例化空表单（无绑定数据）
        form = CustomUserCreationForm()
    # 渲染注册页面模板，传递表单对象（含错误提示）
    return render(request, 'register.html', {'form': form})