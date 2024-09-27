
# Flight Deals

This program sends you a mail when lowest price is available for a flight from your nearest airport to the locations present in the google sheet along with their respective lowest price recored till now.(You can modifiy the sheet for your liking)

## Description

-- First user has to enter their details in google forms and those who fill the google forms with valid info will get the mail.

-- After executing the program the user has to enter details such as "Nearest airport IAIA code","Departure date" and "Return date".

-- Based on user input, the program will find cheapest flight(non-stop fight for single adult passenger) from user's iata code to all the locations in the google sheet.

-- If there is no flights available then it searches for multi-stop flights.

-- If the "Current lowest price" is lower than the "Lowest price recorded" or "User defined price" then it will send mails to all the users who provided their valid mail-id in google forms.

-- The message contains "Current cheapest price","Origin location code", "Destination location code", "Departure date", "Return Date" and "number of stops" if it stops.

## API Reference

#### Amadeus
```http
  https://test.api.amadeus.com/v1/security/oauth2/token
```
```http
  https://test.api.amadeus.com/v2/shopping/flight-offers
```
```http
  https://test.api.amadeus.com/v1/reference-data/locations/cities
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `amadeus_key` | `string` | **Required**. Your API key |
| `amadeus_secret ` | `string` | **Required**. Your secret key |
| `amadeus_access_token ` | `string` | **Required**. Your access token |


#### Twilio
```http
  https://console.twilio.com/us1/develop/sms/try-it-out/send-an-sms
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `auth_token` | `string` | **Required**. Your API key |
| `account_sid`      | `string` | **Required**. Your acc ID

#### Sheety
```http
  https://sheety.co/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `sheety_bearer_FD ` | `string` | **Required**. Your authenticator|

## Environment Variables

To run this project, you will need to add the following environment variables in your .env file

`password`(SMTPLIB)

`account_sid`

`auth_token`

`from_`

`to`

`amadeus_key`

`amadeus_secret`

`amadeus_access_token`

`sheety_bearer_FD`


## Links

 - [Twilio to work on Free accounts with the proxy](https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/)

 - [Google Form](https://forms.gle/x7H2GgbDmGRNaLAr8)

 - [Google sheet](https://docs.google.com/spreadsheets/d/1cSYPuO9dFCNcA-4__9NmfLpvmXwMo0CYiIEK5323wbU/edit?resourcekey=&gid=0#gid=0)
