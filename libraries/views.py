from django.shortcuts import render
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from . import models
# Create your views here.

class LibraryListView(ListView):
	model = models.Library
	paginate_by= 20
	template_name = "libraries/index.html"
	ordering = ["-date_created"]
	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):        
		return super( LibraryListView,self).dispatch(
request, *args, **kwargs)

@login_required
def libraryDetail(request,pk):
	try:
		query = models.Library.objects.filter(pk = pk).first()
	except models.Library.DoesNotExist:
		raise Http404("notfound")
	context = {"data":query}
	return render(request,"libraries/libraryDetail.html",context)