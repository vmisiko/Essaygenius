from django.shortcuts import render, HttpResponse
from django.views import generic
from rest_framework import generics
from .serializers import OrderSerializer, VueOrderSerializer, UploadFileSerializer
from .models import Orders, VueOrders, UploadFiles
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse


# Create your views here.

def index(request):
    return render(request, "index.html", {})

class HomePage(generic.View):

    def get(self, *args, **kwargs):

        context = {

        }


        return render(self.request, "index.html", context)

    def post(self, *args, **kwargs):
        pass

class OrderUpload(generic.CreateView):
    model = Orders
    fields = ["topic", "pages", "style", "subject", "amount", "instructions", "uploads"]
    template_name = "order_Upload.html"


class OrderList(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer




class OrderdetailApi(generics.ListCreateAPIView):
    queryset = VueOrders.objects.all()
    serializer_class = VueOrderSerializer 

    def create(self, request):
        print(request.data)

        deadline = request.data["body"]["deadline"]
        Type = request.data["body"]["type"]
        pages = request.data["body"]["pages"]
        service = request.data["body"]["service"]
        checkbox = request.data["body"]["checkbox"]
        language = request.data["body"]["language"]
        level = request.data["body"]["level"]

        qs = self.queryset.create(
            deadline= deadline,
            Type = Type,
            pages = pages,
            service =service,
            fin_earl = checkbox,
            language = language,
            Level = level   
            
         )


        data = {
            "posted": True,
            "qs": qs.id
        }
        return JsonResponse(data)

class OrderdetaildraftApi(APIView):
    queryset = VueOrders.objects.all()
    serializer_class = VueOrderSerializer 

    def put(self, request, pk):
        print(request.data)

        deadline = request.data["body"]["deadline"]
        Type = request.data["body"]["type"]
        pages = request.data["body"]["pages"]
        service = request.data["body"]["service"]
        checkbox = request.data["body"]["checkbox"]
        language = request.data["body"]["language"]
        level = request.data["body"]["level"]

        qs = self.queryset.get(id=pk)
        qs.qdeadline= deadline
        qs.Type = Type
        qs.pages = pages
        qs.service =service
        qs.fin_earl = checkbox
        qs.language = language  
        qs.Level = level

        qs.save()
            
        data = {
            "posted": True,
            "qs": qs.id
        }
        return JsonResponse(data)


    def get(self, request, pk):

        order = self.queryset.get(id=pk)

        data = {
            "deadline": order.deadline,
            "type": order.Type,
            "pages": order.pages,
            "service": order.service,
            "checkbox": order.fin_earl,
            "language": order.language,
            "level": order.Level
        }
        # data = {"form" : form}

        return JsonResponse(data)
        
    def delete(self, request, pk):
        order = VueOrders.objects.get(id=pk).delete()
        data = {
            "deleted": True
        }
        return JsonResponse(data)

class OrderIntructionsApi(generics.ListCreateAPIView):
    queryset = VueOrders.objects.all()
    serializer_class = VueOrderSerializer 

    def create(self, request, pk):
        print(request.data)

        pk_id = request.data["body"]["id"]
        topic = request.data["body"]["form"]["topic"]
        sources = request.data["body"]["form"]["sources"]
        style = request.data["body"]["form"]["style"]
        subject = request.data["body"]["form"]["subject"]
        instructions = request.data["body"]["form"]["instructions"]

        
        try:

            qs = self.queryset.get(id=pk)
            qs.topic = topic
            qs.sources = sources
            qs.style = style
            qs.subject = subject
            qs.instructions = instructions
            qs.save()
        

            data = {
                "posted": True
            }
        except:

            data = {
                "posted": False
            }

      

        return JsonResponse(data)


    def get(self, request, pk):

        order = self.queryset.get(id=pk)

        data = {
            "topic" :order.Topic,
            "sources" :order.sources,
            "style" :order.style,
            "subject":order.subject,
            "instructions":order.instructions
        }
        # data = {"form" : form}

        return JsonResponse(data)
        
    def delete(self, request, pk):
        order = VueOrders.objects.get(id=pk).delete()
        data = {
            "deleted": true
        }
        return JsonResponse(data)






def serializer(img):
    img_se =  {
        'file':img.files.name,
        'main': img.main
    }
    return img_se

class OrderUploadApi(APIView):
    queryset = UploadFiles.objects.all()

    serializer_class = UploadFileSerializer

    def post(self, request,pk):
        print(request.data)
        data = request.data
        fies = []
        order = VueOrders.objects.get(id=pk)


        file_name = data.keys()

        for img in file_name:
            img = data[img]
            print(img)
            uploads = self.queryset.create(files = img)
            order.files.add(uploads)

        order.save()

        data = {

            "posted": True
        }

        return JsonResponse(data)


    def get(self, request, pk):
        order = VueOrders.objects.get(id=pk)
        images = order.files.all()
        serialized = [serializer(img) for img in images ]
        data = {

            "order" : serialized
        }

        return JsonResponse(data)
        
    def delete(self, request, pk):
        order = VueOrders.objects.get(id=pk).delete()
        data = {
            "deleted": true
        }
        return JsonResponse(data)


