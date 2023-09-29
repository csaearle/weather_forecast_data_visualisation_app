import requests

APIkey = "6fa1cfe818bc1314a6610c4ca35c9cc2"
def get_data(place, forecast_days=None, plot_kind=None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?' \
          f'q={place}&appid={APIkey}'
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if plot_kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if plot_kind == "Sky conditions":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data

if __name__ =="__main__":
    print(get_data(place="Tokyo", forecast_days=3, plot_kind="Temperature"))