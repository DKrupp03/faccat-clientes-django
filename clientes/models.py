from django.db import models

class Endereco(models.Model):
  rua = models.CharField(max_length=100)
  numero = models.CharField(max_length=10)
  complemento = models.CharField(max_length=100, blank=True, null=True)
  bairro = models.CharField(max_length=100)
  cidade = models.CharField(max_length=100)
  estado = models.CharField(max_length=2)
  cep = models.CharField(max_length=9)

  def __str__(self):
    return f'{self.rua}, {self.numero} - {self.cidade}/{self.estado}'

class Cliente(models.Model):
  GENERO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outro'),
  ]

  ESTADO_CIVIL_CHOICES = [
    ('S', 'Solteiro(a)'),
    ('C', 'Casado(a)'),
    ('D', 'Divorciado(a)'),
    ('V', 'Viúvo(a)'),
    ('U', 'União Estável'),
  ]

  nome = models.CharField(max_length=100)
  sobrenome = models.CharField(max_length=100)
  cpf = models.CharField(max_length=14, unique=True)  # Formato: 000.000.000-00
  genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
  estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL_CHOICES)
  telefone = models.CharField(max_length=20)
  email = models.EmailField(unique=True)
  data_cadastro = models.DateTimeField(auto_now_add=True)
  endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.nome} {self.sobrenome}'
