from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

def get_name_file(instance, filename):
    return '/'.join([get_random_string(length=5) + "_" + filename])

def user_directory_path(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


DEVICES = ((None, "Выберите тип устройства"),
           ('r', "Маршрутизатор"), 
           ('s', "Коммутатор"),
           ('h', "Концентратор"),
           ('e', "Конечное устройство"),
           ('c', "Соединение"))

class Network_configuration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(verbose_name="Дата создания")
    network_elements = models.ForeignKey("Element_list",null=True, verbose_name ="Список элементов", on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name = "Стоимость", max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Готовая сеть"
        verbose_name_plural = "Готовые сети"


class Element_list(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    connections_list = models.ForeignKey("Connections", verbose_name ="Список соединений", on_delete=models.CASCADE, blank=True)
    '''connections_list_price = sum(i.cost for i in connections_list)
    contections_count = len(connections_list)'''
    routers_list = models.ForeignKey("Router", verbose_name="Список маршрутизаторов", on_delete=models.CASCADE, blank=True)
    switche_list = models.ForeignKey("Switch", verbose_name="Список коммутаторов", on_delete=models.CASCADE, blank=True)
    hub_list = models.ForeignKey("Hub", verbose_name="Список хабов", on_delete=models.CASCADE, blank=True)
    end_devices_list = models.ForeignKey("End_devices", verbose_name="Список конечных устройств", on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = "Список элементов"
        verbose_name_plural = "Списки элементов"

    

class Element_category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Катеогрия устройства", choices=DEVICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория устройства"
        verbose_name_plural = "Категории устройств"

class Element(models.Model):
    manufacturer = models.CharField(max_length=50, verbose_name="Производитель")
    model = models.CharField(max_length = 50, verbose_name="Модель")
    cost = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    manufacturer_country = models.CharField(max_length=50, verbose_name="Страна производства", blank=True, null = True)
    weight = models.DecimalField(verbose_name="Вес в кг", decimal_places=2, max_digits=10, blank= True, null = True)
    width = models.DecimalField(verbose_name="Ширина в м", max_digits=10, decimal_places=2, blank= True, null = True)
    length = models.DecimalField(verbose_name="Длинна в м",  max_digits=10, decimal_places=2, blank= True, null = True)
    height = models.DecimalField(verbose_name="Высота в м",  max_digits=10, decimal_places=2, blank= True, null = True)
    image = models.ImageField(verbose_name="Изображение", upload_to="img/", blank=True, null = True, default="/static/img/img1.png")
    category = models.ForeignKey(Element_category, on_delete=models.PROTECT, null = True)


class Router(Element):
    used_network_protocols = models.CharField(verbose_name="Сетевые протоколы", max_length=255, blank=True)
    available_interfaces = models.CharField(verbose_name="Поддерживаемые интерфейсы", max_length=255, blank=True)
    overall_performance = models.CharField(verbose_name="Общая производительность", max_length=255, blank=True)

    class Meta:
        verbose_name = "Маршрутизатор"
        verbose_name_plural = "Маршрутизаторы"


class Switch(Element):
    number_of_ports = models.IntegerField(verbose_name="Количество портов", blank=True)
    filtering_speed = models.IntegerField(verbose_name="Скорость фильтрации", blank=True)
    routing_speed = models.IntegerField(verbose_name="Скорость маршрутизации", blank=True)
    transmission_ability = models.IntegerField(verbose_name="Пропускная способность", blank=True)
    frame_delay = models.IntegerField(verbose_name="Задержка передачи кадров", blank=True)
    the_ability_to_stack = models.IntegerField(verbose_name="Возможность стекирования", blank=True)
    work_level = models.IntegerField(verbose_name="Уровень работы", blank=True )

    class Meta:
        verbose_name = "Коммутатор"
        verbose_name_plural = "Коммутаторы"


class Hub(Element):
    number_of_ports = models.IntegerField(verbose_name="Количествопортов", blank=True)
    baud_rate  = models.IntegerField(verbose_name="Скорость передачи данных", blank=True)
    coaxial_or_optical_ports = models.BooleanField(verbose_name = "Наличие коаксильных или оптических портов", default=False)

    class Meta:
        verbose_name = "Концентратор"
        verbose_name_plural = "Концентраторы"


class End_devices(Element):
    device_type = models.CharField(verbose_name="Тип устройства", max_length=50)
    protocol_types = models.CharField(verbose_name="Типы протоклов", max_length=255)
    number_of_ports = models.IntegerField(verbose_name="Количество портов", blank=True)
    approximate_network_load = models.IntegerField(verbose_name="Приблизительная сетевая нагрузка", blank=True)

    class Meta:
        verbose_name = "Конечный девайс"
        verbose_name_plural = "Конечные девайсы"


class Connections(models.Model):
    cabel_type = models.CharField(verbose_name="Тип кабеля", max_length=50)
    type = models.CharField(verbose_name="Тип соединения", max_length=50)
    category = models.ForeignKey(Element_category, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Соединение"
        verbose_name_plural = "Соединения"