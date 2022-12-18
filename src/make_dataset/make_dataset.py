import ff
import requests
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm
import os
import json

def main():
    """
    bs = BeautifulSoup(requests.get("http://fantasyoverlord.com/FPL/History#google_vignette").content,"html.parser")
    results = bs.find(id="History")
    csvs = results.find_all("a")
    hrefs = [element['href'] for element in csvs if 'History' in element['href']]
    print("Now loading Fantasy Premier League data.")
    for i in tqdm(range(len(hrefs))):
        try:
            df = pd.read_csv("http://fantasyoverlord.com" + hrefs[i])
            df.to_csv(os.path.join(ff.PROJECT_ROOT,'data','raw',f"{hrefs[i].split('=')[-1]}.csv"), index=False)
        except:
            print(f"{hrefs[i].split('=')[-1]}.csv did not load")
    """

    df = df = pd.read_csv("https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/cleaned_merged_seasons.csv")
    df.to_csv(os.path.join(ff.PROJECT_ROOT,'data','raw','player_weekly_stats.csv'))

    with open(os.path.join(ff.PROJECT_ROOT,'src','ff','clubs','configs','clubs.json')) as f:
        clubs_json = json.load(f)
        

    print("Now loading ClubElo data.")
    for i in tqdm(range(len(clubs_json['clubs']))):
        club_config = clubs_json['clubs'][i]
        response = requests.get(f"http://api.clubelo.com/{club_config['clubelo_name']}")

        if response.status_code==200:
            with open(os.path.join(ff.PROJECT_ROOT,'data','raw',f"{club_config['name']}_elo.csv"),'w') as f:
                f.write(response.content.decode("utf-8"))
        else:
            print(f"Elo data for {club_config['name']} did not load.")

if __name__=='__main__':
    main()