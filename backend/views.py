from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.conf import settings
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_protect
from google.oauth2 import id_token
from google.auth.transport import requests
# import requests

import json

from .externals.libs.datagenerator import main as dg
from .models import User


def test(request, *args, **kwargs):
    dg.mainf('test', 10, ['h1', 'h2', 'h3'], ["normal", "triangular", "beta"], [[0, 12], [5, 10, 15], [10, 20]], 10)
    return HttpResponse('OK')


# @csrf_protect
@require_POST
def tokensign(request, *args):
    token = request.POST.get('idtoken', None)
    CLIENT_ID = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer')

        userid = idinfo['sub']
        first_name = idinfo['given_name']
        last_name = idinfo['family_name']
        email = idinfo['email']

        if User.objects.filter(username=userid).exists():
            user = User.objects.get(username=userid)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
        else:
            user = User(username=userid, first_name=first_name, last_name=last_name, email=email)
            user.set_unusable_password()
            user.save()
            login(request, user)
        return HttpResponse(userid)
    except ValueError as e:
        return HttpResponse(e)


@require_GET
def generate(request, *args):
    filename = 'test'
    rows = 10
    headers = []
    types = []
    params = []

    data = request.GET.get('data', None)
    if data is not None:
        data = json.loads(data)
        pre_params = []  # этот список используется для перечисления параметров отдельного распределения до его
        # добавления в итоговый список, в целях валидации
        for p in enumerate(data):
            if p[1]['name'] == 'rows':
                rows = int(p[1]['value'])
            elif p[1]['name'] == 'selected':
                i = 1
                pre_params.clear()
                try:
                    while data[p[0]+i]['name'] != 'selected':
                        if data[p[0]+i]['value'] != '':
                            pre_params.append(float(data[p[0]+i]['value']))
                            i += 1
                        else:
                            break
                except IndexError:
                    pass
                if len(pre_params) > 0:
                    headers.append(f'Столбец {len(headers) + 1}')
                    types.append(p[1]['value'])
                    params.append(pre_params.copy())
    else:
        rows = int(request.GET.get('rows', 10))
        headers = request.GET.getlist('header', ['h1, h2', 'h3'])
        types = request.GET.getlist('type', ['normal', 'triangular', 'beta'])
        params = json.loads(request.GET.get('params', '[[0, 12], [5, 10, 15], [10, 20]]'))
    # chunk_size = int(request.GET.get('chunk_size', 10))
    chunk_size = 100

    outfile = dg.mainf(filename, rows, headers, types, params, chunk_size)
    response = outfile.out_file()

    return HttpResponse(response)
