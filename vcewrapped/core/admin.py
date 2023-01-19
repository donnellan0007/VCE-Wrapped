from django.contrib import admin
from core.models import Profile, Subject, Discipline, School
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.

class SubjectResource(resources.ModelResource):
    class Meta:
        model = Subject

class DisciplineResource(resources.ModelResource):
    class Meta:
        model = Discipline
class DisciplineAdmin(ImportExportModelAdmin):
    resource_classes = [DisciplineResource]
class SubjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [SubjectResource]
    list_display = ('name', 'discipline')

admin.site.register(Profile)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(School)
