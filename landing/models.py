from django.db import models

# Create your models here.

# <-- Main (Home) section -->


class Home(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True, verbose_name='Строка 1')
    subtitle = models.CharField(max_length=50, blank=True, null=True, verbose_name='Строка 2')
    tagline = models.CharField(max_length=50, blank=True, null=True, verbose_name='Строка 3')

    def __str__(self):
        return str(self.title) + str(self.subtitle) + str(self.tagline)

    class Meta:
        verbose_name = 'Домашняя сраница'
        verbose_name_plural = 'Домашние сраницы'


# <-- Second (About me) section -->


class AboutMe(models.Model):
    # right block
    name = models.CharField(max_length=50, blank=True, verbose_name='Заголовок правый')
    text = models.CharField(max_length=250, blank=True, verbose_name='Текст правого блока')
    # left block
    name_second = models.CharField(max_length=50, blank=True, verbose_name='Заголовок левый')
    text_second = models.CharField(max_length=250, blank=True, verbose_name='Текс левого блока')

    def __str__(self):
        return str(self.name) + str(self.text) + str(self.name_second) + str(self.text_second)

    class Meta:
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'

# <-- Third (About the site) section -->


class AboutSite(models.Model):
    title = models.CharField(max_length=50, blank=True, verbose_name='Заголовок')
    text = models.CharField(max_length=100, blank=True, verbose_name='Текст описания')
    name_one = models.CharField(max_length=20, blank=True, verbose_name='Заголовок первый')
    text_one = models.CharField(max_length=200, blank=True, verbose_name='Текст описания')
    name_two = models.CharField(max_length=20, blank=True, verbose_name=' Заголовок второй')
    text_two = models.CharField(max_length=200, blank=True, verbose_name='Текст описания')
    name_three = models.CharField(max_length=20, blank=True, verbose_name='Заголовок третий')
    text_three = models.CharField(max_length=200, blank=True, verbose_name='Текст описания')
    name_four = models.CharField(max_length=20, blank=True, verbose_name='Заголовок четвертый')
    text_four = models.CharField(max_length=200, blank=True, verbose_name='Текст описания')

    def __str__(self):
        return str(self.title)+str(self.text)+str(self.name_one)+str(self.text_one)+str(self.name_two)+str(
            self.text_two)+str(self.name_three)+str(self.text_three)+str(self.name_four)+str(self.text_four)

    class Meta:
        verbose_name = 'О сайте'
        verbose_name_plural = 'О сайте'

# <-- Fourth (Feedback) section -->


class Feedback(models.Model):
    line_one = models.CharField(max_length=100, blank=True, verbose_name='Строка 1')
    line_two = models.CharField(max_length=100, blank=True, verbose_name='Строка 2')
    line_three = models.CharField(max_length=100, blank=True, verbose_name='Строка 3')

    def __str__(self):
        return str(self.line_one) + str(self.line_two) + str(self.line_three)

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
