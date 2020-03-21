import requests
import json #to convert python object to strings and make json readable
from datetime import datetime #to make date time readable



# Names of the people currently at International Space Station
response1 = requests.get("http://api.open-notify.org/astros.json")
print("\nResponse 1 status code: ",response1.status_code, "\n")



# print(response1.json(), "\n\n")


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

print("Astronauts currently at ISS: \n")
jprint(response1.json())



""" This endpoint tells us the next times that the 
    international space station will pass over a 
    given location on the earth. """

# Washington DC
parameters = {
    "lat": 38.9072,
    "lon": 77.0369
}

response2 = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
print("\nResponse 2 status code: ", response2.status_code, "\n")


print("Times when ISS will pass over a given location: ", "\n")
jprint(response2.json())


# extracting the response dictionary 
print("\nThe response dictionary: \n")

pass_times = response2.json()['response']
jprint(pass_times)
#print("type of passtimes: ", type(pass_times))

# loop to extract just the five risetime values
risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print("\nRise times: \n")
#print("type of risetimes: ",type(risetimes))

times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)

print("\n------------------")

