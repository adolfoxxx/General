import requests

# Get New Relic Data

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

# Get matching IDs
print (response.text)

l1=[1,2,3]
l2=[1,3,4]
s3=set(l1).intersection(set(l2))
l3=list(s3)
print(l3)

# Fin