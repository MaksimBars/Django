from django.db import models

# Create your models here.

# <-- Main (Home) section -->


class Home(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True, verbose_name='Строка 1')
    subtitle = models.CharField(max_length=50, blank=True, null=True, verbose_name='Строка 2')
    tagline = models.CharField(max_length=50, blank=True, null=True, verbose_name='Строка 3')

    def __str__(self):
        return '%s %s %s' % (self.title, self.subtitle, self.tagline)

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'


# <-- Second (About me) section -->


class AboutMe(models.Model):
    # right block
    name = models.CharField(max_length=50, blank=True, verbose_name='Заголовок правый')
    text = models.CharField(max_length=250, blank=True, verbose_name='Текст правого блока')
    # left block
    name_second = models.CharField(max_length=50, blank=True, verbose_name='Заголовок левый')
    text_second = models.CharField(max_length=250, blank=True, verbose_name='Текс левого блока')

    def __str__(self):
        return '%s %s %s %s' % (self.name, self.text, self.name_second, self.text_second)

    class Meta:
        verbose_name = 'About Me'
        verbose_name_plural = 'About Me'

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
        return '%s %s %s %s %s %s %s %s %s %s' % (self.title, self.text, self.name_one, self.text_one, self.name_two,
                                                  self.text_two, self.name_three, self.text_three, self.name_four,
                                                  self.text_four)

    class Meta:
        verbose_name = 'About Site'
        verbose_name_plural = 'About Site'

# <-- Fourth (Feedback) section -->


class Feedback(models.Model):
    line_one = models.CharField(max_length=100, blank=True, verbose_name='Строка 1')
    line_two = models.CharField(max_length=100, blank=True, verbose_name='Строка 2')
    line_three = models.CharField(max_length=100, blank=True, verbose_name='Строка 3')

    def __str__(self):
        return '%s %s %s' % (self.line_one, self.line_two, self.line_three)

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedback'
