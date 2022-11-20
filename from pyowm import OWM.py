from pyowm import OWM
from twilio.rest import Client

owm = OWM('fba23ae9763c741369cdbb1f696d804e')
forcast = OWM.weather_at_place("London, GB")
weather = forcast.get_weather()


def umbrellaNotRequired():
    rain = weather.get_rain()
    status = weather.get_status().lower().strip()
    if len(rain) == 0 or status == "Clear":
        return True

def send_weather_sms():
    client = Client(SID, AUTH)
        if owm_API_online:
        temperture = weather.get_temperture("fahrenheit")["temp"]
        humidity = weather.get_humidity()
            if umbrellaNotRequired():
                client.messages.create(
                from_= 3466332589
                TO= 832389XXXX
                body='''
                DO NOT NEED A UMBRELLA! WEATHER DETAILS:
                1. HUMIDITY:{humidity} %,
                2. TEMP:{temperture} F
                '''
        )
        Else:
                client.messages.create(
                from_= 3466332589
                TO= 832389XXXX
                body='''
                DO NEED A UMBRELLA!
                '''
        )
if __name__ == '__main__':
    send_weather_sms()