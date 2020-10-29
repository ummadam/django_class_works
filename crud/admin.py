from django.contrib import admin
from crud.models import MyModel, Account,Origin,Book,Category

# Register your models here.


class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'color', 'speed', 'model', 'tags')
    list_filter = ('model', )
    search_fields = ('color', 'speed', 'model', 'tags')

class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'account_username', 'account_followers', 'account_following')
    search_fields = ('account_username', 'account_description')

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_name', 'book_price', 'book_origin')
    list_filter = ('book_origin', )
    search_fields = ('book_name',)
    filter_horizontal = ('book_category',)

admin.site.register(MyModel, MyModelAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Origin)
admin.site.register(Book,BookAdmin)
admin.site.register(Category)
