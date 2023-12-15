from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# books=[
#     {
#         'Title': 'Harry Potter',
#         'Author': 'J.K. Rowling'
#     },
#     {
#         'Title': 'The Lord Of The Rings',
#         'Author': 'J.R.R. Tolkien'
#     },
#     {
#         'Title': 'Percy Jackson',
#         'Author': 'Rick Riordan'
#     },
#     {
#         'Title': 'The Chronicles Of Narnia',
#         'Author': 'C.S. Lewis'
#     }
    
# ]

def home(request):
    context={
        'books': Book.objects.all()
    }
    return render(request, 'book/home.html', context)

class ReviewListView(ListView):
    model=Book
    template_name='book/home.html'
    context_object_name='books'
    ordering=['title']
    paginate_by=10

class UserReviewListView(ListView):
    model = Book
    template_name = 'book/user_reviews.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Book.objects.filter(author=user).order_by('title')


class ReviewDetailView(DetailView):
    model=Book

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model=Book
    fields=['title', 'book_author', 'genre', 'review']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Book
    fields=['title', 'book_author', 'genre', 'review']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        review=self.get_object()
        return self.request.user==review.author
    
class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Book
    success_url = reverse_lazy('book-home')
    
    def test_func(self):
        review=self.get_object()
        return self.request.user==review.author

def about(request):
    return render(request, 'book/about.html', {'title':'About'})

# Create your views here.
