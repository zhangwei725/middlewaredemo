from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse


def test(request):
    print('view------>test被执行')
    # int('affsfsdfsdf')
    temp = TemplateResponse(request, 'index.html', {'msg': '213131313213'})
    return temp.render()
