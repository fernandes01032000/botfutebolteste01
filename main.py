import requests
import json
import time
import telegram

token = '5943517777:AAFcEVrMzyFAeoo2aN85r5a21I6tY_0MgnQ'
chat_id = '688841070'

url = "https://api.sportsanalytics.com.br/api/v1/fixtures-svc/fixtures/livescores?include=weatherReport,additionalInfo,league,stats,pressureStats,probabilities"

headers = {
    "cookie": "route=f69973370a0dd0883a57c7b955dfc742; SRVGROUP=common",
    "authority": "api.sportsanalytics.com.br",
    "accept": "application/json, text/plain, */*",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "origin": "https://playscores.com",
    "referer": "https://playscores.com/",
    "sec-ch-ua": "^\^Google",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

response = requests.request("GET", url, headers=headers)

dic_response = response.json()

for game in dic_response['data']:
    fixtureId = game['fixtureId']
    createdAt = game['createdAt']
    date = game['date']
    dateTime = game['dateTime']
    popularity = game['popularity']
    roundId = game['roundId']
    seasonId = game['seasonId']
    stageId = game['stageId']
    status = game['status']
    time = game['time']
    timestamp = game['timestamp']
    timezone = game['timezone']
    updatedAt = game['updatedAt']

    awayTeam = game['awayTeam']['name']
    homeTeam = game['homeTeam']['name']
    league = game['league']['name']
    stats = game['stats']
    pressureStats = game['pressureStats']

    # additionalInfo#
    referee = game['additionalInfo']['referee']
    tvStations = game['additionalInfo']['tvStations']
    venue = game['additionalInfo']['venue']
    venueImage = game['additionalInfo']['venueImage']
    coordinates = game['additionalInfo']['coordinates']
    homeFormation = game['additionalInfo']['homeFormation']
    awayFormation = game['additionalInfo']['awayFormation']

    # currentTime
    minute = game['currentTime']['minute']
    second = game['currentTime']['second']
    addedTime = game['currentTime']['addedTime']
    extraMinute = game['currentTime']['extraMinute']
    injuryTime = game['currentTime']['injuryTime']

    # scores
    homeTeamScore = game['scores']['homeTeamScore']
    awayTeamScore = game['scores']['awayTeamScore']
    htScore = game['scores']['htScore']

    # standings
    standings_homeTeam = game['standings']['homeTeam']
    standings_awayTeam = game['standings']['awayTeam']

    # probabilities
    AT_over_0_5 = game['probabilities']['AT_over_0_5']
    AT_over_1_5 = game['probabilities']['AT_over_1_5']
    AT_under_0_5 = game['probabilities']['AT_under_0_5']
    AT_under_1_5 = game['probabilities']['AT_under_1_5']
    HT_over_0_5 = game['probabilities']['HT_over_0_5']
    HT_over_1_5 = game['probabilities']['HT_over_1_5']
    HT_under_0_5 = game['probabilities']['HT_under_0_5']
    HT_under_1_5 = game['probabilities']['HT_under_1_5']
    away = game['probabilities']['away']
    btts = game['probabilities']['btts']
    draw = game['probabilities']['draw']
    home = game['probabilities']['home']
    over_0_5 = game['probabilities']['over_0_5']
    over_1_5 = game['probabilities']['over_1_5']
    over_2_5 = game['probabilities']['over_2_5']
    over_3_5 = game['probabilities']['over_3_5']
    under_0_5 = game['probabilities']['under_0_5']
    under_1_5 = game['probabilities']['under_1_5']
    under_2_5 = game['probabilities']['under_2_5']
    under_3_5 = game['probabilities']['under_3_5']

    # stats
    # attacks
    attacks_home = game['stats']['attacks']['home']
    attacks_away = game['stats']['attacks']['away']

    # ballSafe
    ballSafe_home = game['stats']['ballSafe']['home']
    ballSafe_away = game['stats']['ballSafe']['away']

    # corners
    corners_home = game['stats']['corners']['home']
    corners_away = game['stats']['corners']['away']

    # dangerousAttacks
    dangerousAttacks_home = game['stats']['dangerousAttacks']['home']
    dangerousAttacks_away = game['stats']['dangerousAttacks']['away']

    # fouls
    fouls_home = game['stats']['fouls']['home']
    fouls_away = game['stats']['fouls']['away']

    # freeKick
    freeKick_home = game['stats']['freeKick']['home']
    freeKick_away = game['stats']['freeKick']['away']

    # goalAttempts
    goalAttempts_home = game['stats']['goalAttempts']['home']
    goalAttempts_away = game['stats']['goalAttempts']['away']

    # goalKick
    goalKick_home = game['stats']['goalKick']['home']
    goalKick_away = game['stats']['goalKick']['away']

    # goals
    goals_home = game['stats']['goals']['home']
    goals_away = game['stats']['goals']['away']

    # injuries
    injuries_home = game['stats']['injuries']['home']
    injuries_away = game['stats']['injuries']['away']

    # offsides
    offsides_home = game['stats']['offsides']['home']
    offsides_away = game['stats']['offsides']['away']

    # penalties
    penalties_home = game['stats']['penalties']['home']
    penalties_away = game['stats']['penalties']['away']

    # possessiontime
    possessiontime_home = game['stats']['possessiontime']['home']
    possessiontime_away = game['stats']['possessiontime']['away']

    # redcards
    redcards_home = game['stats']['redcards']['home']
    redcards_away = game['stats']['redcards']['away']

    # saves
    saves_home = game['stats']['saves']['home']
    saves_away = game['stats']['saves']['away']

    # shotsBlocked
    shotsBlocked_home = game['stats']['shotsBlocked']['home']
    shotsBlocked_away = game['stats']['shotsBlocked']['away']

    # shotsInsidebox
    shotsInsidebox_home = game['stats']['shotsInsidebox']['home']
    shotsInsidebox_away = game['stats']['shotsInsidebox']['away']

    # shotsOffgoal
    shotsOffgoal_home = game['stats']['shotsOffgoal']['home']
    shotsOffgoal_away = game['stats']['shotsOffgoal']['away']

    # shotsOngoal
    shotsOngoal_home = game['stats']['shotsOngoal']['home']
    shotsOngoal_away = game['stats']['shotsOngoal']['away']

    # shotsOutsidebox
    shotsOutsidebox_home = game['stats']['shotsOutsidebox']['home']
    shotsOutsidebox_away = game['stats']['shotsOutsidebox']['away']

    # substitutions
    substitutions_home = game['stats']['substitutions']['home']
    substitutions_away = game['stats']['substitutions']['away']

    # tackles
    tackles_home = game['stats']['tackles']['home']
    tackles_away = game['stats']['tackles']['away']

    # throwIn
    throwIn_home = game['stats']['throwIn']['home']
    throwIn_away = game['stats']['throwIn']['away']

    # yellowcards
    yellowcards_home = game['stats']['yellowcards']['home']
    yellowcards_away = game['stats']['yellowcards']['away']

    # yellowredcards
    yellowredcards_home = game['stats']['yellowredcards']['home']
    yellowredcards_away = game['stats']['yellowredcards']['away']

    # pressureStats
    # appm1
    appm1_home = game['pressureStats']['appm1']['home']
    appm1_away = game['pressureStats']['appm1']['away']

    # appm2
    appm2_home = game['pressureStats']['appm2']['home']
    appm2_away = game['pressureStats']['appm2']['away']

    # attack_momentum
    attack_momentum_home = game['pressureStats']['attack_momentum']['home']
    attack_momentum_away = game['pressureStats']['attack_momentum']['away']

    # exg
    exg_home = game['pressureStats']['exg']['home']
    exg_away = game['pressureStats']['exg']['away']

    # mh1
    mh1_home = game['pressureStats']['mh1']['home']
    mh1_away = game['pressureStats']['mh1']['away']

    # mh2
    mh2_home = game['pressureStats']['mh2']['home']
    mh2_away = game['pressureStats']['mh2']['away']

    # mh3
    mh3_home = game['pressureStats']['appm1']['home']
    mh3_away = game['pressureStats']['appm1']['away']

    if appm2_home >= 0:
        text = '{} x {} | APPM2 casa > 1'.format(homeTeam, awayTeam)
        url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
        results = requests.get(url_base)

    if appm2_away >= 1:
        text = '{} x {} | APPM2 fORA > 1'.format(homeTeam, awayTeam)
        url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
        results = requests.get(url_base)

    if over_0_5 >= 90:
        text = '{} x {} | OVER 0.5 > 90'.format(homeTeam, awayTeam)
        url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
        results = requests.get(url_base)

    if over_1_5 >= 90:
        text = '{} x {} | OVER 1.5 > 90'.format(homeTeam, awayTeam)
        url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
        results = requests.get(url_base)

    if over_2_5 >= 90:
        text = '{} x {} | OVER 2.5 > 90'.format(homeTeam, awayTeam)
        url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
        results = requests.get(url_base)

    if over_3_5 >= 90:
        text = '{} x {} | OVER 3.5 > 90'.format(homeTeam, awayTeam)
        url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
        results = requests.get(url_base)

    if under_0_5 >= 90:
        text = '{} x {} | UNDER 0.5 > 90'.format(homeTeam, awayTeam)
        url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
        results = requests.get(url_base)

    if under_1_5 >= 90:
        text = '{} x {} | UNDER 1.5 > 90'.format(homeTeam, awayTeam)
        url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
        results = requests.get(url_base)

    if under_2_5 >= 90:
        text = '{} x {} | UNDER 2.5 > 90'.format(homeTeam, awayTeam)
        url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
        results = requests.get(url_base)

    if under_3_5 >= 90:
        text = '{} x {} | UNDER 3.5 > 90'.format(homeTeam, awayTeam)
        url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
        results = requests.get(url_base)