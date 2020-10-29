from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def person(request):
    # if request.method == 'POST':
    #     upload_file_obj = request.__get_files().get('fafafa')
    #     iter_file_data = upload_file_obj.chunks()
    #     f = open(upload_file_obj.name, 'wb')
    #     for d in iter_file_data:
    #         f.write(d)
    #         f.close()

    print(request.POST)
    print(request.GET)
    return HttpResponse('ok')