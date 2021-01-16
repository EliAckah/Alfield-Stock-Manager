from django.shortcuts import redirect,render
from .forms import UserRegisterForm,UserUpdateForm
from django.views.generic import UpdateView,DeleteView
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required,user_passes_test

@login_required
@user_passes_test(lambda u: u.is_superuser)
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('administrator')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def logout_view(request):
    """Log out the user"""
    logout(request)
    return render(request,'alfieldmanager/index.html')    

class UserUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name_suffix = '_update_form'

    def form_valid(self,form):
        return super().form_valid(form)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_user(request,pk):
    user = User.objects.get(id=pk)
   
    if request.method != 'POST':
        # Initial request; pre-fill form with the current user.
        form = UserUpdateForm(instance=user)
    else:
        # POST data submitted; process data.
        form = UserUpdateForm(instance=user, data=request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('administrator')
    context = {'user': user, 'form': form}
    return render(request, 'alfieldmanager/edit_user.html', context)

class UserDeleteView(LoginRequiredMixin,DeleteView):
    model = User
    success_url = '/administrator/' 
