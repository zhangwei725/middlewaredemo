"""
请求到达view之前方法

响应的方法

"""
from django.http import HttpResponse
from django.template.response import TemplateResponse

# class MD1:
#     # process_request
#     # request 到达 路由系统之前
#     def process_request(self, request):
#         print(request.GET.get('a'))
#         print('MD1 ----->process_request被执行')
#         # return HttpResponse('process_request')
#
#     # 路由系统匹配到 views 在请求到达view函数之前
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         print('MD1 ----->process_view被执行')
#         # return HttpResponse(request.GET.get('a'))
#
#     """
#     请求到达视图之后 视图函数抛出异常没有处理异常执行的方法
#     """
#
#     def process_exception(self, request, exception):
#         print('MD1---->process_exception被执行')
#
#     def process_template_response(self, request, response):
#         print('MD1---->process_template_response被执行')
#         response = TemplateResponse(request, 'index.html', {'msg': 'MD1'})
#         return response
#
#     def process_response(self, request, response):
#         print('MD1 ----->process_response被执行')
#         return HttpResponse(22222)
#
#
# class MD2:
#     # process_request
#     # request 到达 路由系统之前
#     def process_request(self, request):
#         print('MD2 ----->process_request被执行')
#
#     # 路由系统匹配到 views 在请求到达view函数之前
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         print('MD2 ----->process_view被执行')
#
#     """
#     请求到达视图之后 视图函数抛出异常没有处理异常执行的方法
#     """
#
#     def process_exception(self, request, exception):
#         print('MD2---->process_exception被执行')
#
#     def process_template_response(self, request, response):
#         print('MD2---->process_template_response被执行')
#         response = TemplateResponse(request, 'index.html', {'msg': '1231313213'})
#         return response
#
#     def process_response(self, request, response):
#         print('MD2 ----->process_response被执行')
#         return HttpResponse(111111)
from django.utils.deprecation import MiddlewareMixin

"""
10以上的版本的写法
"""


class Middle11:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        self.process_response(request, response)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('Middle11 ----->process_view被执行')
        return HttpResponse(1111)

    def process_exception(self, request, exception):
        print('Middle11---->process_exception被执行')

    def process_template_response(self, request, response):
        print('Middle11---->process_template_response被执行')
        return response

    def process_response(self, request, response):
        print('Middle11---->process_template_response被执行')
        return response


class Middle12(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        self.process_response(request, response)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('Middle12 ----->process_view被执行')

    def process_exception(self, request, exception):
        print('Middle12---->process_exception被执行')

    def process_template_response(self, request, response):
        print('Middle12---->process_template_response被执行')
        return response

    def process_response(self, request, response):
        print('Middle12---->process_response被执行')
        return response
