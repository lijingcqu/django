# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def login(request):
    if request.method=='GET':
        context = {}
        context['val']="408分队"
        return render(request,'login/index.html',context)
    else:
        username=request.POST.get('username')
        password=request.POST.get('password')
        ajax_response = {"user": None, "errors": ""}
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            ajax_response['user']=user.username
        else:
            ajax_response['errors']='username/password error'

        return HttpResponse(json.dumps(ajax_response))