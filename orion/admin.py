from django.contrib import admin

from orion.models import Event, Status, TypeMessage, Titul, Org, AdresAte, KlassifPriznakUK, KlassifPriznakUgroza, Face, Zvanie, TypeProverki, ResultProverki, OperativnayaObstanovka

admin.site.register(Event)
admin.site.register(Status)
admin.site.register(TypeMessage)
admin.site.register(Titul)
admin.site.register(Org)
admin.site.register(AdresAte)
admin.site.register(KlassifPriznakUK)
admin.site.register(KlassifPriznakUgroza)
admin.site.register(Face)
admin.site.register(Zvanie)
admin.site.register(TypeProverki)
admin.site.register(ResultProverki)
admin.site.register(OperativnayaObstanovka)
