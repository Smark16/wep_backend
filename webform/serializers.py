from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.db import IntegrityError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'date_joined']

class ObtainSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        if hasattr(user, 'profile'):
            token['middle_name'] = user.profile.middle_name
            token['email'] = user.email
            token['mobile'] = user.profile.mobile

        return token

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserAccount
        fields = ['id', 'email', 'first_name', 'last_name', 'middle_name', 'mobile', 'password', 'confirm_password']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return data

    def create(self, validated_data):
        user_data = {
            'email': validated_data['email'],
            'username': validated_data['email'],  # Use email as username
            'first_name': validated_data['first_name'],
            'last_name': validated_data['last_name'],
        }
        password = validated_data.pop('password')
        validated_data.pop('confirm_password')
        try:
            user = User.objects.create(**user_data)
            user.set_password(password)
            user.save()

            user_account = UserAccount.objects.create(
                user=user,
                middle_name=validated_data['middle_name'],
                mobile=validated_data['mobile'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                email=validated_data['email']
            )
            return user_account
        except IntegrityError:
          raise serializers.ValidationError({"username": "Username already exists."})
        

class BackgroundInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackgroundInformation
        fields = '__all__'

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'

class TradeAssociationMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeAssociationMember
        fields = ['id','name', 'phone_number', 'gender', 'user']

class TradeAssociationSerializer(serializers.ModelSerializer):
    members = TradeAssociationMemberSerializer(many=True)
    class Meta:
        model = TradeAssociation
        fields = ['user','name_of_group', 'website_link', 'is_registered', 'contact_person_name', 'contact_person_phone', 'contact_person_email', 'members']

    def create(self, validated_data):
        courses_data = validated_data.pop('members')
        trade_association = TradeAssociation.objects.create(**validated_data)
        for course_data in courses_data:
           TradeAssociationMember.objects.create(trade_association=trade_association, **course_data)
        return trade_association
    
    
    # def update(self, instance, validated_data):
    #     courses_data = validated_data.pop('courses')
    #     instance.targeted_trade = validated_data.get('targeted_trade', instance.targeted_trade)
    #     instance.reason_for_partnership = validated_data.get('reason_for_partnership', instance.reason_for_partnership)
    #     instance.enterprise_size = validated_data.get('enterprise_size', instance.enterprise_size)
    #     instance.dev_stage = validated_data.get('dev_stage', instance.dev_stage)
    #     instance.track_record = validated_data.get('track_record', instance.track_record)
    #     instance.expertise = validated_data.get('expertise', instance.expertise)
    #     instance.staff_mentoring= validated_data.get('staff_mentoring', instance.staff_mentoring)
    #     instance.infrastructure= validated_data.get('infrastructure', instance.infrastructure)
    #     instance.sector_description= validated_data.get('sector_description', instance.sector_description)
    #     instance.save()

        # Updating the courses
        existing_course_ids = [course.id for course in instance.courses.all()]
        new_course_ids = [course['id'] for course in courses_data if 'id' in course]

        # Delete courses that are not present in the new data
        for course_id in existing_course_ids:
            if course_id not in new_course_ids:
                WorkPlacementCourse.objects.get(id=course_id).delete()

        # Update or create courses
        for course_data in courses_data:
            course_id = course_data.get('id')
            if course_id:
                course = WorkPlacementCourse.objects.get(id=course_id)
                course.sn = course_data.get('sn', course.sn)
                course.course_name = course_data.get('course_name', course.course_name)
                course.duration = course_data.get('duration', course.duration)
                course.save()
            else:
                WorkPlacementCourse.objects.create(trade=instance, **course_data)

        return instance



class WomenEntrepreneurshipPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = WomenEntrepreneurshipPlatform
        fields = '__all__'

