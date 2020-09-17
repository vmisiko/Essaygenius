
from rest_framework import serializers
from .models import CustomUser

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         print(validated_data)
#         password = validated_data.pop('password')
#         user = CustomUser(**validated_data)
#         user.set_password(password)
#         user.save()
#         return user

class UserSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={"input":"password"}, write_only=True)
    class Meta:
        model = CustomUser
        fields = ('email', 'password', "password2")
        extra_kwargs = {'password': {'write_only': True}}


    def save(self):
        user  =  CustomUser(
            email=self.validated_data["email"],
        )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise serializers.validationError({"password":"password must match"})
        user.set_password(password)
        user.save()



class UserGetSerializer(serializers.ModelSerializer):

    class Meta:
        model= CustomUser
        exclude = ["password",]

