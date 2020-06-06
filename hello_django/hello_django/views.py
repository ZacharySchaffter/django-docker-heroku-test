from django.http import JsonResponse


def ping(request):
    data = {"ping": "pong!", "foo": "bar", "testing": "new-prop"}
    return JsonResponse(data)
