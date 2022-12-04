import ff
import requests
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm
import os

def main():

    bs = BeautifulSoup(requests.get("http://fantasyoverlord.com/FPL/History#google_vignette").content,"html.parser")
    results = bs.find(id="History")
    csvs = results.find_all("a")
    hrefs = [element['href'] for element in csvs if 'History' in element['href']]

    for i in tqdm(range(len(hrefs))):
        try:
            df = pd.read_csv("http://fantasyoverlord.com" + hrefs[i])
            df.to_csv(os.path.join(ff.PROJECT_ROOT,'data','raw',f"{hrefs[i].split('=')[-1]}.csv"), index=False)
        except:
            print(f"{hrefs[i].split('=')[-1]}.csv did not load")

if __name__=='__main__':
    main()