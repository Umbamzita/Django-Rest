from rest_framework.permissions import IsAuthenticated, AllowAny


class ObjectViewSet:
    queryset = None
    serializer_class = None

    def get_permissions(self):
   
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]