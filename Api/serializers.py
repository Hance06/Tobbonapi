from rest_framework import serializers
from Api.models import Belge

class BelgeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    belge_basligi = serializers.CharField()
    bagli_olunan_holding = serializers.CharField()
    firma_unvani = serializers.CharField()
    is_yeri_adresi = serializers.CharField()
    merkezi_adres = serializers.CharField()
    mersis_no = serializers.CharField()
    sanayi_sicil_no = serializers.CharField()
    tescilli_marka = serializers.CharField()
    ticaret_sicil_no = serializers.CharField()
    vergi_daire_no = serializers.CharField()
    guncelleme_tarihi = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Belge.objects.create(**validated_data)

    def update(self, instance, validated_data):
        belge_basligi = validated_data.get('belge_basligi',instance.belge_basligi)
        bagli_olunan_holding = validated_data.get('bagli_olunan_holding',instance.bagli_olunan_holding)
        firma_unvani = validated_data.get('firma_unvani',instance.firma_unvani)
        is_yeri_adresi = validated_data.get('is_yeri_adresi',instance.is_yeri_adresi)
        merkezi_adres = validated_data.get('merkezi_adres',instance.merkezi_adres)
        mersis_no = validated_data.get('mersis_no',instance.mersis_no)
        sanayi_sicil_no = validated_data.get('sanayi_sicil_no',instance.sanayi_sicil_no)
        tescilli_marka = validated_data.get('tescilli_marka',instance.tescilli_marka)
        ticaret_sicil_no = validated_data.get('ticaret_sicil_no',instance.ticaret_sicil_no)
        vergi_daire_no = validated_data.get('vergi_daire_no',instance.vergi_daire_no)
        guncelleme_tarihi = validated_data.get('guncelleme_tarihi',instance.guncelleme_tarihi)
        instance.save()
        return instance