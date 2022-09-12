from django.shortcuts import render
from .serializers import OrganizationDetails, EmployeesDetails
from .models import Organization,Employees
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q


# Create views files for Organization details.

class OrganizationView(APIView):
    queryset=Organization.objects.all()
    serializer_class=OrganizationDetails

    def post(self,request):
        try:
            data=request.data
            serializer=OrganizationDetails(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Exception as e:
            return Response({'Error':str(e)},status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        try:
            data=request.GET.get('organization_id')
            print(data)
            model=Organization.objects.get(organization_id=data)
            serializer=OrganizationDetails(model,many=False)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error':str(e)},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request):
        try:
            data=request.data
            model=Organization.objects.get(organization_id=data['organization_id'])
            serializer=OrganizationDetails(model,data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Exception as e:
            return Response({'Error':str(e)},status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request):
        try:
            data=request.data
            model=Organization.objects.get(organization_id=data['organization_id'])
            serializer=OrganizationDetails(model,data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
                print(data)
                return Response(serializer.data)
            return Response(serializer.errors)
        except Exception as e:
            return Response({'Error':str(e)},status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request):
        try:
            data=request.data
            model=Organization.objects.filter(organization_id=data['organization_id']).update(is_deleted=True)
            print(model)
            return Response("successfully deleted",content_type='application/json')
        except Exception as e:
            return Response({'Error':str(e)},status=status.HTTP_400_BAD_REQUEST)



# create views file for Employees details

class EmployeesView(APIView):
    queryset=Employees.objects.all()
    serializer_class=EmployeesDetails

    def post(self,request):
        try:
            data=request.data
            serializer=EmployeesDetails(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Exception as e:
            return Response({'Error':str(e)},status=status.HTTP_400_BAD_REQUEST)

    
    def get(self,request):
        try:
            data=request.GET.get('employee_id')
            print(data)
            model=Employees.objects.get(employee_id=data)
            serializer=EmployeesDetails(model,many=False)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error':str(e)},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request):
        try:
            data=request.data
            model=Employees.objects.get(employee_id=data['employee_id'])
            serializer=EmployeesDetails(model,data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Exception as e:
            return Response({'Error':str(e)},status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request):
        try:
            data=request.data
            model=Employees.objects.get(employee_id=data['employee_id'])
            serializer=EmployeesDetails(model,data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
                print(data)
                return Response(serializer.data)
            return Response(serializer.errors)
        except Exception as e:
            return Response({'Error':str(e)},status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request):
        try:
            data=request.data
            model=Employees.objects.filter(employee_id=data['employee_id']).update(is_deleted=True)
            print(model)
            return Response("successfully deleted",content_type='application/json')
        except Exception as e:
            return Response({'Error':str(e)},status=status.HTTP_400_BAD_REQUEST)


#  This API is Additional functions of Organization view

class OrganizationAdditional(APIView):
    queryset=Organization.objects.all()
    serializer_class=OrganizationDetails

    #Filter API
    def post(self,request):
        try:
            data=request.data
            model=Organization.objects.filter(organization_name__contains=data['organization_name'],organization_location__exact=data['organization_location'],number_of_employees__range=data['number_of_employees'],annual_turn_over__range=data['annual_turn_over'],capital_amount__range=data['capital_amount'])
            print(model)
            serializer=OrganizationDetails(model,many=True)
            return Response(serializer.data)

        except Exception as e:
            return Response({'Error':str(e)},status=status.HTTP_400_BAD_REQUEST)

    #List API
    def get(self,request):
        try:
            data=request.GET.get('is_deleted')
            print(data)
            model=Organization.objects.filter(is_deleted__exact=data).order_by('organization_id')
            serializer=OrganizationDetails(model,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error':str(e)},status=status.HTTP_400_BAD_REQUEST)
    
    #Search API
    def put(self,request):
        try:
            data=request.query_params
            model=Organization.objects.filter(Q(organization_name__icontains=data['search'])|Q(organization_location__icontains=data['search']))
            print(model)
            serializer=OrganizationDetails(model,many=True)
            return Response(serializer.data)
            
        except Exception as e:
            return Response({'Error':str(e)},status=status.HTTP_400_BAD_REQUEST)



#  This API is Additional functions of Employee view

class EmployeesAdditional(APIView):
    queryset=Employees.objects.all()
    serializer_class=EmployeesDetails

    #Filter API
    def post(self,request):
        try:
            data=request.data
            model=Employees.objects.filter(organization_id__organization_name__icontains=data['organization_name'],organization_id__organization_location__exact=data['organization_location'],employee_salary__range=data['employee_salary'])
            serializer=EmployeesDetails(model,many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'Error':str(e)},status=status.HTTP_400_BAD_REQUEST)

    #List API
    def get(self,request):
        try:
            data=request.GET.get('is_deleted')
            print(data)
            model=Employees.objects.filter(is_deleted__exact=data).order_by('employee_id')
            serializer=EmployeesDetails(model,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error':str(e)},status=status.HTTP_400_BAD_REQUEST)
    
    #Search API
    def put(self,request):
        try:
            data=request.query_params
            model=Employees.objects.filter(Q(organization_id__organization_name__icontains=data['search'])|Q(organization_id__organization_location__exact=data['search']))
            serializer=EmployeesDetails(model,many=True)
            print(data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'Error':str(e)},status=status.HTTP_400_BAD_REQUEST)

   


