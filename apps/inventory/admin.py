from django.contrib import admin
from .models import Computer, Person, Assignment

# Registramos el modelo Computer en el admin
@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ('number', 'first_name', 'description', 'is_available', 'is_deleted')
    list_filter = ('is_available', 'is_deleted')
    search_fields = ('number', 'first_name', 'description')
    ordering = ('number',)
    list_editable = ('is_available',)

# Registramos el modelo Person en el admin
# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('dni', 'first_name', 'last_name', 'course', 'is_deleted')
#     list_filter = ('course', 'is_deleted')
#     search_fields = ('dni', 'first_name', 'last_name', 'course')
#     ordering = ('last_name', 'first_name')

# Registramos el modelo Assignment en el admin
# @admin.register(Assignment)
# class AssignmentAdmin(admin.ModelAdmin):
#     list_display = ('person', 'computer', 'date', 'observation', 'returned', 'is_deleted')
#     list_filter = ('returned', 'is_deleted', 'date')
#     search_fields = ('person__dni', 'person__first_name', 'person__last_name', 'computer__number', 'observation')
#     autocomplete_fields = ('person', 'computer')
#     ordering = ('-date',)
#     date_hierarchy = 'date'  # Esto permite filtrar por fecha en la parte superior
#     list_editable = ('returned', 'observation')  # Permite editar 'returned' y 'observation' desde la lista
