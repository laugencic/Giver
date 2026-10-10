from django.shortcuts import render
import requests
import time 
import random


def data(request):
    ids=[]

    player=f"https://www.thesportsdb.com/api/v1/json/123/searchplayers.php?p=Lionel Messi"

    sample= [
    "Lionel Messi",
    "Cristiano Ronaldo",
    "Kevin De Bruyne",
    "Erling Haaland",
    "Mohamed Salah",
    "Neymar",
    "Kylian Mbappe",
    "Luka Modric",
    "Vinicius Junior",
    "Robert Lewandowski",
    ]

    #getting ids
    for name in sample:
        url_name=name.replace(" ","_")#repling empty spaces
        url=f"https://www.thesportsdb.com/api/v1/json/123/searchplayers.php?p={url_name}"
        response=requests.get(url)
        data=response.json()
        player_ids=data.get("player")

        if player_ids:
            player=player_ids[0]

            id=player.get('idPlayer')

            if id:
                ids.append(id)
    print(ids)

    #player details
    if ids:
        pick=random.choice(ids)

        url2=f"https://www.thesportsdb.com/api/v1/json/123/lookupplayer.php?p={pick}"

        p_response=requests.get(url2)
        data=p_response.json()
        players=data.get("player")
        
        if players:
            target=players[0]

            id=target.get('idPlayer')
            name=target.get('strPlayer')
            image=target.get('strCutout')
            country=target.get('strNationality')

            print(name)

            context={
                "data":data,
                "name":name,
                "image":image,
                "country":country
            }

        else:
            context={}
            print(p_response.status_code)
            print("No player found")
            print(pick)


    #former teams using player ids , which can apply(ids) when looking up players
    # former_teams=f"https://www.thesportsdb.com/api/v1/json/123/lookupformerteams.php?id={id}"
    milestones="https://www.thesportsdb.com/api/v1/json/123/lookupmilestones.php?id=34161397"
    statistics="https://www.thesportsdb.com/api/v1/json/123/lookupplayerstats.php?id=34146304"
    team_players="https://www.thesportsdb.com/api/v1/json/123/lookup_all_players.php?id=133604"
    

    # teams=requests.get(former_teams)
    # t_res=teams.json()



    return render(request,'index.html',context)

