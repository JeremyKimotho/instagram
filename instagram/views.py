from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .forms import SignUpForm, NewPostForm
from .tokens import account_activation_token
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Image, Profile
from django.core.urlresolvers import reverse


@login_required(login_url='/accounts/register')
def default(request):
  posts = Image.get_images()
  return render(request, 'actual/home.html', {'posts':posts})

def signup(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.is_active = False
      user.save()
      current_site = get_current_site(request)
      subject = 'Activate Your Instagram Account'
      message = render_to_string('email/email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
      })
      user.email_user(subject, message)
      return redirect('home')
  else:
    form = SignUpForm()
  return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
  try:
    uid = force_text(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)
  except (TypeError, ValueError, OverflowError, User.DoesNotExist):
    user = None

  if user is not None and account_activation_token.check_token(user, token):
    user.is_active = True
    user.profile.email_confirmed = True
    user.save()
    login(request, user)
    return redirect('home')
  else:
    return render(request, 'account_activation_invalid.html')

@login_required(login_url='/accounts/register/')
def new_post(request):
  current_user = request.user
  if request.method == 'POST':
    form=NewPostForm(request.POST, request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      post.profile = current_user
      post.save_image()
    return redirect('home')
  else:
    form=NewPostForm()
  return render(request, 'actual/new_post.html', {'form': form})

@login_required(login_url='/accounts/register/')
def search(request):
  if 'user' in request.GET and request.GET['user']:
    search_term = request.GET.get('user')
    searched_users = Profile.search_profile(search_term)
    return render(request, 'actual/search.html', {'users':searched_users})

  else: 
    return render(request, 'actual/search.html')

@login_required(login_url='/accounts/register/')
def profile(request, id):
  profile = get_object_or_404(User, pk=id)
  images = profile.posts.all()
  return render(request, 'actual/profile.html', {'profile':profile, 'images':images})

@login_required(login_url='/accounts/register/')
@require_POST
def like(request):
  print('The first part')
  if request.method == 'POST':
    user = request.user
    slug = request.POST.get('slug', None)
    post = get_object_or_404(Image, slug=slug)

    if post.likes.filter(id=user.id).exists():
      post.likes.remove(user)
    else:
      post.likes.add(user)

  info = {'likes_count':post.get_likes()}
  return HttpResponse(json.dumps(info), content_type='application/json')