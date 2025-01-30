from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class home(APIView):
    def get(self, request):
        return Response("Hello, World!", status=status.HTTP_200_OK)
    
    def post(self, request):
        try:
            input = int(request.data.get('input'))
            result = self.compute(input)
            return Response(result, status=status.HTTP_200_OK);
        except:
            return Response("POST error", status=status.HTTP_400_BAD_REQUEST)    

    def compute(self, input):
        return input * 2