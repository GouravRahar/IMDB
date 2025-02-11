import csv

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from io import TextIOWrapper

from imdb.models import Movie
from imdb.serializers import MovieCreateSerializer, MovieSerializer


# Create your views here.
class MoviewView(APIView):
    queryset = Movie.objects.all()
    serializer = MovieSerializer

    def get(self,request):
        curr_page = request.query_params.get('page',1)
        per_page_data = 100
        start_data = (curr_page-1)*per_page_data
        end_data = (curr_page)*per_page_data
        year_of_release = request.query_params.get('year_of_release')
        language = request.query_params.get('language')
        if year_of_release:
            self.queryset = self.queryset.filter(release_date__year=year_of_release)
        if language:
            self.queryset = self.queryset.filter(languages__contains=[language])

        sorting_by = request.query_params.get('sorting_by')
        if sorting_by:
            valid_sort_fields = ['release_date', 'vote_average']
            if sorting_by.lstrip('-') in valid_sort_fields:
                self.queryset = self.queryset.order_by(sorting_by)
        all_data = self.queryset[start_data:end_data]
        return Response({'data':self.serializer(all_data,many=True).data})



    def post(self,request):
        document = request.data.get("file",None)
        if not document:
            return Response({"error": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)

        decoded_file = TextIOWrapper(document, encoding='utf-8')
        reader = csv.DictReader(decoded_file)
        movies = []
        errors = []
        count = 1
        for row in reader:
            serializer = MovieCreateSerializer(data=row)
            if serializer.is_valid():
                movies.append(serializer.save())
            else:
                errors.append({"row": count, "errors": serializer.errors})
            count+=1

        if errors:
            return Response({"message": "Some rows failed to process.", "errors": errors}, status=status.HTTP_207_MULTI_STATUS)

        return Response({"message": "CSV file processed successfully.", "movies_created": len(movies)}, status=status.HTTP_201_CREATED)

