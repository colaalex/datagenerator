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
                # # пока работает только для распределний из двух параметров
                # if data[p[0]+1]['value'] != '':
                #     headers.append(f'Столбец {len(headers)+1}')
                #     types.append(p[1]['value'])
                #     params.append([float(data[p[0]+1]['value']), float(data[p[0]+2]['value'])])
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
