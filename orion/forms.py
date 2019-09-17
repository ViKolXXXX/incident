from django import forms
from django.forms import ModelForm

from orion.models import Event, TypeMessage, Titul, Org, KlassifPriznakUK, KlassifPriznakUgroza, Face, TypeProverki, ResultProverki, OperativnayaObstanovka, Status, AdresAte, Zvanie


class EventForm(ModelForm):
    status = forms.ModelChoiceField(label="Статус", required=True, empty_label=None, queryset=Status.objects.all(), widget=forms.Select(attrs={"class": "custom-select mr-sm-2"}))
    date_vklyuch_doklad = forms.DateField(label="Дата включения в доклад", required=False, widget=forms.DateInput(format='%Y-%m-%d', attrs={"class": "form-control form-control-sm", "type": "date"}))
    type_message = forms.ModelChoiceField(label="Тип сообщения", queryset=TypeMessage.objects.all(), empty_label=None, required=True, widget=forms.Select(attrs={"class": "custom-select mr-sm-2"}))
    titul = forms.ModelChoiceField(label="Документ", queryset=Titul.objects.all(), required=False, widget=forms.Select(attrs={"class": "custom-select mr-sm-2"}))
    org = forms.ModelMultipleChoiceField(label="Организация", queryset=Org.objects.all(), required=False,
                                         widget=forms.SelectMultiple(attrs={"class": "form-control", "multiple": "multiple",
                                                                    "title": "Ничего не выбрано"}))
    date_registratsii = forms.DateField(label="Дата регистрации", required=True, widget=forms.DateInput(format='%Y-%m-%d', attrs={"class": "form-control form-control-sm", "type": "date"}))
    reg_number = forms.CharField(label="Регистрационный номер", required=True, max_length=50, widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}))
    sut_info = forms.CharField(label="Суть информации", required=True, widget=forms.Textarea(attrs={"class": "form-control form-control-sm", "cols": 2, "rows": 2}))
    klassif_priznak_UK = forms.ModelChoiceField(label="Классифицирующий признак (по статье УК РФ)", queryset=KlassifPriznakUK.objects.all(), required=False,
                                                widget=forms.Select(attrs={"class": "form-control form-control-sm selectpicker show-tick font-size-option", "data-live-search": "true", "data-size": "7"}))
    klassif_priznak_ugroza = forms.ModelChoiceField(label="Классифицирующий признак (угроза)", queryset=KlassifPriznakUgroza.objects.all(), required=False,
                                                    widget=forms.Select(attrs={"class": "form-control form-control-sm selectpicker show-tick font-size-option", "data-live-search": "true", "data-size": "7"}))
    klassif_priznak_text = forms.CharField(label="Классифицирующий признак (текст)", required=False, widget=forms.TextInput(attrs={"class": "form-control form-control-sm "}))
    rezolyutsiya_rukovodstva = forms.CharField(label="Резолюция руководства ВНГ, ГУСБ", required=False, widget=forms.Textarea(attrs={"class": "form-control form-control-sm", "cols": 2, "rows": 2}))
    date_start = forms.DateField(label="Дата начала", required=True, widget=forms.DateInput(format='%Y-%m-%d', attrs={"class": "form-control form-control-sm", "type": "date"}))
    date_finish = forms.DateField(label="Дата окончания", required=True, widget=forms.DateInput(format='%Y-%m-%d', attrs={"class": "form-control form-control-sm", "type": "date"}))
    ispolnitel_organ = forms.CharField(label="Исполнитель (Орган)", max_length=100, required=False, widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}))
    ispolnitel_sotrudnik = forms.CharField(label="Исполннитель (Сотрудник)", max_length=100, required=False, widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}))
    info_otrabotki_materiala = forms.CharField(label="Информация, полученная в ходе отработки материала", required=False, widget=forms.Textarea(attrs={"class": "form-control form-control-sm", "cols": 2, "rows": 2}))
    identified_face = forms.ModelMultipleChoiceField(label="В ходе проверки выявлены (установленны лица)", queryset=Face.objects.all(), required=False,
                                                     widget=forms.SelectMultiple(attrs={"class": "form-control", "multiple": "multiple"}))
    type_proverki = forms.ModelChoiceField(label="Вид проверки", queryset=TypeProverki.objects.all(), required=False, widget=forms.Select(attrs={"class": "custom-select mr-sm-2"}))
    rezult_proverki = forms.ModelChoiceField(label="Результат проверки", queryset=ResultProverki.objects.all(), required=False, widget=forms.Select(attrs={"class": "custom-select mr-sm-2"}))
    prinyatie_meri = forms.CharField(label="Принятые меры", required=False, widget=forms.Textarea(attrs={"class": "form-control form-control-sm", "cols": 2, "rows": 2}))
    otvet_zayavitelyu = forms.CharField(label="Ответ заявителю", required=False, widget=forms.Textarea(attrs={"class": "form-control form-control-sm", "cols": 2, "rows": 2}))
    ispolnenie_rezolyucii = forms.CharField(label="Исполнение резолюции руководства ВНГ, ГУСБ", required=False, widget=forms.Textarea(attrs={"class": "form-control form-control-sm", "cols": 2, "rows": 2}))
    date_otveta = forms.DateField(label="Дата ответа заявителю", required=False, widget=forms.DateInput(attrs={"class": "form-control form-control-sm", "type": "date"}))
    ishodyaschii_nomer = forms.CharField(label="Исходящий номер документа", max_length=50, required=False, widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}))
    operativnaya_obstanovka = forms.ModelChoiceField(label="Оперативная обстановка", queryset=OperativnayaObstanovka.objects.all(), required=False,
                                                     widget=forms.Select(attrs={"class": "form-control form-control-sm selectpicker show-tick font-size-option", "data-live-search": "true", "data-size": "7"}))

    class Meta:
        model = Event
        exclude = [' date_creation', 'user', 'subdivision', 'date_change']



class TitulForm(ModelForm):
    name = forms.CharField(label="Наименование документа", required=True, max_length=300, widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}))
    nomer_vhodyaschego = forms.CharField(label="Номер входящего документа", required=False, max_length=300, widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}))
    date_vhodyaschego = forms.DateField(label="Дата входящего документа", required=False, widget=forms.DateInput(format='%Y-%m-%d', attrs={"class": "form-control form-control-sm", "type": "date"}))
    otkuda = forms.CharField(label="Откуда поступил документ", max_length=100, required=False, widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}))
    ishodyaschii_nomer = forms.CharField(label="Исходящий номер документа", max_length=50, required=False, widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}))
    date_ishodyaschego = forms.DateField(label="Дата исходящего документа", required=False, widget=forms.DateInput(format='%Y-%m-%d', attrs={"class": "form-control form-control-sm", "type": "date"}))

    class Meta:
        model = Titul
        exclude = ['date_vneseniya']


class OrgForm(ModelForm):
    name = forms.CharField(label="Наименование организации", required=True, max_length=300, widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}))
    inn_ogrn = forms.CharField(label="ИНН (ОГРН)", required=False, max_length=300, widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}))
    adres_organiz_ate = forms.ModelChoiceField(label="Адрес организации (АТЕ)", queryset=AdresAte.objects.all(), widget=forms.Select(attrs={"class": "custom-select mr-sm-2"}))
    adres_organiz = forms.CharField(label="Адрес организации", max_length=100, required=False, widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}))
    inaya_informaciya = forms.CharField(label="Иная информация", required=False, widget=forms.Textarea(attrs={"class": "form-control form-control-sm", "cols": 2, "rows": 2}))

    class Meta:
        model = Org
        fields = '__all__'


class OperationalEnvForm(ModelForm):
    date = forms.DateField(label="Дата", required=True, widget=forms.DateInput(format='%Y-%m-%d', attrs={"class": "form-control form-control-sm", "type": "date"}))
    klassif_priznak_ugroza = forms.ModelChoiceField(label="Классифицирующий признак (угроза)", queryset=KlassifPriznakUgroza.objects.all(), required=False,
                                                    widget=forms.Select(attrs={"class": "form-control form-control-sm selectpicker show-tick font-size-option", "data-live-search": "true", "data-size": "7"}))
    klassif_priznak_text = forms.CharField(label="Классифицирующий признак (текст)", required=False, widget=forms.TextInput(attrs={"class": "form-control form-control-sm "}))
    sut_info = forms.CharField(label="Суть информации", required=True, widget=forms.Textarea(attrs={"class": "form-control form-control-sm", "cols": 2, "rows": 2}))
    prinyatie_meri = forms.CharField(label="Принятые меры", required=False, widget=forms.Textarea(attrs={"class": "form-control form-control-sm", "cols": 2, "rows": 2}))

    class Meta:
        model = OperativnayaObstanovka
        fields = '__all__'


class FaceForm(ModelForm):
    familiya = forms.CharField(label="Фамилия", required=True, max_length=100, widget=forms.TextInput(attrs={"class": "form-control form-control-sm "}))
    imya = forms.CharField(label="Имя", required=True, max_length=100, widget=forms.TextInput(attrs={"class": "form-control form-control-sm "}))
    otchestvo = forms.CharField(label="Отчество", required=True, max_length=100, widget=forms.TextInput(attrs={"class": "form-control form-control-sm "}))
    date_rojdeniya = forms.DateField(label="Дата рождения", required=True, widget=forms.DateInput(format='%Y-%m-%d', attrs={"class": "form-control form-control-sm ", "type": "date"}))
    mesto_rojdeniya_ATE = forms.ModelChoiceField(label="Место рождения (АТЕ)", required=False, queryset=AdresAte.objects.all(), widget=forms.Select(attrs={"class": "custom-select mr-sm-2"}))
    mesto_rojdeniya_raion = forms.CharField(label="Место рождения (район)", required=False, max_length=100, widget=forms.TextInput(attrs={"class": "form-control form-control-sm "}))
    mesto_rojdeniya_np = forms.CharField(label="Место рождения (н.п.)", required=False, max_length=100, widget=forms.TextInput(attrs={"class": "form-control form-control-sm "}))
    zvanie = forms.ModelChoiceField(label="Воинское (специальное) звание", required=True, queryset=Zvanie.objects.all(), widget=forms.Select(attrs={"class": "custom-select mr-sm-2"}))
    dopolnitelnaya_info = forms.CharField(label="Дополнительная информация", required=False, widget=forms.Textarea(attrs={"class": "form-control form-control-sm ", "cols": 2, "rows": 2}))

    class Meta:
        model = Face
        exclude = ['rodstvennie_svyazi']
