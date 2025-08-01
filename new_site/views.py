from django.http import HttpResponse, JsonResponse

def http_test(request):
    return HttpResponse("<h1>http test<h1>")

def json_test(req):
    return JsonResponse({'name':'ali'})