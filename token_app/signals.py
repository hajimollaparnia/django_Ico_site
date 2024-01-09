from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TokenPurchase, UserWallet


@receiver(post_save, sender=TokenPurchase)
def update_wallet_balance(sender, instance, **kwargs):
    # Update UserWallet balance when a TokenPurchase is made
    user_wallet = instance.user.userwallet
    user_wallet.balance -= instance.price * instance.quantity
    user_wallet.save()
