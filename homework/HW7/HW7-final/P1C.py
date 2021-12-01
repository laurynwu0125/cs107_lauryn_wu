from Markov import Markov, MarkovIterator


if __name__ == "__main__":
    days = 7
    trials = 100
    city_weather = {
        'New York': 'rainy',
        'Chicago': 'snowy',
        'Seattle': 'rainy',
        'Boston': 'hailing',
        'Miami': 'windy',
        'Los Angeles': 'cloudy',
        'San Francisco': 'windy' }
    city_pred = {}

    for city in city_weather:
        weather = Markov(city_weather.get(city))
        predictions = weather.get_weather_for_day(days, trials)
        freq = {i: predictions.count(i) for i in set(predictions)}
        print(city, ":", freq)
        max_key = max(freq, key=freq.get)
        city_pred[city] = max_key

    print("\n Most likely weather in seven days")
    print("------------------------------------")
    for city in city_pred:
        print(city, ":", city_pred.get(city))
