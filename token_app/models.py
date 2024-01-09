from django.db import models
from django.contrib.auth.models import User


class Token(models.Model):

    # نام توکن با حداکثر طول ۲۵۵ کاراکتر
    name = models.CharField(max_length=255)

    # نماد توکن با حداکثر طول ۱۰ کاراکتر و باید یکتا باشد
    symbol = models.CharField(max_length=10, unique=True)

    # مجموع عرضه توکن با حداکثر ۲۰ رقم در اعشار
    total_supply = models.DecimalField(max_digits=20, decimal_places=2)


class SmartContract(models.Model):
    token = models.OneToOneField(Token, on_delete=models.CASCADE)


class ICO(models.Model):

    # یک به یک با مدل Token، در صورت حذف Token، این مدل نیز حذف شود
    token = models.OneToOneField(Token, on_delete=models.CASCADE)

    # یک به یک با مدل SmartContract، در صورت حذف SmartContract، این مدل نیز حذف شود
    smart_contract = models.OneToOneField(SmartContract, on_delete=models.SET_NULL, null=True, blank=True)

    # تاریخ شروع ICO
    start_date = models.DateTimeField()

    # تاریخ پایان ICO
    end_date = models.DateTimeField()

    # حداکثر مقدار پولی که می‌خواهیم جمع آوری کنیم با حداکثر ۲۰ رقم در اعشار
    hard_cap = models.DecimalField(max_digits=20, decimal_places=2)

    # حداقل مقدار پولی که می‌خواهیم جمع آوری کنیم با حداکثر ۲۰ رقم در اعشار
    soft_cap = models.DecimalField(max_digits=20, decimal_places=2)


class TokenPurchase(models.Model):

    # کاربری که Token را خریداری کرده است با استفاده از کلید خارجی
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Token خریداری شده با استفاده از کلید خارجی
    token = models.ForeignKey(Token, on_delete=models.CASCADE)

    # تعداد Token خریداری شده
    quantity = models.PositiveIntegerField()

    # قیمت پرداخت شده برای Token با حداکثر ۱۰ رقم در اعشار
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # تاریخ و زمان خرید Token
    date_purchased = models.DateTimeField(auto_now_add=True)


class UserWallet(models.Model):

    # یک به یک با مدل User، در صورت حذف User، این مدل نیز حذف شود
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # موجودی کیف پول کاربر با حداکثر ۲۰ رقم در اعشار
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)



