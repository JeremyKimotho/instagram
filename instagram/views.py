from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/register')
def default(request):
  return render(request, 'actual/home.html')


