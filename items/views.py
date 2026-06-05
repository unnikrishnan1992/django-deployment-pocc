from django.http import JsonResponse


def item_list(request):
    data = [
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Mobile"},
    ]
    return JsonResponse(data, safe=False)