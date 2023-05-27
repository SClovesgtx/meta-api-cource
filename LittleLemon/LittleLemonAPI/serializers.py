from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import MenuItem
from decimal import Decimal
import bleach


class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source="inventory")
    price_after_tax = serializers.SerializerMethodField(method_name="calculate_tax")
    # price = serializers.DecimalField(
    #     max_digits=6, decimal_places=2, min_value=Decimal(2.0)
    # )
    title = serializers.CharField(
        max_length=100, validators=[UniqueValidator(queryset=MenuItem.objects.all())]
    )

    class Meta:
        model = MenuItem
        fields = ["id", "title", "price", "stock", "price_after_tax"]
        # extra_kwargs = {
        #     "title": {"required": True, "allow_blank": False, "max_length": 100},
        #     "price": {"required": True, "min_value": Decimal(2.0)},
        #     "stock": {
        #         "required": True,
        #         "min_value": Decimal(0.0),
        #         "source": "inventory",
        #     },
        # }

    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal(1.1)

    def validate_price(self, value):
        if value < Decimal(2.0):
            raise serializers.ValidationError("Price must be greater than 2.0")
        return value

    def validate_stock(self, value):
        if value < Decimal(0.0):
            raise serializers.ValidationError("Stock must be greater than 0.0")
        return value

    def validate_title(self, value):
        if len(value) <= 1:
            raise serializers.ValidationError(
                "Title must be at least 2 characters long"
            )
        return bleach.clean(value)
