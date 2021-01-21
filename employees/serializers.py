from rest_framework import serializers

from .models import Employee



class EmployeeSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)
    sex_full = serializers.CharField(source='get_sex_display', read_only=True)
    role_name = serializers.CharField(source='role.full_name', read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'username', 'last_name', 'first_name', 'middle_name', 'sex',
        'sex_full', 'birthday', 'pass_series', 'pass_number', 'inn', 'email', 'address', 'phone',
        'active', 'role', 'role_name']

    def get_username(self, obj):
        return obj.user.username