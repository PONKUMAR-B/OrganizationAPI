from django.test import TestCase
from employeeapp.models import Organization,Employees
from employeeapp.serializers import OrganizationDetails,EmployeesDetails
from employeeapp.views import OrganizationAdditional, OrganizationView,EmployeesView,EmployeesAdditional


# Create your Organization tests here.
class OrganizationTest(TestCase):
    def setUp(self):
        Organization.objects.create(
            organization_id=3,start_date="1995-03-11",organization_name= "Dr.SA College Of Engineering",organization_address= {"Door no": 94,"Street": "Tisaiyanvilai main road","City": "Tuticorin","State": "Tamilnadu","Country": "India"},organization_location= "Tiruchendur",number_of_employees= 70,annual_turn_over= 30000000,capital_amount= 925000,is_deleted= True)

        Organization.objects.create(
            organization_id=50,start_date="1995-03-11",organization_name= "Dr.SA College Of Engineering",organization_address= {"Door no": 94,"Street": "Tisaiyanvilai main road","City": "Tuticorin","State": "Tamilnadu","Country": "India"},organization_location= "Tiruchendur",number_of_employees= 70,annual_turn_over= 30000000,capital_amount= 925000,is_deleted= True)

        Organization.objects.create(
            organization_id=60,start_date="1995-03-11",organization_name= "Dr.SA College Of Engineering",organization_address= {"Door no": 94,"Street": "Tisaiyanvilai main road","City": "Tuticorin","State": "Tamilnadu","Country": "India"},organization_location= "Tiruchendur",number_of_employees= 70,annual_turn_over= 30000000,capital_amount= 925000,is_deleted= True)

        

    # creating a post request for test cases  
    def test_organization_post_status_200(self):
        org=OrganizationView.post(self,request={
                "organization_id": 2,
                "start_date": "1995-03-11",
                "organization_name": "Dr.SA College Of Engineering",
                "organization_address": {
                    "Door no": 94,
                    "Street": "Tisaiyanvilai main road",
                    "City": "Tuticorin",
                    "State": "Tamilnadu",
                    "Country": "India"
                },
                "organization_location": "Tiruchendur",
                "number_of_employees": 70,
                "annual_turn_over": 30000000,
                "capital_amount": 925000,
                "is_deleted": True
            })
        self.assertEqual(org.status_code,200)
    
    def test_organization_post_status1_400(self):
        org=OrganizationView.post(self,request={
               
                "start_date": "1995-03-11",
                "organization_name": "Dr.SA College Of Engineering",
                "organization_address": {
                    "Door no": 94,
                    "Street": "Tisaiyanvilai main road",
                    "City": "Tuticorin",
                    "State": "Tamilnadu",
                    "Country": "India"
                },
                "organization_location": "Tiruchendur",
                "number_of_employees": 70,
                "annual_turn_over": 30000000,
                "capital_amount": 925000,
                "is_deleted": True
            })
        self.assertEqual(org.status_code,400)

    def test_organization_post_status2_400(self):
        org=OrganizationView.post(self,request="")
        self.assertEqual(org.status_code,400)
    
    # creating a get request status
    def test_organization_get_status_200(self):
        org=OrganizationView.get(self,request=50)
        self.assertEqual(org.status_code,200)

    def test_organization_status1_400(self):
        org=OrganizationView.get(self,request="")
        self.assertEqual(org.status_code,400)

    # creating a put request status
    def test_organization_status_200(self):
        org=OrganizationView.put(self,request={
                "organization_id": 60,
                "start_date": "1995-03-11",
                "organization_name": "Dr.SA College Of Engineering",
                "organization_address": {
                    "Door no": 94,
                    "Street": "Tisaiyanvilai main road",
                    "City": "Tuticorin",
                    "State": "Tamilnadu",
                    "Country": "India"
                },
                "organization_location": "Tiruchendur",
                "number_of_employees": 70,
                "annual_turn_over": 30000000,
                "capital_amount": 925000,
                "is_deleted": True
            })
        self.assertEqual(org.status_code,200)

    # def test_organization_status1_400(self):
    #     org=OrganizationView.put(self,request={
               
    #             "start_date": "1995-03-11",
    #             "organization_name": "Dr.SA College Of Engineering",
    #             "organization_address": {
    #                 "Door no": 94,
    #                 "Street": "Tisaiyanvilai main road",
    #                 "City": "Tuticorin",
    #                 "State": "Tamilnadu",
    #                 "Country": "India"
    #             },
    #             "organization_location": "Tiruchendur",
    #             "number_of_employees": 70,
    #             "annual_turn_over": 30000000,
    #             "capital_amount": 925000,
    #             "is_deleted": True
    #         })
    #     self.assertEqual(org.status_code,400)

    def test_organization_status2_400(self):
        org=OrganizationView.put(self,request="")
        self.assertEqual(org.status_code,400)

    # creating a patch request test status
    def test_organization_status_200(self):
        org=OrganizationView.patch(self,request={
                "organization_id": 3,
                "organization_location": "Tiruchendur",
                "number_of_employees": 70,
                "annual_turn_over": 30000000,
                "capital_amount": 925000
            })
        self.assertEqual(org.status_code,200)
    
    # def test_organization_status1_400(self):
    #     org=OrganizationView.patch(self,request={

    #             "organization_location": "Tiruchendur",
    #             "number_of_employees": 70,
    #             "annual_turn_over": 30000000,
    #             "capital_amount": 925000
    #         })
    #     self.assertEqual(org.status_code,400)

    def test_organization_status2_400(self):
        org=OrganizationView.patch(self,request="")
        self.assertEqual(org.status_code,400)


    # creating a delete request test status
    def test_organization_status_200(self):
        org=OrganizationView.delete(self,request={"organization_id":60})
        self.assertEqual(org.status_code,200)

    def test_organization_status1_400(self):
        org=OrganizationView.delete(self,request="")
        self.assertEqual(org.status_code,400)





# create your employee test cases
class EmployeeTest(TestCase):
    def setUp(self):
        Organization.objects.create(
            organization_id=3,start_date="1995-03-11",organization_name= "Dr.SA College Of Engineering",organization_address= {"Door no": 94,"Street": "Tisaiyanvilai main road","City": "Tuticorin","State": "Tamilnadu","Country": "India"},organization_location= "Tiruchendur",number_of_employees= 70,annual_turn_over= 30000000,capital_amount= 925000,is_deleted= True)

        Employees.objects.create(
            employee_id= 8,join_date= "2022-09-08T11:38:19Z",employee_name= "ramesh",employee_department= "csc",employee_address= {"Door no": 38,"Street": "madurai bypass","City": "Tirunelveli","State": "Tamilnadu","Country": "India"},employee_salary= 28000,designation= "assistant professor",is_deleted=False,organization_id= Organization.objects.get(organization_id=3))

        Employees.objects.create(
            employee_id=9,join_date="2022-09-08T11:38:19Z",employee_name="suresh",employee_department="civil",employee_address={"Door no": 38,"Street": "madurai bypass","City": "Tirunelveli","State": "Tamilnadu","Country": "India"},employee_salary=25000,designation="assistant professor",is_deleted=False,organization_id=Organization.objects.get(organization_id=3)
        )

        Employees.objects.create(
            employee_id=10,join_date= "2022-09-08T11:38:19Z",employee_name= "ramesh",employee_department= "csc",employee_address= {"Door no": 38,"Street": "madurai bypass","City": "Tirunelveli","State": "Tamilnadu","Country": "India"},employee_salary= 28000,designation= "assistant professor",is_deleted=False,organization_id= Organization.objects.get(organization_id=3))            

    # creating a post request test cases
    def test_employee_status_200(self):
        org=EmployeesView.post(self,request={
                    "employee_id": 12,
                    "join_date": "2022-09-08T11:38:19Z",
                    "employee_name": "ramesh",
                    "employee_department": "csc",
                    "employee_address": {
                        "Door no": 38,
                        "Street": "madurai bypass",
                        "City": "Tirunelveli",
                        "State": "Tamilnadu",
                        "Country": "India"
                    },
                    "employee_salary": 28000,
                    "designation": "assistant professor",
                    "is_deleted": False,
                    "organization_id": 3
                })
        print(org)
        self.assertEqual(org.status_code,200)

    def test_employee_status1_400(self):
        org=EmployeesView.post(self,request={
        
                    "join_date": "2022-09-08T11:38:19Z",
                    "employee_name": "ramesh",
                    "employee_department": "csc"
                })
        print(org)
        self.assertEqual(org.status_code,400)

    def test_employee_status2_400(self):
        org=EmployeesView.post(self,request="")
        print(org)
        self.assertEqual(org.status_code,400)

    # creating a get request test cases
    def test_employee_status_200(self):
        org=EmployeesView.get(self,request=10)
        print(org)
        self.assertEqual(org.status_code,200)

    def test_employee_status1_400(self):
        org=EmployeesView.get(self,request=33)
        print(org)
        self.assertEqual(org.status_code,400)

    # creating a put request test cases
    def test_employee_status_200(self):
        org=EmployeesView.put(self,request={
                    "employee_id": 8,
                    "join_date": "2022-09-08T11:38:19Z",
                    "employee_name": "ramesh",
                    "employee_department": "csc",
                    "employee_address": {
                        "Door no": 38,
                        "Street": "madurai bypass",
                        "City": "Tirunelveli",
                        "State": "Tamilnadu",
                        "Country": "India"
                    },
                    "employee_salary": 28000,
                    "designation": "assistant professor",
                    "is_deleted": True,
                    "organization_id": 3
                })
        self.assertEqual(org.status_code,200)

    # def test_employee_status1_400(self):
    #     org=EmployeesView.put(self,request={
        
    #                 "join_date": "2022-09-08T11:38:19Z",
    #                 "employee_name": "Ramesh",
    #                 "employee_department": "csc",
    #                 "employee_address": {
    #                     "Door no": 38,
    #                     "Street": "madurai bypass",
    #                     "City": "Tirunelveli",
    #                     "State": "Tamilnadu",
    #                     "Country": "India"
    #                 },
    #                 "employee_salary": 28000,
    #                 "designation": "assistant professor",
    #                 "is_deleted": True,
    #                 "organization_id": 3
    #             })
    #     self.assertEqual(org.status_code,400)

    def test_employee_status2_400(self):
        org=EmployeesView.put(self,request="")
        self.assertEqual(org.status_code,400)

    # creating a patch request test cases
    def test_employee_status_200(self):
        org=EmployeesView.patch(self,request= {
                    "employee_id": 9,
                    "join_date": "2022-09-08T11:38:19Z",
                    "employee_name": "suresh",
                    "employee_department": "civil"
                })
        self.assertEqual(org.status_code,200)

    # def test_employee_status1_400(self):
    #     org=EmployeesView.patch(self,request= {

    #                     "join_date": "2022-09-08T11:38:19Z",
    #                     "employee_name": "ramesh",
    #                     "employee_department": "csc"
    #             })
    #     self.assertEqual(org.status_code,400)

    def test_employee_status2_400(self):
        org=EmployeesView.patch(self,request="")
        self.assertEqual(org.status_code,400)


    # creating a delete request test cases
    def test_employee_status_200(self):
        org=EmployeesView.delete(self,request={"employee_id":3})
        self.assertEqual(org.status_code,200)

    def test_employee_status1_400(self):
        org=EmployeesView.delete(self,request='')
        self.assertEqual(org.status_code,400)




# create a organization additional test cases
class OrganizationAdditionalTest(TestCase):
    def setUp(self):
        print("ok")
        Organization.objects.create(
            organization_id=3,start_date="1995-03-11",organization_name= "Dr.SA College Of Engineering",organization_address= {"Door no": 94,"Street": "Tisaiyanvilai main road","City": "Tuticorin","State": "Tamilnadu","Country": "India"},organization_location= "Tiruchendur",number_of_employees= 70,annual_turn_over= 30000000,capital_amount= 925000,is_deleted= True)

    # for Filter API
    def test_organization_additional_post_status_200(self):
        org=OrganizationAdditional.post(self,request={
                    "start_date": "1995-03-11",
                    "organization_name": "Dr.SA College Of Engineering",
                    "organization_location": "Tiruchendur",
                    "number_of_employees":[0,70],
                    "annual_turn_over":[0,30000000],
                    "capital_amount": [0,925000]
                })
        self.assertEqual(org.status_code,200)

    def test_organization_additional_post_status1_400(self):
        org=OrganizationAdditional.post(self,request={ })
        self.assertEqual(org.status_code,400)

    # for List API
    def test_organization_additional_get_status_200(self):
        org=OrganizationAdditional.get(self,request=True)
        self.assertEqual(org.status_code,200)

    def test_organization_additional_get_status1_400(self):
        org=OrganizationAdditional.get(self,request={ })
        self.assertEqual(org.status_code,400)

    # for Search API
    def test_organization_additional_put_status_200(self):
        org=OrganizationAdditional.put(self,request={"search":'Tiruchendur'})
        self.assertEqual(org.status_code,200)

    def test_organization_additional_put_status1_400(self):
        org=OrganizationAdditional.put(self,request={ })
        self.assertEqual(org.status_code,400)




# create a employee additional test cases
class EmployeesAdditionalTest(TestCase):
    def setUp(self):
        print("ok")
        Organization.objects.create(
            organization_id=3,start_date="1995-03-11",organization_name= "Dr.SA College Of Engineering",organization_address= {"Door no": 94,"Street": "Tisaiyanvilai main road","City": "Tuticorin","State": "Tamilnadu","Country": "India"},organization_location= "Tiruchendur",number_of_employees= 70,annual_turn_over= 30000000,capital_amount= 925000,is_deleted= True)

        Employees.objects.create(
            employee_id= 12,join_date= "2022-09-08T11:38:19Z",employee_name= "ramesh",employee_department= "csc",employee_address= {"Door no": 38,"Street": "madurai bypass","City": "Tirunelveli","State": "Tamilnadu","Country": "India"},employee_salary= 28000,designation= "assistant professor",is_deleted=False,organization_id= Organization.objects.get(organization_id=3))

    # for Filter API
    def test_employees_additional_post_status_200(self):
        org=EmployeesAdditional.post(self,request={
                    "organization_name": "Dr.SA College of Engineering",
                    "organization_location": "Tiruchendur",
                    "join_date": "2022-09-08T11:38:19Z",
                    "employee_salary": [0,30000]
                })
        self.assertEqual(org.status_code,200)

    def test_employees_additional_post_status1_400(self):
        org=EmployeesAdditional.post(self,request={ })
        self.assertEqual(org.status_code,400)

    # for List API
    def test_employees_additional_get_status_200(self):
        org=EmployeesAdditional.get(self,request=False)
        self.assertEqual(org.status_code,200)

    def test_employees_additional_get_status1_400(self):
        org=EmployeesAdditional.get(self,request={ })
        self.assertEqual(org.status_code,400)

    # for Search API
    def test_employees_additional_put_status_200(self):
        org=EmployeesAdditional.put(self,request={"search":'Tiruchendur'})
        self.assertEqual(org.status_code,200)

    def test_employees_additional_put_status1_400(self):
        org=EmployeesAdditional.put(self,request={ })
        self.assertEqual(org.status_code,400)