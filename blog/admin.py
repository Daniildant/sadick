from django.contrib import admin
from .models import Post, Category
# from django.contrib.flatpages.models import FlatPage
# from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _
from markdownx.admin import MarkdownxModelAdmin

# admin.site.register(Post),

# Re-register FlatPageAdmin
# admin.site.unregister(FlatPage)



# Define a new FlatPageAdmin
class FlatPageAdmin(MarkdownxModelAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'markdown', 'category', 'thumbnail')}),
        (_('Advanced options'), {
            'classes': ('collapse', ),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
                'content',
                'sites',
                'seo',
            ),
        }),
    )

# Re-register FlatPageAdmin
# admin.site.unregister(FlatPage)
admin.site.register(Post, FlatPageAdmin)
admin.site.register(Category),
