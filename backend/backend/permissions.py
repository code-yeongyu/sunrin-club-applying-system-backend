from rest_framework import permissions
from custom_user.models import Profile
from application.serializers import ApplicationSerializer
from custom_user.serializers import ProfileSerializer


class IsSameClub(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = Profile.objects.get(user=request.user)
        application = ApplicationSerializer(obj)
        profile = ProfileSerializer(user)
        return application['club'].value == profile['club'].value