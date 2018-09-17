from django.shortcuts import render
from.models import Comment

# Create your views here.
def indexf(request):
	comments=Comment.objects.order_by('-date_added')

	context={'comments':comments}
	return render(request,"Adminpanel/adpanel.html", context)