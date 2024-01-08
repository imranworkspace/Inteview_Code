from typing import Any


class Mymiddeware:
    def __init__(self,get_response):
        self.get_response=get_response
        print('cbv one time initialization')
    
    def __call__(self,request):
        print('cbv before view called')
        response = self.get_response(request)
        print('cbv after view called')
        return response