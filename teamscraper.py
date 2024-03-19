import requests
from bs4 import BeautifulSoup

def Getter(URL: str) -> list:
    """
    Takes full URL of a CBS Sports College Basketball Team Schedule website and returns a list of 
    all the teams they have played against this season.
    """

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    table = soup.find(id="TableBase")
    teams_html = table.find_all("span", class_="TeamName")
    teams = []

    for team in teams_html:
        team = team.find("a", class_="")
        teams.append(team.text)

    return teams