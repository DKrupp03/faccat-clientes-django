import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')
django.setup()

from clientes.models import Cliente, Endereco

clientes_data = [
  {
    "nome": "Ana", "sobrenome": "Silva", "cpf": "111.111.111-11", "genero": "F", "estado_civil": "S",
    "telefone": "5199990001", "email": "ana1@example.com", "rua": "Rua A", "numero": "101", "bairro": "Centro",
    "cidade": "Porto Alegre", "estado": "RS", "cep": "90000-000"
  },
  {
    "nome": "Bruno", "sobrenome": "Souza", "cpf": "222.222.222-22", "genero": "M", "estado_civil": "C",
    "telefone": "5199990002", "email": "bruno@example.com", "rua": "Av B", "numero": "202", "bairro": "Jardim",
    "cidade": "Canoas", "estado": "RS", "cep": "92000-000"
  },
  {
    "nome": "Carlos", "sobrenome": "Oliveira", "cpf": "333.333.333-33", "genero": "M", "estado_civil": "D",
    "telefone": "5199990003", "email": "carlos@example.com", "rua": "Rua C", "numero": "303", "bairro": "Centro",
    "cidade": "São Leopoldo", "estado": "RS", "cep": "93000-000"
  },
  {
    "nome": "Daniela", "sobrenome": "Moraes", "cpf": "444.444.444-44", "genero": "F", "estado_civil": "U",
    "telefone": "5199990004", "email": "daniela@example.com", "rua": "Rua D", "numero": "404", "bairro": "Vista Alegre",
    "cidade": "Gravataí", "estado": "RS", "cep": "94000-000"
  },
  {
    "nome": "Eduardo", "sobrenome": "Lima", "cpf": "555.555.555-55", "genero": "M", "estado_civil": "S",
    "telefone": "5199990005", "email": "edu@example.com", "rua": "Rua E", "numero": "505", "bairro": "Boa Vista",
    "cidade": "Viamão", "estado": "RS", "cep": "94400-000"
  },
  {
    "nome": "Fernanda", "sobrenome": "Pires", "cpf": "666.666.666-66", "genero": "F", "estado_civil": "C",
    "telefone": "5199990006", "email": "fernanda@example.com", "rua": "Rua F", "numero": "606", "bairro": "Centro",
    "cidade": "Alvorada", "estado": "RS", "cep": "94800-000"
  },
  {
    "nome": "Gabriel", "sobrenome": "Alves", "cpf": "777.777.777-77", "genero": "M", "estado_civil": "S",
    "telefone": "5199990007", "email": "gabriel@example.com", "rua": "Rua G", "numero": "707", "bairro": "Santa Cecília",
    "cidade": "Pelotas", "estado": "RS", "cep": "96000-000"
  },
  {
    "nome": "Helena", "sobrenome": "Dias", "cpf": "888.888.888-88", "genero": "F", "estado_civil": "V",
    "telefone": "5199990008", "email": "helena@example.com", "rua": "Rua H", "numero": "808", "bairro": "Tristeza",
    "cidade": "Porto Alegre", "estado": "RS", "cep": "91700-000"
  },
  {
    "nome": "Igor", "sobrenome": "Martins", "cpf": "999.999.999-99", "genero": "M", "estado_civil": "U",
    "telefone": "5199990009", "email": "igor@example.com", "rua": "Rua I", "numero": "909", "bairro": "Menino Deus",
    "cidade": "Porto Alegre", "estado": "RS", "cep": "90100-000"
  },
  {
    "nome": "Joana", "sobrenome": "Freitas", "cpf": "000.000.000-00", "genero": "F", "estado_civil": "D",
    "telefone": "5199990010", "email": "joana@example.com", "rua": "Rua J", "numero": "1001", "bairro": "Centro",
    "cidade": "Caxias do Sul", "estado": "RS", "cep": "95000-000"
  },
  {
    "nome": "Kevin", "sobrenome": "Torres", "cpf": "123.123.123-12", "genero": "M", "estado_civil": "S",
    "telefone": "5199990011", "email": "kevin@example.com", "rua": "Rua K", "numero": "1101", "bairro": "Cruzeiro",
    "cidade": "Santa Maria", "estado": "RS", "cep": "97000-000"
  },
  {
    "nome": "Larissa", "sobrenome": "Rocha", "cpf": "234.234.234-23", "genero": "F", "estado_civil": "C",
    "telefone": "5199990012", "email": "larissa@example.com", "rua": "Rua L", "numero": "1201", "bairro": "Nonoai",
    "cidade": "Porto Alegre", "estado": "RS", "cep": "91750-000"
  },
  {
    "nome": "Marcos", "sobrenome": "Vieira", "cpf": "345.345.345-34", "genero": "M", "estado_civil": "S",
    "telefone": "5199990013", "email": "marcos@example.com", "rua": "Rua M", "numero": "1301", "bairro": "Sarandi",
    "cidade": "Porto Alegre", "estado": "RS", "cep": "91100-000"
  },
  {
    "nome": "Natália", "sobrenome": "Carvalho", "cpf": "456.456.456-45", "genero": "F", "estado_civil": "C",
    "telefone": "5199990014", "email": "natalia@example.com", "rua": "Rua N", "numero": "1401", "bairro": "Centro",
    "cidade": "Novo Hamburgo", "estado": "RS", "cep": "93500-000"
  },
  {
    "nome": "Otávio", "sobrenome": "Pereira", "cpf": "567.567.567-56", "genero": "M", "estado_civil": "D",
    "telefone": "5199990015", "email": "otavio@example.com", "rua": "Rua O", "numero": "1501", "bairro": "São José",
    "cidade": "Canoas", "estado": "RS", "cep": "92400-000"
  },
]

for c in clientes_data:
  endereco = Endereco.objects.create(
    rua=c["rua"],
    numero=c["numero"],
    complemento=c.get("complemento", ""),
    bairro=c["bairro"],
    cidade=c["cidade"],
    estado=c["estado"],
    cep=c["cep"]
  )

  Cliente.objects.create(
    nome=c["nome"],
    sobrenome=c["sobrenome"],
    cpf=c["cpf"],
    genero=c["genero"],
    estado_civil=c["estado_civil"],
    telefone=c["telefone"],
    email=c["email"],
    endereco=endereco
  )

print("15 clientes criados com sucesso!")
