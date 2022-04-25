from django.http import JsonResponse
def helloworld(request):
    data = {"Message": "Hello World!"}
    return JsonResponse(data, safe=False)