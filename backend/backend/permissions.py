from datetime import datetime
from rest_framework import permissions
from custom_user.models import Profile
from application.serializers import ApplicationSerializer
from custom_user.serializers import ProfileSerializer
from backend import settings


class IsSameClub(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = Profile.objects.get(user=request.user)
        application = ApplicationSerializer(obj)
        profile = ProfileSerializer(user)
        return application['club'].value == profile['club'].value


class IsBeforeDue(permissions.BasePermission):
    def has_permission(self, request, view):
        date_time_obj = datetime.strptime(settings.DUE_DATE, '%Y-%m-%d %H:%M')
        return date_time_obj > datetime.now()