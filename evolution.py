from player import Player
import numpy as np
from config import CONFIG
import random
import pandas as pd


class Evolution():

    def __init__(self, mode):
        self.mode = mode
        self.arr_max_fitness = []
        self.arr_avg_fitness = []
        self.arr_min_fitness = []

    # calculate fitness of players
    def calculate_fitness(self, players, delta_xs):
        for i, p in enumerate(players):
            p.fitness = delta_xs[i]

    def find_max_fitness(self, array_of_players):
        array_of_players.sort(key=lambda x: x.fitness, reverse=True)
        return array_of_players[0].fitness

    def find_min_fitness(self, array_of_players):
        array_of_players.sort(key=lambda x: x.fitness, reverse=False)
        return array_of_players[0].fitness

    def find_avg_fitness(self, array_of_players):
        sum_fitness = 0
        for p in array_of_players:
            sum_fitness += p.fitness
        return sum_fitness / len(array_of_players)

    def mutate(self, child):

        # TODO add a Gaussian noise
        # child: an object of class `Player`
        pass


    def generate_new_population(self, num_players, prev_players=None):

        # in first generation, we create random players
        if prev_players is None:
            return [Player(self.mode) for _ in range(num_players)]

        else:

            # TODO
            # num_players example: 150
            # prev_players: an array of `Player` objects

            # TODO (additional): a selection method other than `fitness proportionate`
            # TODO (additional): implementing crossover

            new_players = prev_players
            return new_players

    def return_scores(self, array_of_players):
        scores = [p.fitness for p in array_of_players]
        return scores

    def next_population_selection(self, players, num_players):

        # num_players example: 100
        # players: an array of `Player` objects

        selected_players = []
        player_fitness_arr = self.return_scores(players)
        selected_players += random.choices(list(players), weights=player_fitness_arr, k=num_players)
        np_selected_players = np.array(selected_players)

        # write to file
        self.arr_max_fitness.append(self.find_max_fitness(players))
        self.arr_min_fitness.append(self.find_min_fitness(players))
        self.arr_avg_fitness.append(self.find_avg_fitness(players))

        fitness_data = {'max': self.arr_max_fitness,
                        'avg': self.arr_avg_fitness,
                        'min': self.arr_min_fitness
                        }
        fitness_DF = pd.DataFrame(fitness_data)
        fitness_DF.to_csv('evolution_info.csv')

        return np_selected_players
        # return players[: num_players]
