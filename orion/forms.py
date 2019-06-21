from django import forms
from django.forms import ModelForm

from orion.models import Event, TypeMessage, Titul, Organizatsiya, KlassifPriznakUK, KlassifPriznakUgroza, Face, TypeProverki, ResultProverki, OperativnayaObstanovka, \
    Status


class EventForm(ModelForm):
    status = forms.ModelChoiceField(label="Статус", required=True, empty_label=None, queryset=Status.objects.all(),
                                    widget=forms.Select(attrs={"class": "custom-select mr-sm-2"}))
    type_message = forms.ModelChoiceField(label="Тип сообщения", queryset=TypeMessage.objects.all(), empty_label=None, required=True,
                                          widget=forms.Select(attrs={"class": "custom-select mr-sm-2"}))
    titul = forms.ModelChoiceField(label="Документ", queryset=Titul.objects.all(),
                                   widget=forms.Select(attrs={"class": "custom-select mr-sm-2"}))

    organizatsiya = forms.ModelChoiceField(label="Организация", queryset=Organizatsiya.objects.all(),
                                           widget=forms.Select(attrs={"class": "custom-select mr-sm-2"}))
    date_registratsii = forms.DateField(label="Дата регистрации", required=True, widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}))
    reg_number = forms.CharField(label="Регистрационный номер", required=True, max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))

    sut_info = forms.CharField(label="Суть информации", required=True, widget=forms.Textarea(attrs={"class": "form-control", "cols": 2, "rows": 2}))

    klassif_priznak_UK = forms.ModelChoiceField(label="Классифицирующий признак (по статье УК РФ)", queryset=KlassifPriznakUK.objects.all(),
                                                widget=forms.Select(attrs={"class": "form-control selectpicker show-tick font-size-option", "data-live-search": "true",
                                                                           "data-size": "7"}))

    klassif_priznak_ugroza = forms.ModelChoiceField(label="Классифицирующий признак (угроза)", queryset=KlassifPriznakUgroza.objects.all(),
                                                    widget=forms.Select(attrs={"class": "form-control selectpicker show-tick font-size-option", "data-live-search": "true",
                                                                           "data-size": "7"}))
    klassif_priznak_text = forms.CharField(label="Классифицирующий признак (текст)", widget=forms.TextInput(attrs={"class": "form-control "}))
    rezolyutsiya_rukovodstva = forms.CharField(label="Резолюция руководства ВНГ, ГУСБ", widget=forms.Textarea(attrs={"class": "form-control", "cols": 2, "rows": 2}))
    date_start = forms.DateField(label="Дата начало", required=True, widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}))
    date_finish = forms.DateField(label="Дата конец", required=True, widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}))
    ispolnitel_organ = forms.CharField(label="Исполнитель (Орган)", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    ispolnitel_sotrudnik = forms.CharField(label="Исполннитель (сотрудник)", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    info_otrabotki_materiala = forms.CharField(label="Информация, полученная в ходе отработки материала",
                                               widget=forms.Textarea(attrs={"class": "form-control", "cols": 2, "rows": 2}))

    identified_face = forms.ModelChoiceField(label="В ходе проверки выявлены (установленны лица)", queryset=Face.objects.all(),
                                             widget=forms.Select(attrs={"class": "custom-select mr-sm-2"}))

    type_proverki = forms.ModelChoiceField(label="Вид проверки", queryset=TypeProverki.objects.all(), widget=forms.Select(attrs={"class": "custom-select mr-sm-2"}))
    rezult_proverki = forms.ModelChoiceField(label="Результат проверки", queryset=ResultProverki.objects.all(),
                                             widget=forms.Select(attrs={"class": "custom-select mr-sm-2"}))
    prinyatie_meri = forms.CharField(label="Принятые меры", widget=forms.Textarea(attrs={"class": "form-control", "cols": 2, "rows": 2}))
    otvet_zayavitelyu = forms.CharField(label="Ответ заявителю", widget=forms.Textarea(attrs={"class": "form-control", "cols": 2, "rows": 2}))
    ispolnenie_rezolyucii = forms.CharField(label="Исполнение резолюции руководства ВНГ, ГУСБ",
                                            widget=forms.Textarea(attrs={"class": "form-control", "cols": 2, "rows": 2}))
    data_otveta = forms.DateField(label="Дата ответа заявителю", widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}))
    ishodyaschii_nomer = forms.CharField(label="Исходящий номер документа", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    operativnaya_obstanovka = forms.ModelChoiceField(label="Оперативная обстановка", queryset=OperativnayaObstanovka.objects.all(),
                                                     widget=forms.Select(attrs={"class": "custom-select mr-sm-2"}))

    class Meta:
        model = Event
        exclude = [' date_creation', 'user', 'subdivision']
