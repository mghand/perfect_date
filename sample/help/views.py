from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from help.models import Req


# Create your views here.
def index(request):
    return render(request, 'help/index.html')

class ListReqView(ListView):
    template_name = 'help/req-list.html'
    model = Req

class CreateReqView(CreateView):
    template_name = 'help/req-create.html'
    model = Req
    fields = ('title', 'text', 'price')
    success_url = reverse_lazy('req-list')

