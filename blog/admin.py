from django.contrib import admin
from .models import Post, Category
# from django.contrib.flatpages.models import FlatPage

admin.site.register(Post),
admin.site.register(Category),

# Re-register FlatPageAdmin
# admin.site.unregister(FlatPage)
