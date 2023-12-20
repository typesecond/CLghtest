import requests
from ossapi import Ossapi, UserLookupKey, GameMode, RankingType, ScoringType, UserCompact, ScoreType


response = requests.get('https://api.github.com')


print(response)

print(response.status_code)

if response.status_code == 200: 
    print("Operational")
else:
    print('Error')





client_id = 28923
client_secret = 'pv6WR4HNI4yKlL7vWuvtDx2Owy8qUf2aoNpsT55v' 

api = Ossapi(client_id, client_secret)


user = api.user(29312082)
print(user.username) 

recact = api.user_recent_activity(29312082, limit=1)


usscore = api.user_scores(29312082, ScoreType.BEST)
print(usscore)
print(recact)


api_key = '333ae01adeae77ecc84e6a7dec40fc3b41da9e7e'

params = {
    'apikey': api_key,  # The parameter name 'apikey' may vary depending on the API
    # ... other parameters if any

}

response = requests.get("https://osu.ppy.sh/api/v2/rankings/mania/performance?country=JP&filter=all&variant=4k", params=params)
data = response.json

print(data)
print(response) 
