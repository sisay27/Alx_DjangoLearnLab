from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
from .models import Post
from django.views.generic.edit import DeleteView,CreateView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        user.email = request.POST.get('email')
        # Update other profile fields as needed
        user.save()
        # Redirect to the profile page or a success page
        return redirect('profile')
    context = {
        'user': user
    }
    return render(request, 'app_name/profile.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 10  # Number of posts per page

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
