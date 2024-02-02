from django.contrib import admin

from .models import Post, Autor


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'birthday']
    ordering = ['name', '-birthday']
    list_filter = ['name', 'birthday']
    search_fields = ['name']
    search_help_text = 'Поиск по имени автора'

    readonly_fields = ['birthday']

    fieldsets = [
        (
            'Author',
            {
                'classes': ['wide'],
                'fields': ['name', 'last_name'],
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'description': 'Биография автора',
                'fields': ['birthday', 'bio', ],
            },
        ),
        (
            'Other',
            {
                'description': 'Контактная информация',
                'fields': ['email']
            }
        )
    ]


class PostAdmin(admin.ModelAdmin):
    @admin.action(description="Стереть содержание статьи")
    def reset_content(modeladmin, request, queryset):
        queryset.update(content="")

    list_display = ['title', 'content', 'author']
    ordering = ['title', 'author']
    list_filter = ['author', 'title', ]
    search_fields = ['title']
    search_help_text = 'Поиск по заголовку'
    actions = [reset_content]



    readonly_fields = ['is_published']

    fieldsets = [
        (
            'Post',
            {
                'classes': ['wide'],
                'fields': ['title'],
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'description': 'Автор',
                'fields': ['author', ],
            },
        ),
        (
            'Other',
            {
                'description': 'Прочая информация',
                'fields': ['is_published', 'views']
            },
        ),
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Autor, AuthorAdmin)
