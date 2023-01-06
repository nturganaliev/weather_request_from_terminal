# weather_request_from_terminal
Script to get weather information for interested location from terminal.


### request_weather
Location and params should be provided to get weather information.
For testing purposes, function can be run without any parameter.


### Usage
```python
request_weather(location='Bishkek', params={'FMnqT': '', 'lang': 'ru'})
```
And you will get the following result on terminal:</br>

![image](https://user-images.githubusercontent.com/4350960/210967359-bd80022f-7dfc-4f8b-ab37-bc1fc7a73c8b.png)

To learn what is the purpose of key 'FMnqT', look below.
<ul>
    <li>1. F - do not show the "Follow" line.</li>
    <li>2. M - show wind speed in m/s</li>
    <li>3. n - narrow version (only day and night)</li>
    <li>4. q - quiet version (no "Weather report" text)</li>
    <li>5. T - switch terminal sequences off (no colors)</li>
</ul>
  
For detailed help, please visit [wttr.in](https://wttr.in/:help)
