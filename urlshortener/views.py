from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.throttling import UserRateThrottle

from urlshortener.models import Link
from urlshortener.serializers import LinkSerializer,CreateLinkSerializer
from django.shortcuts import redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.



# class CreateLink(CreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Link.objects.all()
#     serializer_class = CreateLinkSerializer
    
class CreateLink(CreateAPIView):
    
    permission_classes = [IsAuthenticated]
    queryset = Link.objects.all()
    serializer_class = CreateLinkSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        link = serializer.save()

        return Response(
            LinkSerializer(link).data,
            status=status.HTTP_201_CREATED
        )
    
    
class LinkViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LinkSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Link.objects.all()
        return Link.objects.filter(owner=user)


class RedirectViewset(APIView):
    throttle_classes = [UserRateThrottle]
    def get(self, request, short_code):
        link = get_object_or_404(Link, short_code=short_code)
        if link.is_Valid():
            link.clicks_count += 1
            link.save()
            return redirect(link.original_url, permanent=False)
        else:
            return Response({"error": "This link is inactive or expired."}, status=400)
       
    