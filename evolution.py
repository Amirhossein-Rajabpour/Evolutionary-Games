from player import Player
import numpy as np
from config import CONFIG
import random
import pandas as pd
import copy

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

        # child: an object of class `Player`
        mean = 0
        sd = 0.2
        noise_W1 = np.random.normal(mean, sd, child.nn.W_1.shape)
        noise_W2 = np.random.normal(mean, sd, child.nn.W_2.shape)
        child.nn.W_1 += noise_W1
        child.nn.W_2 += noise_W2
        return child


    def generate_new_population(self, num_players, prev_players=None):

        # in first generation, we create random players
        if prev_players is None:
            return [Player(self.mode) for _ in range(num_players)]

        else:
            # num_players example: 150
            # prev_players: an array of `Player` objects
            # make a copy from prev_players
            copied_players = copy.deepcopy(prev_players)
            new_players = []

            # sort the list so that better players have more chances to be selected for mutation
            # copied_players.sort(key=lambda x: x.fitness, reverse=True)
            copied_players = sorted(copied_players, key=lambda x: x.fitness, reverse=True)

            # we should iterate until new_players array becomes full
            is_list_full = False
            while not is_list_full:
                for p in range(len(prev_players)):
                    new_pop = copied_players[p]
                    # copied_players = np.delete(copied_players, 0)

                    # mutate copied players
                    mutation_probability = 0.6
                    random_prob = random.random()
                    if random_prob < mutation_probability:
                        mutated_new_pop = self.mutate(new_pop)
                        # append to new_players
                        new_players.append(mutated_new_pop)
                        if len(new_players) >= num_players:
                            is_list_full = True
                            break

            # TODO (additional): a selection method other than `fitness proportionate`
            # TODO (additional): implementing crossover

            # new_players = np.array(new_players)
            return new_players

    def return_scores(self, array_of_players):
        scores = [p.fitness for p in array_of_players]
        return scores

    def next_population_selection(self, players, num_players):

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

        return selected_players
        # return players[: num_players]
