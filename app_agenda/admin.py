from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Compromisso)
class CompromissoAdmin(admin.ModelAdmin):
    pass


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    pass

@admin.register(AgendaInstitucional)
class AgendaInstitucionalAdmin(admin.ModelAdmin):
    pass