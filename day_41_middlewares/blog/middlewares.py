from django.shortcuts import HttpResponse

# my_middleware using function
def my_middleware(get_response):
    print('one time code')
    def my_function(request):
        print('before view')
        response = get_response(request)
        print('after view')
        return response
    return my_function


# MyMiddleware using class 
class MyMiddleware():
    def __init__(self , get_response):
        self.get_response = get_response
        print('one time code')
        
    def __call__(self, request):
        print('before view')
        # response = self.get_response(request)
        response = HttpResponse('middle ware return response not server view not calling')
        print('after view')
        return response