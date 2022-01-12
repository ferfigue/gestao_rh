from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'core/index.html', data)