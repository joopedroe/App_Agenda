from django.db import models

# Create your models here.


class Compromisso(models.Model):
    class Meta:
        verbose_name = 'Compromisso'
        verbose_name_plural= 'Compromissos'
    data=models.DateField()
    compromisso=models.CharField('Compromisso', max_length=200)
    horario=models.TimeField(blank=True,null=True)
    def __str__(self):
        return (self.compromisso)

class Agenda(models.Model):
    nomeAgenda=models.CharField('Nome Agenda', max_length=128)
    compromissos=models.ManyToManyField(Compromisso)
    publico=models.BooleanField('Público',blank=True,null=True)
    def __str__(self):
        return (self.nomeAgenda)

class Pessoa(models.Model):
    nome=models.CharField('Nome',max_length=128)
    cargo=models.CharField('Cargo',max_length=100)
    telefone_celular=models.CharField("Telefone Celular", max_length=15, help_text='Numero de telefone celular no formato (99)99999-9999', null=True, blank=True)
    email=models.EmailField('E-mail',null=True, blank=True)
    agendas=models.ForeignKey(Agenda,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return (self.nome)

class AgendaInstitucional(models.Model):
    nomeAgendaIn=models.CharField('Nome Agenda', max_length=128)
    compromissos=models.ManyToManyField(Compromisso)
    publico=models.BooleanField('Público',blank=True,null=True)
    def __str__(self):
        return (self.nomeAgendaIn)

