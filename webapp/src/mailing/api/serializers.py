from rest_framework import serializers
from ..models import Client, Mailing, Message

class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
    


# class ClientSerializer(serializers.Serializer):

    # phone_regex = RegexValidator(
    #     regex=r"^\+?7?\d{7,11}$",
    #     message="Phone number must be entered in the format: '7999999999'. Up to 11 digits not allowed."
    # )

    # phone_number = serializers.CharField(validators=[phone_regex], max_length=11)
    # operator = serializers.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(900)])
    # tag = serializers.CharField(max_length=50)
    # timezone = serializers.CharField(max_length=32, default="UTC")

#     def create(self, validated_data):
#         return Client.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.phone_number = validated_data.get("phone_number", instance.phone_number)
#         instance.operator = validated_data.get("operator",instance.operator)
#         instance.tag = validated_data.get("tag", instance.tag)
#         instance.timezone = validated_data.get("timezone", instance.timezone)
#         instance.save
#         return instance

# class MessageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Client
#         fields = ['client', 'mailing', 'sending_status', 'start_date']
#     pass