from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Client
from .serializers import ClientSerializer


class ClientApiView(GenericAPIView):
    queryset = Client.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ClientSerializer

    def get(self, request, *args, **kwargs):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'phone_number': request.data.get('phone_number'), 
            'mobile_operator_code': request.data.get('mobile_operator_code'), 
            'tags': request.data.get('tags'), 
            'timezone': request.data.get('timezone')
        }
        serializer = ClientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetailApiView(GenericAPIView):
    queryset = Client.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ClientSerializer

    def get_object(self, client_id):
        try:
            return Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return None

    def get(self, request, client_id, *args, **kwargs):
        client_instance = self.get_object(client_id)
        if not client_instance:
            return Response(
                {"res": "Object with client id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = ClientSerializer(client_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, client_id, *args, **kwargs):
        client_instance = self.get_object(client_id)
        if not client_instance:
            return Response(
                {"res": "Object with client id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {}
        instance_fields = ['phone_number', 'mobile_operator_code', 'tags', 'timezone']
        for field in instance_fields:
            if request.data.get(field) is not None:
                data[field] = request.data.get(field)
        serializer = ClientSerializer(instance=client_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, client_id, *args, **kwargs):
        client_instance = self.get_object(client_id)
        if not client_instance:
            return Response(
                {"res": "Object with client id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        client_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

