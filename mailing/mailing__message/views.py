from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, permissions
from datetime import datetime, timedelta
from .models import Message
from .serializers import MessageSerializer
from scheduler import scheduler


class MessageApiView(GenericAPIView):
    queryset = Message.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MessageSerializer

    def retry_sending(instance):
        run_date = datetime.utcnow() + timedelta(seconds=25)
        run_date = run_date.strftime("%Y-%m-%d %H:%M:%S")
        scheduler.Scheduler(instance_id=instance.id, run_date=run_date, task_id="task_2")

    def get(self, request, *args, **kwargs):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'sending_date': request.data.get('sending_date'), 
            'sending_status': request.data.get('sending_status'), 
            'mailing': request.data.get('mailing'), 
            'client': request.data.get('client')
        }
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageDetailApiView(GenericAPIView):
    queryset = Message.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MessageSerializer

    def get_object(self, message_id):
        try:
            return Message.objects.get(id=message_id)
        except Message.DoesNotExist:
            return None

    def get(self, request, message_id, *args, **kwargs):
        message_instance = self.get_object(message_id)
        if not message_instance:
            return Response(
                {"res": "Object with message id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = MessageSerializer(message_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, message_id, *args, **kwargs):
        message_instance = self.get_object(message_id)
        if not message_instance:
            return Response(
                {"res": "Object with message id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {}
        instance_fields = ['sending_date', 'sending_status', 'mailing', 'client']
        for field in instance_fields:
            if request.data.get(field) is not None:
                data[field] = request.data.get(field)
        serializer = MessageSerializer(instance=message_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, message_id, *args, **kwargs):
        message_instance = self.get_object(message_id)
        if not message_instance:
            return Response(
                {"res": "Object with message id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        message_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

