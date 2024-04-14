from django.db import models

# Create your models here.
class Compile(models.Model):
    name=models.CharField(max_length=255, verbose_name='Имя языка')
    short_name=models.CharField(max_length=255, verbose_name='Короткое имя языка')
    text = models.TextField(verbose_name='Описание')
    starter = models.CharField(verbose_name='С помощью чего запускается файл (например python или py)', max_length=255)
    ext=models.CharField(max_length=255, verbose_name='Расширение файла (например .py)')
    input_command=models.CharField(max_length=255, verbose_name='Какая команда отвечает за ввод от пользователя (например input())')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'компилятор'
        verbose_name_plural = 'компиляторы'