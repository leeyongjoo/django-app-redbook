from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from . import models
from .models import Book, Author, Publisher


# TemplateView
class BooksModelView(TemplateView):
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['model_list'] = ['Book', 'Author', 'Publisher']
        return context


# ListView
class BookList(ListView):
    model = Book


class AuthorList(ListView):
    model = Author


class PublisherList(ListView):
    model = Publisher


# DetailView
class BookDetail(DetailView):
    model = Book


class AuthorDetail(DetailView):
    model = Author


class PublisherDetail(DetailView):
    model = Publisher
