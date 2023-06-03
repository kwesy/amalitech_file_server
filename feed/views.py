from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.core.mail import EmailMessage
from documents.models import Document
from users_profile.models import UserProfile
import mimetypes
from .forms import UserForm



User = get_user_model()


def home(request):
    return render(request, 'feed.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        password1 = request.POST['password2']
        email = request.POST['email']


        if password != password1:
            messages.error(request, 'password doesn\'t match')
            redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password, email=email)
        user.is_active = False
        user.save()

        user_profile = UserProfile.objects.create(user=user)
        user_profile.generate_verification_token()

        current_site = get_current_site(request)
        mail_subject = 'Activate your account'
        message = render_to_string('account/activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        to_email = email
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()

        messages.success(request, 'Account created successfully. Please check your email for activation.')
        return redirect('login')

    return render(request, 'account/signup.html')



def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your account has been activated. You can now log in.')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link.')
        return redirect('signup')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')

    return render(request, 'account/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def feed(request):
    search_query = request.GET.get('search', '')

    if search_query:
        documents = Document.objects.filter(target_users__id=request.user.id,title__icontains=search_query)
    else:
        documents = Document.objects.filter(target_users__id=request.user.id)
        
    context = {
        'documents': documents,
        'search_query': search_query,
    }
    return render(request, 'feed.html', context)


@login_required
def search(request):
    query = request.GET.get('query', '')
    documents = Document.objects.filter(title__icontains=query)
    return render(request, 'search.html', {'documents': documents})


@login_required
def preview(request, document_id):
    document = get_object_or_404(Document, target_users__id =request.user.id, id=document_id)
    return render(request, 'preview.html', {'document': document})

@login_required
def downloads(request, document_id):
    document = get_object_or_404(Document, target_users__id =request.user.id, id=document_id)
    document.num_downloads += 1
    document.save()
    return JsonResponse({'document':document.id, 'd':document.num_downloads})


@login_required
def send_email(request, document_id):
    file = get_object_or_404(Document,id=document_id, target_users__id =request.user.id)
    if request.method == 'POST':
        recipient_email = request.POST['email']
        subject = f"File: {file.title}"
        content_type = mimetypes.guess_type(file.file.name)
        email = EmailMessage(
            subject,
            'Please find the attached file: ' + file.title,
            to=[recipient_email],
        )

        email.attach(file.file.name, file.file.read(), content_type[0])
        email.send()
        file.num_emails_sent += 1
        file.save()
        messages.success(request, 'Email sent successfully.')
        return redirect('feed')

    return render(request, 'send_email.html', {'document': file})


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserForm(instance=user)
    return render(request, 'account/profile.html', {'user': user, 'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'account/change_password.html', {'form': form})