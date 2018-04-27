from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'django-rest-framework', 'url': 'http://pypi.python.org/pypi/django-rest-framework/0.1.0'},
	{'name':'askbot', 'url': 'http://pypi.python.org/pypi/askbot/0.10.2'},
	{'name':'django-allauth', 'url': 'http://pypi.python.org/pypi/django-allauth/0.34.0'},
    ]
    context = {
        'title': 'anand-crowdbotics-139',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
