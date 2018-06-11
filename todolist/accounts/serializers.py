from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.authtoken.models import Token
from rest_framework.serializers import (ModelSerializer, CharField, EmailField, 
                                        ChoiceField, BooleanField, DateField,
                                        ValidationError)
from .models import TaskAll
User = get_user_model()

class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')
    confirm_email = EmailField(label='Confirm Email')
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'confirm_email',
            'password',
        ]
        extra_kwargs = {"password":
                        {"write_only": True}
                        }

    def validate_email(self, value):
        data = self.get_initial()
        email = data.get('confirm_email')
        email_2 = value
        if email != email_2:
            raise ValidationError("Email must match")
        user_query = User.objects.filter(email=email)
        print(user_query)
        if user_query:
            raise ValidationError("This user has already registered")
        return value
    
    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username = username,
            email = email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    email = EmailField(label='Email Address')
    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'token',
        ]
    extra_kwargs = {"password":
                    {"write_only":True}
                    }

    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        password = data["password"]
        if not email:
            raise ValidationError("Email is required to login.")

        user = User.objects.filter(
                Q(email=email)
        ).distinct()

        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This Email is not valid.")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect password")
        for i in user:
            username = i
        token = Token.objects.get_or_create(user=username)
        data["token"] = token
        return data

class TaskCreateSerializer(ModelSerializer):
    task = CharField(label='Task')
    finished = DateField(label='Finish')
    class Meta:
        model = TaskAll
        fields = [
            'task',
            'created',
            'finished',
        ]

class ListTaskSerializer(ModelSerializer):
    class Meta:
        model = TaskAll
        fields = [
            'task',
            'created',
            'finished',
            'status',
        ]

class UpdateStatuskSerializer(ModelSerializer):
    task = CharField(allow_blank=True, read_only=True)
    class Meta:
        model = TaskAll
        fields = [
            'task',
            'status',
        ]