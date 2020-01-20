from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET

import json

from .externals.libs.datagenerator import main as dg


def test(request, *args, **kwargs):
    dg.mainf('test', 10, ['h1', 'h2', 'h3'], ["normal", "triangular", "beta"], [[0, 12], [5, 10, 15], [10, 20]], 10)
    return HttpResponse('OK')


@require_GET
def generate(request, *args):
    filename = 'test'
    rows = int(request.GET.get('rows', 10))
    headers = request.GET.getlist('header', ['h1, h2', 'h3'])
    types = request.GET.getlist('type', ['normal', 'triangular', 'beta'])
    params = json.loads(request.GET.get('params', '[[0, 12], [5, 10, 15], [10, 20]]'))
    chunk_size = int(request.GET.get('chunk_size', 10))
    dg.mainf(filename, rows, headers, types, params, chunk_size)
    return HttpResponse('OK')
