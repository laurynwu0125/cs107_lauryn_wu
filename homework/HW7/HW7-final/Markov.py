import numpy as np
import random

class Markov:
    def __init__(self, day_zero_weather=None): # You will need to modify this header line later in Part C
        self.data = []
        # map the weathers to indices
        self.dict = {"sunny":0, "cloudy":1, "rainy":2, "snowy":3, "windy":4, "hailing":5}
        # if no day 0 weather is given, select a random weather
        if day_zero_weather == None:
            day_zero_weather = random.choice(list(self.dict.keys()))
        self.day_zero_weather = day_zero_weather
        self.load_data()

    def load_data(self, file_path='./weather.csv'):
        # load data from file into a 2d numpy array
        self.data = np.genfromtxt(file_path, delimiter=',')

    def get_prob(self, current_day_weather, next_day_weather):
        # get the indices for the weathers
        curIndex = self.dict.get(current_day_weather.lower())
        nextIndex = self.dict.get(next_day_weather.lower())
        # raise an exception if a weather is not valid
        if curIndex == None or nextIndex == None:
            raise Exception("Weather is not one of the possible six strings specified")
        # return the transition probability
        return self.data[curIndex][nextIndex]

    def __iter__(self):
        return MarkovIterator(self.day_zero_weather, self.dict, self.data)

    def _simulate_weather_for_day(self, day):
        # track the weather at each iteration
        curWeather = self.day_zero_weather
        weatherPred = iter(self.__iter__())
        # iterate using the iterator for day number of iterations
        for i in range(day):
            curWeather = next(weatherPred)
        return curWeather

    def get_weather_for_day(self, day, trials=100):
        # array of predictions for the weather on the day number day
        predictions = []
        for i in range(trials):
            predictions.append(self._simulate_weather_for_day(day))
        return predictions


class MarkovIterator:
    def __init__(self, curWeather, dict, data):
        # keep track of the weather at the current iteration
        self.curWeather = curWeather
        # mapping of the weather to index
        self.dict = dict
        # 2d numpy array of transition probabilities
        self.data = data
        # keep track of the weather's index at the current iteration
        self.curIndex = self.dict.get(self.curWeather.lower())

    def __iter__(self):
        return self

    def __next__(self):
        # get the transition probabilities for the current weather
        probs = self.data[self.curIndex]
        # select the next weather index using the weighted probabilities
        self.curIndex = np.random.choice(list(self.dict.values()), 1, p=probs)[0]
        # get the name of the weather state from the index
        for weather in self.dict.keys():
            if self.dict.get(weather) == self.curIndex:
                self.curWeather = weather
        return self.curWeather
