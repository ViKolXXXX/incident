from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    tip_soobshcheniya = models.ForeignKey("TipSoobshcheniya", null=True, on_delete=models.PROTECT, verbose_name="Тип сообщения")
    titul = models.ForeignKey("Titul", null=True, on_delete=models.PROTECT, verbose_name="Титул")
    organizatsiya = models.ForeignKey("Organizatsiya", null=True, on_delete=models.PROTECT, verbose_name="Организация")
    data_registratsii = models.DateField(verbose_name="Дата регистрации")
    registratsionnyy_nomer = models.CharField(max_length=50, verbose_name="Регистрационный номер")
    sut_informatsii = models.TextField(verbose_name="Суть информации")
    klassif_priznak_UK = models.ForeignKey("KlassifPriznakUK", null=True, on_delete=models.PROTECT, verbose_name="Классифицирующий признак (по статье УК РФ)")
    klassif_priznak_ugroza = models.ForeignKey("KlassifPriznakUgroza", null=True, on_delete=models.PROTECT, verbose_name="Классифицирующий признак (угроза)")
    klassif_priznak_text = models.TextField(verbose_name="Классифицирующий признак (текст)", null=True)
    rezolyutsiya_rukovodstva = models.TextField(verbose_name="Резолюция руководства ВНГ, ГУСБ", null=True)
    srok_ispolneniya = models.DurationField(verbose_name="Срок исполнения", null=True)
    ispolnitel_organ = models.CharField(max_length=100, null=True, verbose_name="Исполнитель (Орган)")
    ispolnitel_sotrudnik = models.CharField(max_length=100, null=True, verbose_name="Исполннитель (сотрудник)")
    info_otrabotki_materiala = models.TextField(verbose_name="Информация, полученная в ходе отработки материала", null=True)
    viyavlennie_face = models.ForeignKey("Face", null=True, on_delete=models.PROTECT, verbose_name="В ходе проверки выявлены (установленны лица)")
    vid_proverki = models.ForeignKey("VidProverki", null=True, on_delete=models.PROTECT, verbose_name="Вид проверки")
    rezultat_proverki = models.ForeignKey("ResultatProverki", null=True, on_delete=models.PROTECT, verbose_name="Результат проверки")
    prinyatie_meri = models.TextField(verbose_name="Принятые меры", null=True)
    otvet_zayavitelyu = models.TextField(verbose_name="Ответ заявителю", null=True)
    ispolnenie_rezolyucii = models.TextField(verbose_name="Исполнение резолюции руководства ВНГ, ГУСБ", null=True)
    data_otveta = models.DateField(verbose_name="Дата ответа заявителю", null=True)
    ishodyaschii_nomer = models.CharField(max_length=50, null=True, verbose_name="Исходящий номер документа")
    operativnaya_obstanovka = 

    date_creation = models.DateField(auto_now=True, verbose_name="Дата создания")

    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Пользователь")
    status


class TipSoobshcheniya(models.Model):
    name = models.TextField(verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип сообщения"
        verbose_name_plural = "Типы сообщений"


class Titul(models.Model):
    name = models.CharField(max_length=300, verbose_name="Наименование")
    nomer_vhodyaschego = models.CharField(max_length=300, null=True, verbose_name="Номер входящего документа")
    date_vhodyaschego = models.DateField(verbose_name="Дата входящего документа", null=True)
    otkuda = models.CharField(max_length=100, null=True, verbose_name="Откуда поступил документ")
    ishodyaschii_nomer = models.CharField(max_length=50, null=True, verbose_name="Исходящий номер документа")
    date_ishodyaschego =  models.DateField(verbose_name="Дата исходящего документа", null=True)
    date_vneseniya = models.DateTimeField(verbose_name="Дата вненсения документа в ИБД", null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Титул"
        verbose_name_plural = "Титулы"


class Organizatsiya(models.Model):
    name = models.CharField(max_length=300, verbose_name="Наименование организации")
    inn_ogrn = models.CharField(max_length=100, null=True, verbose_name="ИНН (ОГРН)")
    adres_organiz_ate = models.ForeignKey("AdresAte", null=True, on_delete=models.PROTECT, verbose_name="Адрес организации (АТЕ)")
    adres_organiz = models.CharField(max_length=100, null=True, verbose_name="Адрес организации")
    inaya_informaciya = models.TextField(null=True, verbose_name="Иная организация")

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
    imya = models.CharField(max_length=100, null=True, verbose_name="Имя")
    otchestvo = models.CharField(max_length=100, null=True, verbose_name="Отчество")
    date_rojdeniya = models.DateField(verbose_name="Дата рождения", null=True)
    mesto_rojdeniya_ATE = models.ForeignKey("AdresAte", null=True, on_delete=models.PROTECT,
                                          verbose_name="Место рождения (АТЕ))")
    mesto_rojdeniya_raion = models.CharField(max_length=100, null=True, verbose_name="Место рождения (район)")
    mesto_rojdeniya_np = models.CharField(max_length=100, null=True, verbose_name="Место рождения (н.п.)")
    zvanie = models.ForeignKey("Zvanie", null=True, on_delete=models.PROTECT,
                                            verbose_name="Воинское (специальное) звание")
    dopolnitelnaya_info = models.TextField(verbose_name="Дополнительная информация", null=True)
    rodstvennie_svyazi = models.ManyToManyField("Face", verbose_name="Родственные связи")

    def __str__(self):
        return self.familiya

    class Meta:
        verbose_name = "Лицо"
        verbose_name_plural = "Лица"

class Zvanie(models.Model):
    name = models.TextField(verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Звание"
        verbose_name_plural = "Звания"


class VidProverki(models.Model):
    name = models.TextField(verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вид проверки"
        verbose_name_plural = "Виды проверок"

class ResultatProverki(models.Model):
    name = models.TextField(verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Результа проверки"
        verbose_name_plural = "Результаты проверок"