from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet

from urlshortener.models import Link
from urlshortener.serializers import LinkSerializer,CreateLinkSerializer
# Create your views here.



class CreateLink(CreateAPIView):
    queryset = Link.objects.all()
    serializer_class = CreateLinkSerializer
    
    
class LinkViewset(ModelViewSet):
    
    serializer_class = LinkSerializer
    
    def get_queryset(self):
        return Link.objects.filter(owner=self.request.user)
    