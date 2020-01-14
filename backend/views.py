from django.shortcuts import render
from django.http import HttpResponse

from .externals.libs.datagenerator import main as dg

def test(request, *args, **kwargs):
    dg.mainf(10, ['h1', 'h2', 'h3'], ["normal", "triangular", "beta"], [[0, 12], [5, 10, 15], [10, 20]], 'test')
    return HttpResponse('OK')
