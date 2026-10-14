from django.shortcuts import render
import requests
from decouple import config
token=config('TOKEN')
headers={
    "accept":"application/json",
    "Authorization":f"Bearer {token}"
}

movies=[]
def api_calls(request):
    if request.method=='POST':
        title=request.POST.get('title')

    # similar movies to the title
        url=f"https://api.themoviedb.org/3/search/movie?query={title}"



        response=requests.get(url,headers=headers)
        data=response.json()
        # print(data)
        results=data['results']
        # print(results)

        for result in results:
            poster_path=result.get('poster_path')
            content={
                'path':'https://image.tmdb.org/t/p/w500'+poster_path if poster_path else None,
                'title':result.get('title'),
                'overview':result.get('overview'),
                'date':result.get('release_date'),
                'id':result.get('id')

            }

            if content not in movies:
                movies.append(content)
    # print(movies)
    return render(request,'index.html',{'movies':movies})


def display(request,movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response=requests.get(url,headers=headers)
    movie=response.json()
    return render(request,'display.html',{'movie':movie})