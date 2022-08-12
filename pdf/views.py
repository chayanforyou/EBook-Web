from .models import PDF
from django.http import JsonResponse


def pdf_list(request):
    objects = PDF.objects.all().values("id", "name", "thumb", "pdf").order_by('-id')
    data = list(objects)
    return JsonResponse(data, safe=False)
