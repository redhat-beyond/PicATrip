from django.apps import apps
from django.contrib import admin
from commenting_system.models import Comment


# Customized model registration
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'created_on', 'label', 'post')
    list_filter = ('created_on', 'label')
    search_fields = ('username', 'body')

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


# for viewing models registration fields
class ListAdminMixin(object):
    def __init__(self, general_model, admin_site):
        self.list_display = [field.name for field in general_model._meta.fields]
        super(ListAdminMixin, self).__init__(general_model, admin_site)


# Register all other models automatically - should stay last in file.
models = apps.get_models()
for model in models:
    admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
    try:
        admin.site.register(model, admin_class)
    except admin.sites.AlreadyRegistered:
        pass
