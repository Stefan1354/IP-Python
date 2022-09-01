'''2.Da se sazdade programa na Python koqto da preobrazuva Python obekt v json danni. Da se izpolzva metoda json.dumps.'''

import json

dict = {
    "country": "Serbia",
    "capital_city": "Belgrade"
}

with open("21.12.json", 'w') as file:
    json.dump(dict, file, indent = 4)

