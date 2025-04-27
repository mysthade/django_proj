from django.contrib import admin
from .models import Article, Category, ArticleImage

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'slug')
    prepopulated_fields = {'slug': ('category',)}

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'slug', 'main_page', 'category')
    inlines = [ArticleImageInline]
    multiupload_form = True
    multiupload_list = False
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('category',)
    search_fields = ['title', 'description', 'slug']
    ordering = ['-pub_date']
    save_on_top = True
    list_filter = ('pub_date', 'category')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)