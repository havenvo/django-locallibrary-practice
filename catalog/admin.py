from django.contrib import admin

from .models import Author, Genre, Book, BookInstance, Language


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

class BooksInline(admin.TabularInline):
    model = Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BooksInline]
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


admin.site.register(Genre)


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('display_book', 'status', 'due_back')
    list_filter = ('status', 'due_back')


admin.site.register(Language)