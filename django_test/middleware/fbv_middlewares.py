# function based middleware
def mymiddleware(get_response):
    print('one time initialization')
    def myfunction(request):
        print('before fun call')
        response=get_response(request)
        print('after fun call')
        return response
    return myfunction