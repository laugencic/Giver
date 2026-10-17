from django.shortcuts import render
import requests
from decouple import config
token=config('TOKEN')
headers={
    "accept":"application/json",
    "Authorization":f"Bearer {token}"
}


def api_calls(request):
    movies=[]

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

# displaying the clicked movie and extacting their genre ids 
def display(request,movie_id):
    posters=[]
    discovery_genres=[]

    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response=requests.get(url,headers=headers)
    movie=response.json()
    gs=movie['genres']
    for genre in gs:
        for key,value in genre.items():
            if key=='id':
                discovery_genres.append(value)

    genres = "|".join(str(a) for a in discovery_genres)
    
    url2 = f"https://api.themoviedb.org/3/discover/movie?with_genres={genres}"
    response2=requests.get(url2,headers=headers)

    data=response2.json()
    results=data['results']
    for result in results:
        poster_path=result.get('poster_path')
        content={
            'id': result.get('id'),
            'path':'https://image.tmdb.org/t/p/w500'+poster_path if poster_path else None,
            # 'title':result.get('title'),
            # 'overview':result.get('overview'),
            # 'date':result.get('release_date'),
            # 'id':result.get('id')

        }
        if content:
            posters.append(content)


    
    return render(request,'display.html',{'movie':movie,"posters":posters})

# similar movies based on genre

