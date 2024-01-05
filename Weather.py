import requests #needs to be downloaded first

base_url = "http://api.openweathermap.org/data/2.5/weather?" 
#^^ foundational part of a URL for all weather info, question mark to be able to add more parameters 

api_key = "c9af738fbb8903a81f645c714d048e0e" 
#^^ Application Programming Interface, allows different software applications to communicate with each other

user_city = input("Enter City: ")

final_url = base_url + "&units=metric&appid=" + api_key + "&q=" + user_city 
#^^ specific URL for what is wanted here, combining variables

response = requests.get(final_url).json() 
#^^ can be printed to show all parts of weather, can then add what data to display

print(response)

''' JavaScript Object Notation, 

based on a subset of the JavaScript programming language 
and is often used to transmit data between a server and a 
web application '''

if response['cod'] == '404': #handeling invalid city input, 404=error and cod=shows the status of a client's request numerically
    print('Sorry, this city cannot be found')

else: #valid city was entered

    weather_data = requests.get(final_url).json()['weather'][0]['main'] # [0] indicates from first element

    temp_data = int(requests.get(final_url).json()['main']['temp']) #removes decimal 

    feels_temp = int(requests.get(final_url).json()['main']['feels_like'])

    print(f"The weather in {user_city} is: {weather_data}")
          
    print(f"The temperature in {user_city} is: {temp_data}°C")

    print(f"The temperature that it feels like in {user_city} is: {feels_temp}°C")
