from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def welcome(request):
  return render(request, 'welcome.html')
