from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    imagem_url = models.URLField()

    def __str__(self):
        return self.nome
