import requests
from twilio.rest import Client

# Info to get access to weather data from openweathermap.org
OWN_End_point = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = '#################'
# lat_istambul = 41.038870  # cause it's raining
# long_istambul = 28.981420
# This lat and long numbers are for mexico city :
LAT = 19.432680
LONG = -99.134209


# Info to get access to SMS sender by twilio

account_sid = 'ACc6096965c9fb86011af5fd28baa46fca'
auth_token = '####################'
client = Client(account_sid, auth_token)
my_twilio_number = '##########'
my_number = '+########'  # Note: You need to verify this number in Twilio
weather_params = {
    'lat': LAT,    # 17.551480, this is for Chilpancingo
    'lon': LONG,   # -99.500570,
    'appid': api_key,
    'exclude': 'current,minutely,daily'
}


response = requests.get(OWN_End_point, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]  # In weather_slice just contains the first 12 hours
# print(weather_data['hourly'][0]['weather'][0]['id'])  # This give me the id status, if id statys < 700, it's raining
will_rain = False
for hour in weather_slice:
    condition_code = hour['weather'][0]['id']

if int(condition_code) < 700:
       will_rain = True

if will_rain:
    # print('Bring an umbrella')
    message = client.messages \
        .create(
        body="They buddy. Today it's gonna rain, you'd better bring an umbrella.☔",
        from_=my_twilio_number,
        to=my_number
    )
    print(message.status)

