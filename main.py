import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUTN_SID")
auth_token =os.environ.get("AUTH_TOKEN")
latitude = os.environ.get("lAT")
longitude = os.environ.get("lON")

weather_parameters = {
    "lat": latitude,
    "lon": longitude,
    "exclude": "current,minutely,daily,",
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

hourly_weather_list = weather_data["hourly"][:12]
bring_umbrella = None

for data in hourly_weather_list:
    weather_id = data["weather"][0]["id"]
    if weather_id < 700:
        bring_umbrella = True
        break

if bring_umbrella:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Its going to rain today. Remember to bring an ☔",
        from_=os.environ.get("SENDER_NO"),
        to=os.environ.get("RECEIVER_NO")
    )

    print(message.status)


