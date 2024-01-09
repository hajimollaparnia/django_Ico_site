from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Token, ICO, TokenPurchase, UserWallet
from .forms import TokenPurchaseForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Token, ICO, TokenPurchase, UserWallet
from .forms import TokenPurchaseForm


def token_page(request, token_id=None):
    tokens = Token.objects.all()
    token = get_object_or_404(Token, id=token_id) if token_id else None
    ico = ICO.objects.filter(token=token).first() if token else None
    purchases = TokenPurchase.objects.filter(token=token) if token else None
    wallet, created = UserWallet.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = TokenPurchaseForm(request.POST)
        if form.is_valid():
            # Process the form data, update UserWallet and TokenPurchase models
            # ...

            return redirect('token_page')  # Redirect to the same page after purchase
    else:
        form = TokenPurchaseForm()

    context = {
        'tokens': tokens,
        'token': token,
        'ico': ico,
        'purchases': purchases,
        'wallet': wallet,
        'form': form,
    }

    return render(request, 'token_page.html', context)

#
# class TokenListView(ListView):
#     model = Token
#     template_name = 'token_list.html'
#     context_object_name = 'tokens'
#
#
# class TokenDetailView(DetailView):
#     model = Token
#     template_name = 'token_detail.html'
#     context_object_name = 'token'
#
#
# def purchase_token(request, token_id):
#     token = Token.objects.get(id=token_id)
#
#     if request.method == 'POST':
#         form = TokenPurchaseForm(request.POST)
#         if form.is_valid():
#             # Process the form data, update UserWallet and TokenPurchase models
#             # ...
#
#             return redirect('token_list')  # Redirect to token list after purchase
#     else:
#         form = TokenPurchaseForm()
#
#     return render(request, 'purchase_token.html', {'form': form, 'token': token})
#
# def token_page(request, token_id=None):
#     # دریافت تمام توکن‌ها از دیتابیس
#     tokens = Token.objects.all()
#
#     # اگر token_id وجود داشته باشد، توکن مورد نظر را بر اساس آن بیاب یا در غیر این صورت None باشد
#     token = get_object_or_404(Token, id=token_id) if token_id else None
#
#     # اگر توکن موجود باشد، اطلاعات ICO مربوط به آن را بیاب
#     ico = ICO.objects.filter(token=token).first() if token else None
#
#     # اگر توکن موجود باشد، خریدهای انجام شده بر اساس آن را بیاب
#     purchases = TokenPurchase.objects.filter(token=token) if token else None
#
#     # اگر کاربر وارد شده باشد، اطلاعات کیف پول کاربر را بیاب
#     wallet = UserWallet.objects.get(user=request.user) if request.user.is_authenticated else None
#
#     # اگر درخواست ارسال شده توسط فرم پستی باشد
#     if request.method == 'POST':
#         # ساخت یک فرم پستی TokenPurchaseForm با داده‌های درخواست
#         form = TokenPurchaseForm(request.POST)
#
#         # اگر اعتبارسنجی فرم موفق باشد
#         if form.is_valid():
#             # پردازش داده‌های فرم، به‌روزرسانی مدل‌های UserWallet و TokenPurchase
#             # ...
#
#             # هدایت به همان صفحه بعد از انجام خرید
#             return redirect('token_page')
#
#     else:
#         # اگر درخواست متد GET باشد، یک فرم پستی خالی ایجاد کن
#         form = TokenPurchaseForm()
#
#     # تنظیمات متغیرها برای ارسال به قالب
#     context = {
#         'tokens': tokens,
#         'token': token,
#         'ico': ico,
#         'purchases': purchases,
#         'wallet': wallet,
#         'form': form,
#     }
#
#     # ارسال متغیرها به قالب و نمایش صفحه
#     return render(request, 'token_page.html', context)
