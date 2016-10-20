from rest_framework import serializers

from .models import Document, Paragraph


class ParagraphSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paragraph
        read_only_fields = ('id',)
        fields = ('name', 'text', 'id', 'weight')


class DocumentSerializer(serializers.ModelSerializer):
    paragraphs = ParagraphSerializer(many=True, partial=True)

    class Meta:
        model = Document
        exclude = ('creator',)

    def create(self, validated_data):
        user = self.context['request'].user
        document = Document.objects.create(
            creator=user,
            name=validated_data['name'],
            module=validated_data['module'])

        for item in validated_data['paragraphs']:

            paragraph = Paragraph(text=item['text'],
                                  weight=item['weight'],
                                  document=document)
            if 'name' in item:
                paragraph.name = item['name']
            paragraph.save()

        return document

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.save()

        for paragraph in instance.paragraphs.all():
            paragraph.delete()

        for item in validated_data['paragraphs']:
            paragraph = Paragraph(name=item['name'],
                                  text=item['text'],
                                  weight=item['weight'],
                                  document=instance)
            paragraph.save()

        return instance
