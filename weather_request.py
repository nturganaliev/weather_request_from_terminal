import requests

locations = ['Лондон', '~Шереметьево', 'Череповец']

# To learn what is the purpose of key 'FMnqT', look below.
# F - do not show the "Follow" line.
# M - show wind speed in m/s
# n - narrow version (only day and night)
# q - quiet version (no "Weather report" text)
# T - switch terminal sequences off (no colors)
# For detailed help, please visit https://wttr.in/:help
parameters = {'FMnqT': '', 'lang': 'ru'}


def request_weather(url='https://wttr.in/',
                    location='Bishkek',
                    params=None):
    try:
        response = requests.get(url=f"{url}{location}", params=params)
        return (response.text
                if response.ok
                else response.status_code)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


if __name__ == '__main__':
    for location in locations:
        print(
            request_weather(
                location=location,
                params=parameters
                )
            )
