from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_object_or_404
from application.serializers import ApplicationSerializer
from rest_framework import permissions
from backend.permissions import IsSameClub
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.views import APIView
from application.models import Application
from custom_user.models import Profile
from custom_user.serializers import ProfileSerializer


# get
@api_view(['GET'])
def applications_list(request, ):
    if request.user.is_authenticated:
        user = Profile.objects.get(user=request.user)
        profile = ProfileSerializer(user).data
        applications = Application.objects.filter(club=profile['club'])
        serializer = ApplicationSerializer(applications, many=True)
        dic = {"data": serializer.data}
        return Response(dic, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


# get detailed club info, only allowed to a same club user
class ApplicationDetail(generics.RetrieveDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (IsSameClub, )


# creating new application
class ApplicationCreation(generics.CreateAPIView, APIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (permissions.AllowAny, )