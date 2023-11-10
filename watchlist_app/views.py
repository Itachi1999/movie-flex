# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse

# # Create your views here.
# def movie_list(request):
#     movies = Movie.objects.all()
#     response_data = {'movies': list(movies.values())}
#     # print(movies.values())
    
#     return JsonResponse(response_data)

# def movie_detail(request, id):
#     movie_detail = Movie.objects.get(id=id)
#     response_data = {
#         'title': movie_detail.title,
#         'description' : movie_detail.description,
#         'active' : movie_detail.active,
#         'year' : movie_detail.year,
#     }
    
#     return JsonResponse(response_data)    
