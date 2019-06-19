from django.contrib.auth.models import User
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver


class Event(models.Model):
    type_message = models.ForeignKey("TypeMessage", blank=True, on_delete=models.PROTECT, verbose_name="Тип сообщения")
    titul = models.ForeignKey("Titul", blank=True, on_delete=models.PROTECT, verbose_name="Титул")
    organizatsiya = models.ForeignKey("Organizatsiya", blank=True, on_delete=models.PROTECT, verbose_name="Организация")
    date_registratsii = models.DateField(verbose_name="Дата регистрации")
    reg_number = models.CharField(max_length=50, verbose_name="Регистрационный номер")
    sut_info = models.TextField(verbose_name="Суть информации")
    klassif_priznak_UK = models.ForeignKey("KlassifPriznakUK", blank=True, on_delete=models.PROTECT, verbose_name="Классифицирующий признак (по статье УК РФ)")
    klassif_priznak_ugroza = models.ForeignKey("KlassifPriznakUgroza", blank=True, on_delete=models.PROTECT, verbose_name="Классифицирующий признак (угроза)")
    klassif_priznak_text = models.TextField(verbose_name="Классифицирующий признак (текст)", blank=True)
    rezolyutsiya_rukovodstva = models.TextField(verbose_name="Резолюция руководства ВНГ, ГУСБ", blank=True)
    date_start = models.DateField(verbose_name="Дата начало", null=True)
    date_finish = models.DateField(verbose_name="Дата конец", null=True)
    ispolnitel_organ = models.CharField(max_length=100, blank=True, verbose_name="Исполнитель (Орган)")
    ispolnitel_sotrudnik = models.CharField(max_length=100, blank=True, verbose_name="Исполннитель (сотрудник)")
    info_otrabotki_materiala = models.TextField(verbose_name="Информация, полученная в ходе отработки материала", blank=True)
    identified_face = models.ForeignKey("Face", blank=True, on_delete=models.PROTECT, verbose_name="В ходе проверки выявлены (установленны лица)")
    type_proverki = models.ForeignKey("TypeProverki", blank=True, on_delete=models.PROTECT, verbose_name="Вид проверки")
    rezult_proverki = models.ForeignKey("ResultProverki", blank=True, on_delete=models.PROTECT, verbose_name="Результат проверки")
    prinyatie_meri = models.TextField(verbose_name="Принятые меры", blank=True)
    otvet_zayavitelyu = models.TextField(verbose_name="Ответ заявителю", blank=True)
    ispolnenie_rezolyucii = models.TextField(verbose_name="Исполнение резолюции руководства ВНГ, ГУСБ", blank=True)
    data_otveta = models.DateField(verbose_name="Дата ответа заявителю", blank=True)
    ishodyaschii_nomer = models.CharField(max_length=50, blank=True, verbose_name="Исходящий номер документа")
    operativnaya_obstanovka = models.ForeignKey("OperativnayaObstanovka", blank=True, on_delete=models.PROTECT, verbose_name="Оперативная обстановка")
    # Свои поля
    date_creation = models.DateField(auto_now=True, verbose_name="Дата создания")
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Пользователь")
    status = models.ForeignKey("Status", on_delete=models.PROTECT, verbose_name="Пользователь")
    subdivision = models.ForeignKey("Subdivision", on_delete=models.PROTECT, verbose_name="Подразделение", default="ГУСБ")


class TypeMessage(models.Model):
    name = models.TextField(verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип сообщения"
        verbose_name_plural = "Типы сообщений"


class Titul(models.Model):
    name = models.CharField(max_length=300, verbose_name="Наименование")
    nomer_vhodyaschego = models.CharField(max_length=300, blank=True, verbose_name="Номер входящего документа")
    date_vhodyaschego = models.DateField(verbose_name="Дата входящего документа", blank=True)
    otkuda = models.CharField(max_length=100, blank=True, verbose_name="Откуда поступил документ")
    ishodyaschii_nomer = models.CharField(max_length=50, blank=True, verbose_name="Исходящий номер документа")
    date_ishodyaschego = models.DateField(verbose_name="Дата исходящего документа", blank=True)
    date_vneseniya = models.DateTimeField(verbose_name="Дата вненсения документа в ИБД", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Титул"
        verbose_name_plural = "Титулы"


class Organizatsiya(models.Model):
    name = models.CharField(max_length=300, verbose_name="Наименование организации")
    inn_ogrn = models.CharField(max_length=100, blank=True, verbose_name="ИНН (ОГРН)")
    adres_organiz_ate = models.ForeignKey("AdresAte", blank=True, on_delete=models.PROTECT, verbose_name="Адрес организации (АТЕ)")
    adres_organiz = models.CharField(max_length=100, blank=True, verbose_name="Адрес организации")
    inaya_informaciya = models.TextField(blank=True, verbose_name="Иная организация")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"


class AdresAte(models.Model):
    name = models.TextField(verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Адрес АТЕ"
        verbose_name_plural = "Адреса АТЕ"


class KlassifPriznakUK(models.Model):
    name = models.TextField(verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Классифицирующий признак (по статье УК РФ)"
        verbose_name_plural = "Классифицирующие признаки (по статье УК РФ)"


class KlassifPriznakUgroza(models.Model):
    name = models.TextField(verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Классифицирующий признак (угроза)"
        verbose_name_plural = "Классифицирующие признаки (угроза)"


class Face(models.Model):
    familiya = models.CharField(max_length=100, verbose_name="Фамилия")
    imya = models.CharField(max_length=100, verbose_name="Имя")
    otchestvo = models.CharField(max_length=100, verbose_name="Отчество")
    date_rojdeniya = models.DateField(verbose_name="Дата рождения")
    mesto_rojdeniya_ATE = models.ForeignKey("AdresAte", on_delete=models.PROTECT, verbose_name="Место рождения (АТЕ))")
    mesto_rojdeniya_raion = models.CharField(max_length=100, blank=True, verbose_name="Место рождения (район)")
    mesto_rojdeniya_np = models.CharField(max_length=100, blank=True, verbose_name="Место рождения (н.п.)")
    zvanie = models.ForeignKey("Zvanie", blank=True, on_delete=models.PROTECT, verbose_name="Воинское (специальное) звание")
    dopolnitelnaya_info = models.TextField(verbose_name="Дополнительная информация", blank=True)
    rodstvennie_svyazi = models.ManyToManyField('self', blank=True, symmetrical=False, verbose_name="Родственные связи")

    def __str__(self):
        return self.familiya

    class Meta:
        unique_together = (['familiya', 'imya', 'otchestvo', 'date_rojdeniya', 'mesto_rojdeniya_ATE'])
        verbose_name = "Лицо"
        verbose_name_plural = "Лица"


class Zvanie(models.Model):
    name = models.TextField(verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Звание"
        verbose_name_plural = "Звания"


class TypeProverki(models.Model):
    name = models.TextField(verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вид проверки"
        verbose_name_plural = "Виды проверок"


class ResultProverki(models.Model):
    name = models.TextField(verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Результа проверки"
        verbose_name_plural = "Результаты проверок"


class OperativnayaObstanovka(models.Model):
    date = models.DateField(verbose_name="Дата")
    klassif_priznak_ugroza = models.ForeignKey("KlassifPriznakUgroza", blank=True, on_delete=models.PROTECT, verbose_name="Классифицирующий признак (угроза)")
    klassif_priznak_text = models.TextField(verbose_name="Классифицирующий признак (текст)", blank=True)
    sut_info = models.TextField(verbose_name="Суть информации")
    prinyatie_meri = models.TextField(verbose_name="Принятые меры", blank=True)

    def __str__(self):
        return self.sut_info

    class Meta:
        verbose_name = "Оперативная обстановка"
        verbose_name_plural = "Оперативные обстановки"


class Status(models.Model):
    name = models.TextField(verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Subdivision(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"


# Кастомизируем модель User и добавляем дополнительные поля
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    subdivision = models.ForeignKey("Subdivision", on_delete=models.PROTECT, verbose_name="Подразделение", default=1)
    # avatar = models.ImageField(upload_to='images/users', verbose_name='Изображение')

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователя'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
