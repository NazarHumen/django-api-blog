from django.http import JsonResponse


def article_list(request):
    if request.method == 'GET':
        data = [{"id": 1, "title": "Test"}]
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        return JsonResponse({}, status=201)


def detail(request, pk):
    return JsonResponse({"id": pk})
