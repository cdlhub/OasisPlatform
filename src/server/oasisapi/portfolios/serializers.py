from rest_framework import serializers

from ..analyses.serializers import AnalysisSerializer
from .models import Portfolio


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = (
            'id',
            'name',
            'created',
            'modified',
        )

    def create(self, validated_data):
        data = dict(validated_data)
        if not data.get('creator') and 'request' in self.context:
            data['creator'] = self.context.get('request').user
        return super(PortfolioSerializer, self).create(data)

    def to_representation(self, instance):
        rep = super(PortfolioSerializer, self).to_representation(instance)
        rep['accounts_file'] = instance.get_absolute_accounts_file_url()
        rep['location_file'] = instance.get_absolute_location_file_url()
        rep['reinsurance_info_file'] = instance.get_absolute_reinsurance_info_file_url()
        rep['reinsurance_source_file'] = instance.get_absolute_reinsurance_source_file_url()

        if self.context.get('request'):
            rep['accounts_file'] = self.context['request'].build_absolute_uri(rep['accounts_file'])
            rep['location_file'] = self.context['request'].build_absolute_uri(rep['location_file'])
            rep['reinsurance_info_file'] = self.context['request'].build_absolute_uri(rep['reinsurance_info_file'])
            rep['reinsurance_source_file'] = self.context['request'].build_absolute_uri(rep['reinsurance_source_file'])

        return rep


class CreateAnalysisSerializer(AnalysisSerializer):
    class Meta(AnalysisSerializer.Meta):
        fields = ['name', 'model']

    def __init__(self, portfolio=None, *args, **kwargs):
        self.portfolio = portfolio
        super(CreateAnalysisSerializer, self).__init__(*args, **kwargs)

    def validate(self, attrs):
        attrs['portfolio'] = self.portfolio
        return super(CreateAnalysisSerializer, self).validate(attrs)
