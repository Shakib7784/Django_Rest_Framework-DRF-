from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type:password"},write_only=True)#here style is working as widget of form
    class Meta:
        model=User
        fields = ["username","email","password","password2"]
        extra_kwargs={
            "password":{"write_only":True} # it will not showable
        }  
    def save(self): # to dave the data.
        username = self.validated_data["username"]
        email = self.validated_data["email"]
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        
        if password != password2:
            raise serializers.ValidationError({"error":"password does not matched"})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error":"email already exists"})
        
        account = User(username=username,email=email)
        account.set_password(password)
        account.save()
        return account
    