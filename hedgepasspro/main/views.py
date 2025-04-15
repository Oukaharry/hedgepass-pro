from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.http import JsonResponse
from .forms import CustomUserCreationForm, AccountPairForm
from .models import AccountPair
from .models import MT5Account
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm


def index(request):
    return render(request, 'main/landing.html')  

def landing(request):
    """Landing page view"""
    return render(request, 'main/landing.html')  # Keep existing template

def dashboard(request):
    """Dashboard view (previous index)"""
    return render(request, 'main/landing.html')


@login_required
def add_account(request):
    if request.method == 'POST':
        try:
            account = MT5Account(
                user=request.user,
                account_type=request.POST.get('account_type'),
                account_number=request.POST.get('account_number'),
                password=request.POST.get('password'),  # Will be encrypted in save()
                server=request.POST.get('server'),
                pair_number=request.POST.get('pair_number')
            )
            account.save()
            return redirect('landing')
        except Exception as e:
            return render(request, 'hedgepasspro/add_account.html', {
                'error': str(e)
            })
    
    return render(request, 'hedgepasspro/add_account.html')

@login_required
def view_pairs(request):
    accounts = MT5Account.objects.filter(user=request.user).order_by('pair_number')
    return render(request, 'hedgepasspro/pairs.html', {
        'accounts': accounts,
        'pair_range': range(1, 11)  # For 10 possible pairs
    })

def landing(request):
    return render(request, 'main/landing.html')

def login_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('client_area')
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/signup.html', {'form': form})


@login_required
def client_area(request):
    pairs = AccountPair.objects.filter(user=request.user, is_active=True)
    return render(request, 'main/client_area.html', {'pairs': pairs})

@login_required
def account_management(request):
    if request.method == 'POST':
        form = AccountPairForm(request.POST)
        if form.is_valid():
            pair = form.save(commit=False)
            pair.user = request.user
            pair.save()
            return redirect('account_management')
    else:
        form = AccountPairForm()
    
    pairs = AccountPair.objects.filter(user=request.user)
    return render(request, 'main/account_management.html', {
        'form': form,
        'pairs': pairs
    })

# Keep other views (performance, portfolio_performance, settings) unchanged
@login_required
def performance(request, pair_id):
    try:
        pair = AccountPair.objects.get(id=pair_id, user=request.user)
        context = {
            'pair': pair,
            'live_pl': 5240.50,          # Replace with actual data
            'hedge_pl': -4980.25,        # Replace with actual data
            'live_daily_pl': 320.75,     # Replace with actual data
            'hedge_daily_pl': -295.40,   # Replace with actual data
            'live_win_rate': 72.0,       # Replace with actual data
            'hedge_win_rate': 68.0,      # Replace with actual data
            'active_trades': []          # Replace with actual data
        }
    except AccountPair.DoesNotExist:
        context = {'pair': None}
    
    return render(request, 'main/performance.html', context)

@login_required
def portfolio_performance(request):
    pairs = AccountPair.objects.filter(user=request.user, is_active=True)
    return render(request, 'main/portfolio_performance.html', {'pairs': pairs})

@login_required
def settings(request):
    return render(request, 'main/settings.html')

@login_required
def delete_account(request):
    if request.method == 'POST':
        # Logic to delete the user's account
        request.user.delete()
        return JsonResponse({'message': 'Account deleted successfully'}, status=200)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def custom_logout(request):
    logout(request)
    return redirect('landing')  # Redirect to the landing page after logout