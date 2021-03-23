from .serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import connection

def executeSQL(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

class SignUpViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    # override get_queryset or create queryset
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    def create(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        email = request.data.get('email', None)
        firstname = request.data.get('firstname', None)
        lastname = request.data.get('lastname', None)

        # sql = "SELECT * FROM User_user WHERE username = {};".format(username)
        # res = executeSQL(sql)

        try:
            user = User.objects.raw('SELECT * FROM User_user where username = %s', [username])
            #user = User.objects.get(username=username)

        except User.DoesNotExist:
            instance = User.objects.raw('Update User_user SET username = %s, password = %s, email = %s, firstname = %s, lastname = %s', [username, password, email. firstname, lastname])
            #instance = User(username=username, password=password, email=email, firstname=firstname, lastname=lastname)
            instance.save()
            return Response({"response": {"error":"OK", "id": instance.id, "username": instance.username, "email":instance.email, "password":instance.password, "firstname":instance.firstname, "lastname":instance.lastname}, "status": 201}, status=status.HTTP_201_CREATED)
        else:

            return Response({"response": {"error":"User name already exists."}, "status": 400}, status=status.HTTP_400_BAD_REQUEST)
