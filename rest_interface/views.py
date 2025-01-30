from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pynq import Overlay

overlay = Overlay('/home/xilinx/pynq/calculator/design_1_wrapper.bit')
calculator_ip = overlay.calculator_0

class home(APIView):
    def get(self, request):
        return Response("Hello, World!", status=status.HTTP_200_OK)
    
    def post(self, request):
        try:
            input1 = int(request.data.get('input1'))
            input2 = int(request.data.get('input2'))
            operation = str(request.data.get('operation'))
            result = self.compute(input1, input2, operation)
            return Response(result, status=status.HTTP_200_OK);
        except:
            return Response("POST error", status=status.HTTP_400_BAD_REQUEST)    

    def compute(self, input1, input2, operation):
        calculator_ip.write(0x10, input1)
        calculator_ip.write(0x18, input2)

        if operation == '+':
            return calculator_ip.read(0x20)
        elif operation == '-':
            return calculator_ip.read(0x30)
        elif operation == '*':
            return calculator_ip.read(0x40)
        elif operation == '/':
            return calculator_ip.read(0x50)
        else:
            return "Invalid operation"
        