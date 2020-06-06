from django.http import JsonResponse


def ping(request):
    data = {"ping": "pong!", "foo": "bar"}
    return JsonResponse(data)
