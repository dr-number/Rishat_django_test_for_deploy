def getCurrentHost(request):
    return request.META['HTTP_REFERER']