from rest_framework import serializers

from FAQ.models import FaqModel


class FAqSerializers(serializers.ModelSerializer):
    class Meta:
        model = FaqModel
        fields = "__all__"