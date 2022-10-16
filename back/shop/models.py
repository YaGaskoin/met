from django.db import models


class CarBrand(models.Model):
    name = models.CharField(verbose_name='Марка машины', max_length=100)

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'

    def __str__(self):
        return '{}'.format(self.name)


class CarModel(models.Model):
    name = models.CharField(verbose_name='Модель машины', max_length=100)
    car_brand = models.ForeignKey(
        CarBrand, verbose_name='Марка',
        related_name='models', on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    def __str__(self):
        return '{}'.format(self.name)


class CarColor(models.Model):
    name = models.CharField(verbose_name='Цвет', max_length=100)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Доступные цвета'

    def __str__(self):
        return '{}'.format(self.name)


class Order(models.Model):
    car_model = models.ForeignKey(
        CarModel, verbose_name='Модель машины',
        related_name='orders', on_delete=models.CASCADE
    )
    car_color = models.ForeignKey(
        CarColor, verbose_name='Цвет машины',
        related_name='orders', on_delete=models.CASCADE
    )
    date = models.DateField(verbose_name='Дата заказа', auto_now_add=True, null=True)
    count = models.IntegerField(verbose_name='Количество')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ от {}, на {}, цвет - {}, кол-во {}'.format(
            self.date, self.car_model.name, self.car_color.name, self.count)
