import ast
from rest_framework import serializers
from datetime import datetime
from imdb.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'budget',
            'homepage',
            'original_language',
            'original_title',
            'overview',
            'release_date',
            'revenue',
            'runtime',
            'status',
            'title',
            'vote_average',
            'vote_count',
            'production_company_id',
            'genre_id',
            'languages',
        ]

class MovieViewSerializer(serializers.Serializer):
    year_of_release = serializers.DateTimeField()
    language = serializers.CharField()


class MovieCreateSerializer(serializers.ModelSerializer):
    languages = serializers.CharField()

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_languages(self, value):
        try:
            return ast.literal_eval(value)  # Convert string to list
        except Exception as e:
            raise serializers.ValidationError(f"Error while uploading languages. {e}")

    def validate(self, data):
        # Convert numeric fields to appropriate types
        numeric_fields = ['budget', 'revenue', 'runtime', 'vote_count', 'production_company_id', 'genre_id']
        for field in numeric_fields:
            if data.get(field):
                try:
                    data[field] = int(data[field])  # Convert to integer
                except Exception as e:
                    raise serializers.ValidationError(f"Erroe for {field}. {e}")
        return data