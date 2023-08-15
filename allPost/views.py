from django.shortcuts import render

from allPost import models


# Create your views here.
def index(request):
    blog = models.post.objects.all()
    return render(request, 'allPost/index.html', {'post': blog})