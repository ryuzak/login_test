# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import UserForm
from .models import User

#import logint_test.functions as fn
# Create your views here.
def accounts_list(request):
	users = User.objects.all().order_by('id')
	#print(users)
	return render(request, 'accounts/accounts_list.html',{'users':users})

def account_add(request):
	form = UserForm(request.POST or None)
	if(form.is_valid()):
		try:
			model = User.objects.get(email=form.cleaned_data.get('email'))
			if(not model.is_active):
				#fn.sendmail_activations(user_model.email, model, '3')
				return redirect('recovery:user_success')
		except Exception as e:
			print(e)
			model = form.save(commit=False)
			model.password = ''
			model.is_active = False
			model.save()
			#fn.sendmail_activations(model.email, model, '3')
			return redirect('accounts:account_list')

			
	return render(request, 'accounts/account_add.html',{'form':form})


def account_edit(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	form = UserForm(request.POST or None, instance=user)
	if form.is_valid():
		model = form.save()
		return redirect('accounts:account_list')
	return render(request, 'accounts/account_add.html', {'form':form})

def account_delete(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	user.is_active = False
	user.save()
	return redirect('accounts:account_list')

