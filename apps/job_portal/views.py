from rest_framework.response import Response
from rest_framework.views import APIView


class ApiView(APIView):
    def get(self, request, format=None):
        api_list = {"home": "http://127.0.0.1:8000/"}
        return Response(api_list)
