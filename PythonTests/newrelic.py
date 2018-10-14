import requests

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://insights-api.newrelic.com/v1/accounts/713892/query?nrql=SELECT%20uniques%28userId%29%20FROM%20segment_foxapp_android', headers=headers)


headers = {
    'Accept': 'application/json',
    'X-Query-Key': 'JI9uQB1tE6dlhfZiPIPB_1vSzizS-jaI',
}

params = (
    ('nrql', 'SELECT uniques(userId) FROM segment_foxapp_android'),
)

response = requests.get('https://insights-api.newrelic.com/v1/accounts/713892/query', headers=headers, params=params)

print (response.text)