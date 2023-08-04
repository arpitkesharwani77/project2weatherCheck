import requests
flag=True
while flag:
    BASE_URL= "http://api.openweathermap.org/data/2.5/weather?"
    API_KEY= "bd6e4c77538b21fea2818fbc563d6480" 
    CITY= input("Please Enter Your City Name: " ) 
    def tempchnage_k_to_c(kelvin): 
        celsius=kelvin-273.15
        return celsius
    url=BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    response=requests.get(url).json()

    if response["cod"]==200:
        temp_kelvin=response["main"]["temp"]
        temp_celsius=tempchnage_k_to_c(temp_kelvin)
        rounded_temp_celsius=round(temp_celsius,2) 
        print("The temperature of ", CITY , "is :" , rounded_temp_celsius, "°C")

    else:
        print("ERROR....INVALID CITY")

    choice=input("\n If you want to check temperature of another city type 'yes'\n otherwise type 'no': ")
    if choice=="yes" or choice=="Yes" or choice=="YES":
        flag=True
    else:
        print("THANKS FOR USING THIS WIDGET")
        flag=False    

