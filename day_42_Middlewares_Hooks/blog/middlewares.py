from django.shortcuts import HttpResponse

# hook - 1
class MyProcessMiddleware():
    def __init__(self , get_response):
        self.get_response = get_response
    
    def __call__(self,request):
        response = self.get_response(request)
        return response
    
    def process_view(request, *args, **kwargs):
        return HttpResponse('this is process view')
        # return None

# hook - 2
class MyExceptionMiddleware():
    def __init__(self , get_response):
        self.get_response = get_response
    
    def __call__(self,request):
        response = self.get_response(request)
        return response
    
    def process_exception(self, request, exception):
        msg = exception
        return HttpResponse(f'this is process_exxception  {msg}')
        # return None


# hook - 3
class MyTemplateResponseMiddleware():
    def __init__(self , get_response):
        self.get_response = get_response
    
    def __call__(self,request):
        response = self.get_response(request)
        return response
    
    def process_template_response(self, request, response):
        print('process template response from middleware')
        response.context_data['name'] = 'nazz'
        return response