from django.shortcuts import render
from django.views.generic import FormView
from account.forms import LoginForm
from django.contrib.auth import authenticate,login
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
import requests
from requests.auth import HTTPBasicAuth
import os


# Create your views here.

def index_page(request):
    # headers = {
    # 'orgId': '60001280952',
    # 'Authorization': '9446933330c7f886fbdf16782906a9e0',}
    # response = requests.get('https://desk.zoho.in/api/v1/tickets', headers=headers)
    # print("###########3")
    # print(response.json())
    # if response.status_code == 200:
    #     print("Code 200")
    # else:
    #     print("Code not 200")
    headers = {
    'Authorization': 'Zoho-oauthtoken 1000.3d0a155402dbb59f776fd63adb1e67c0.a41ea557a6a8d7e402690098b2056f60s',
}
    data = '{ "subCategory" : "Sub General", "cf" : { "cf_permanentaddress" : null, "cf_dateofpurchase" : null, "cf_phone" : null, "cf_numberofitems" : null, "cf_url" : null, "cf_secondaryemail" : null, "cf_severitypercentage" : "0.0", "cf_modelname" : "F3 2017" }, "productId" : "", "contactId" : "1892000000042032", "subject" : "Real Time analysis Requirement", "dueDate" : "2016-06-21T16:16:16.000Z", "departmentId" : "1892000000006907", "channel" : "Email", "description" : "Hai This is Description", "language" : "English", "priority" : "High", "classification" : "", "assigneeId" : "1892000000056007", "phone" : "1 888 900 9646", "category" : "general", "email" : "carol@zylker.com", "status" : "Open" }'
    response = requests.post('https://desk.zoho.com/api/v1/tickets', headers=headers, data=data)
    print("###########3")
    print(response.json())
    if response.status_code == 200:
        print("Code 200")
    else:
        print("Code not 200")
    return render(request,'main/front/index.html',{})



    
    
