from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_object_or_404
from application.serializers import ApplicationSerializer
from rest_framework import permissions
from backend.permissions import IsSameClub
from backend.permissions import IsBeforeDue
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.views import APIView
from application.models import Application
from custom_user.models import Profile
from custom_user.serializers import ProfileSerializer


def count_applications(data):
    all_numbers = []
    for d in data:
        all_numbers.append(d['number'])
    return len(set(all_numbers))


# get my applications of my club
@api_view(['GET'])
def applications_list(request, ):
    if request.user.is_authenticated:
        user = Profile.objects.get(user=request.user)
        profile = ProfileSerializer(user).data
        applications = Application.objects.filter(club=profile['club'],
                                                  is_hide=False)
        serializer = ApplicationSerializer(applications, many=True)
        dic = {
            "data": serializer.data,
            "length": count_applications(serializer.data)
        }
        return Response(dic, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


# get detailed club info, only allowed to a same club user
class ApplicationDetail(generics.RetrieveDestroyAPIView):
    queryset = Application.objects.filter(is_hide=False)
    serializer_class = ApplicationSerializer
    permission_classes = (IsSameClub, )

    def delete(self, request, *args, **kwargs):
        application = Application.objects.get(pk=kwargs['pk'])
        application.is_hide = True
        application.save()
        return Response(status=status.HTTP_200_OK)


# creating new application
class ApplicationCreation(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (IsBeforeDue, )