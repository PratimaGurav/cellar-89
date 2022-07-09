"""
Config file for checkout app
"""
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Checkout app Config
    """
    name = 'checkout'

    def ready(self):
        import checkout.signals
