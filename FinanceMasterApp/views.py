from urllib import response
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Asset
from .models import User
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import requests
from requests import Session

 

assetDetailsa = [
    {
        'asset': 'asset1',
        'exchange': 'FinanceMaster',
        'qty': '100',
        'price': '2.00',
        'total': '200.00',
    },
    {
        'asset': 'asset2',
        'exchange': 'Binance',
        'qty': '100',
        'price': '2.00',
        'total': '200.00',
    },
    {
        'asset': 'asset3',
        'exchange': 'Hargreaves Lansdown',
        'qty': '100',
        'price': '5.00',
        'total': '500.00',
    },

]


# Views
@login_required
def index(request):
    context = {
        
        'assetDetails': Asset.objects.filter(user=request.user)
    }
    return render(request,'FinanceMasterApp/index.html',  context)



#Delete User
class UserDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = User
    context_object_name = 'user'
    success_url = '/'
    

    def test_func(self):
        user = self.get_object()
        if self.request.user == user.user:
            return True
        return False


#Add Asset
class AssetCreateView(LoginRequiredMixin,CreateView):
    model = Asset
    fields = ['asset', 'exchange', 'qty', 'price']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#Show detail of Asset
class AssetDetailView(DetailView):
    model = Asset
    context_object_name = 'asset'
    template_name = 'FinanceMasterApp/asset.html'

#Update Asset
class AssetUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Asset
    fields = ['asset', 'exchange', 'qty', 'price']
    template_name = 'FinanceMasterApp/updateasset.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        asset = self.get_object()
        if self.request.user == asset.user:
            return True
        return False

#Delete Asset
class AssetDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Asset
    context_object_name = 'asset'
    success_url = '/'
    

    def test_func(self):
        asset = self.get_object()
        if self.request.user == asset.user:
            return True
        return False

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} Registered! Please Login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'FinanceMasterApp/register.html', {'form': form})

def login(request):
    return render(request, 'FinanceMasterApp/login.html')

@login_required
def profile(request):
    return render(request, 'FinanceMasterApp/profile.html')

def cryptodata(request):
    paramaters = {
        'slug': 'bitcoin,ethereum,maker,bnb,bitcoin-cash',
        'skip_invalid': 'false',      
        'convert': 'GBP',
        'aux': 'cmc_rank'
    }
    headers = {
        'Accept-Encoding': 'true',
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '3557c2b2-c325-4ce3-9cc6-7c0632448e43'
    }
    

    responseB=requests.get('https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest', headers=headers ,params=paramaters).json()['data']['1']['quote']['GBP']['price']
    responseC=requests.get('https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest', headers=headers ,params=paramaters).json()['data']['1027']['quote']['GBP']['price']
    responseD=requests.get('https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest', headers=headers ,params=paramaters).json()['data']['1518']['quote']['GBP']['price']
    responseE=requests.get('https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest', headers=headers ,params=paramaters).json()['data']['1839']['quote']['GBP']['price']
    responseF=requests.get('https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest', headers=headers ,params=paramaters).json()['data']['1831']['quote']['GBP']['price']
    

  
    return render(request,'FinanceMasterApp/cryptodata.html', {'responseB':responseB,'responseC':responseC,'responseD':responseD,'responseE':responseE,'responseF':responseF })
 
 
 
