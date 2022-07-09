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
        # pylint: disable=unused-import, import-outside-toplevel
        import checkout.signals
