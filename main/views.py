from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

def home(request):
	blogs = Blog.objects.all().order_by('-id')
	context = {
		'blogs': blogs
	}
	return render(request, 'main/index.html', context)


def details(request, id):
	blog = Blog.objects.get(id=id)
	context = {
		'blog': blog
	}
	return render(request, 'main/details.html', context)

def add_blog(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = BlogForm(request.POST or None)
			if form.is_valid():
				data = form.save()
				return redirect('main:home')
		else:
			form = BlogForm()

		return render(request, 'main/add_blog.html', {'form': form})
	else:
		return redirect('main:home')

def edit_blog(request, id):
	if request.user.is_authenticated:
		blog = Blog.objects.get(id=id)
		if request.method == 'POST':
			form = BlogForm(request.POST, instance=blog)
			if form.is_valid():
				data = form.save()
				return redirect('main:details', id)
		else:
			form = BlogForm(instance=blog)

		return render(request, 'main/add_blog.html', {'form': form})
	else:
		return redirect('main:home')

def delete_blog(request, id):
	if request.user.is_authenticated:
		blog = Blog.objects.get(id=id)
		blog.delete()
		return redirect('main:home')
	else:
		return redirect('main:details', id)
