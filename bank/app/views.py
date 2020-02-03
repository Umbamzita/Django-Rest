from .serializers import *
from .models import *
from rest_framework import generics, viewsets, mixins

class CustomerViewSet(viewsets.ModelViewSet):
    
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]


class AccountViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    def perform_create(self, serializer):
        """Create a new account"""
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """Return object for current authenticated user only"""
        return self.queryset.filter(user=self.request.user)


class ActionViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


