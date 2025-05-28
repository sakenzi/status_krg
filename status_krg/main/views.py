from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from drf_yasg.utils import swagger_auto_schema
from .serializers import *

# Create your views here.

class InformationView(generics.ListAPIView):

    @swagger_auto_schema(
        operation_description="Получение информаций",
        responses={200: InformationSerializer(many=True)}
    )
    def get(self, request):
        information = Information.objects.all()
        serializer = InformationSerializer(information, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class TypeActivityView(generics.ListAPIView):

    @swagger_auto_schema(
        operation_description="Получение типов деятельности",
        responses={200: TypeActivitySerializer(many=True)}
    )
    def get(self, request):
        type_activity = TypeActivity.objects.all()
        serializer = TypeActivitySerializer(type_activity, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ActivityView(generics.ListAPIView):
    serializer_class = ActivitySerializer

    @swagger_auto_schema(
        operation_description="получение деятельности по id типа деятельности",
        responses={200: ActivitySerializer(many=True)}
    )
    def get_queryset(self):
        type_activity_id = self.kwargs.get('type_activity_id')
        try:
            type_activity = TypeActivity.objects.get(id=type_activity_id)
        except TypeActivity.DoesNotExist:
            raise NotFound("Такого типа нету")
        return Activity.objects.filter(type_activity=type_activity)
    

class RepairView(generics.ListAPIView):

    @swagger_auto_schema(
        operation_description="Получение о информаций ремонта",
        responses={200: RepairSerializer(many=True)}
    )
    def get(self, request):
        repair = Repair.objects.all()
        serializer = RepairSerializer(repair, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CertificateView(generics.ListAPIView):

    @swagger_auto_schema(
        operation_description="Получение сертификатов",
        responses={200: CertificateSerializer(many=True)}
    )
    def get(self, request):
        certificate = Certificate.objects.all()
        serializer = CertificateSerializer(certificate, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ProjectView(generics.ListAPIView):

    @swagger_auto_schema(
        operation_description="Получение проектов",
        responses={200: ProjectSerialiazer(many=True)}
    )
    def get(self, request):
        project = Project.objects.all()
        serializer = ProjectSerialiazer(project, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class FeedbackView(generics.ListCreateAPIView):
    serializer_class = FeedBackSerializer

    @swagger_auto_schema(
        operation_description="Добавление сообщений",
        responses={200: FeedBackSerializer(many=True)}
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            feed_back = serializer.save()
            return Response(self.serializer_class(feed_back).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LinkView(generics.ListAPIView):
    
    @swagger_auto_schema(
        operation_description="Получение ссылок",
        responses={200: LinkSerializer(many=True)}
    )
    def get(self, request):
        link = Link.objects.all()
        serializer = LinkSerializer(link, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 