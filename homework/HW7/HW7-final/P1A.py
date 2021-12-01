from Markov import Markov

if __name__ == "__main__":
    weather_today = Markov()
    weather_today.load_data(file_path='./weather.csv')
    print(weather_today.get_prob('cloudy', 'windy'))
    print(weather_today.get_prob('sunny', 'cloudy'))