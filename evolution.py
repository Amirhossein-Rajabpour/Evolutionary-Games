from player import Player
import numpy as np
from config import CONFIG
import random


class Evolution():

    def __init__(self, mode):
        self.mode = mode

    # calculate fitness of players
    def calculate_fitness(self, players, delta_xs):
        for i, p in enumerate(players):
            p.fitness = delta_xs[i]

    def mutate(self, child):

        # TODO
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

        # TODO (additional): plotting

        return np_selected_players
        # return players[: num_players]
