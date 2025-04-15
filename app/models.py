from django.db import models

class ObjetoMuseu(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    modelo_3d = models.FileField(upload_to='modelos_3d/')

    def __str__(self):
        return self.nome
