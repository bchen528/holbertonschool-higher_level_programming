# 0x15. Javascript - Web JQuery

[0-script.js](0-script.js) - updates the text color of the HTML tag HEADER to red (#FF0000)

[1-script.js](1-script.js) - updates the text color of the HTML tag HEADER to red (#FF0000)

[2-script.js](2-script.js) - updates the text color of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header

[3-script.js](3-script.js) - adds the class red to the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header

[4-script.js](4-script.js) - toggles the class of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#toggle_header

[5-script.js](5-script.js) - adds a LI element to a list when the user clicks on the tag DIV#add_item

[6-script.js](6-script.js) - updates the text of the HTML tag HEADER to “New Header!!!” when the user clicks on DIV#update_header

[7-script.js](7-script.js) - fetches and replaces the name of this URL: https://swapi.co/api/people/5/?format=json

[8-script.js](8-script.js) - fetches and lists all movies title by using this URL: https://swapi.co/api/films/?format=json

[9-script.js](9-script.js) - fetches and prints the San Francisco wind speed by using this URL: https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22San%20Francisco%2C%20CA%22)&format=json

[100-script.js](100-script.js) - updates the text color of the HTML tag HEADER to red (#FF0000) and script works when imported from the HEAD tag

[101-script.js](101-script.js) - adds, removes and clears LI elements from a list when the user clicks and script works when imported from HEAD tag

[102-script.js](102-script.js) - fetches and prints the wind speed by using this URL: https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22:city_name%22)&format=json, where:
  * wind speed must be display in the HTML tag `DIV#wind_speed`
  * city name must be the value of the tag `INPUT#city_search`
  * wind speed must be fetch when the user clicks on `INPUT#btn_search`

[103-script.js](103-script.js) - fetches and prints the wind speed by using this URL: https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22:city_name%22)&format=json, where:
  * wind speed must be display in the HTML tag `DIV#wind_speed`
  * city name must be the value of the tag `INPUT#city_search`
  * wind speed must be fetch when the user clicks on `INPUT#btn_search` OR press ENTER when the focus is on `INPUT#city_search`
