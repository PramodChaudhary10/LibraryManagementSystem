from django.contrib import admin
from .models import Book, StudentExtra, IssuedBook
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'isbn', 'author', 'category']


admin.site.register(Book, BookAdmin)


class StudentExtraAdmin(admin.ModelAdmin):
    pass


admin.site.register(StudentExtra, StudentExtraAdmin)


class IssuedBookAdmin(admin.ModelAdmin):
    pass


admin.site.register(IssuedBook, IssuedBookAdmin)
