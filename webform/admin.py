from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(BackgroundInformation)
class BackgroundInformationAdmin(admin.ModelAdmin):
    list_display = ('FullName', 'TelephoneNumber', 'Age', 'Gender', 'MaritalStatus', 'EmailAddress', 'Nationality', 'Ugandan_Identification_Number','Refugee_Number', 'settlement', 'district_city', 'subcounty_division', 'parish_ward', 'village_cell_zone')
    search_fields = ('FullName', 'EmailAddress', 'Nationality')

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_of_establishment', 'sector', 'number_of_employees_male', 'number_of_employees_female', 'total_employees', 'revenue_per_annum', 'location_address')
    search_fields = ('name', 'sector')
    list_filter = ('year_of_establishment', 'sector')

@admin.register(TradeAssociation)
class TradeAssociationAdmin(admin.ModelAdmin):
    list_display = ('name_of_group', 'website_link', 'is_registered', 'contact_person_name', 'contact_person_phone', 'contact_person_email')
    search_fields = ('name_of_group', 'contact_person_name')
    list_filter = ('is_registered',)

@admin.register(TradeAssociationMember)
class TradeAssociationMemberAdmin(admin.ModelAdmin):
    list_display = ('trade_association', 'name', 'phone_number', 'gender')
    search_fields = ('name', 'phone_number')
    list_filter = ('gender', 'trade_association')

@admin.register(WomenEntrepreneurshipPlatform)
class WomenEntrepreneurshipPlatformAdmin(admin.ModelAdmin):
    list_display = ('how_did_you_hear', 'preferred_communication_method', 'involved_in_empowerment', 'confirmed')
    search_fields = ('how_did_you_hear', 'preferred_communication_method')
    list_filter = ('involved_in_empowerment',)
