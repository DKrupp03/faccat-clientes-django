from django.contrib import admin
from .models import Cliente, Endereco
from django.utils.timezone import localtime


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
  list_display = ('nome', 'sobrenome', 'get_cidade', 'get_data_cadastro_formatada')
  filter_fields = ('nome', 'sobrenome')

  def get_cidade(self, obj):
    return obj.endereco.cidade if obj.endereco else '-'
  get_cidade.short_description = 'Cidade'

  def get_data_cadastro_formatada(self, obj):
    return localtime(obj.data_cadastro).strftime('%d/%m/%Y %H:%M')
  get_data_cadastro_formatada.short_description = 'Data de Cadastro'
  get_data_cadastro_formatada.admin_order_field = 'data_cadastro'


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
  list_display = ('rua', 'numero', 'cidade', 'estado', 'cep')
