from django.http import JsonResponse


def ping(request):
    data = {"ping": "pong!", "foo": "bar", "testing": "pr-branches"}
    return JsonResponse(data)
