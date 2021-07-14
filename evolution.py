from nltk.tokenize.api import TokenizerI
from player import Player
import numpy as np
from config import CONFIG


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
        return child
        #pass


    def generate_new_population(self, num_players, prev_players=None):

        # in first generation, we create random players
        if prev_players is None:
            return [Player(self.mode) for _ in range(num_players)]

        else:
            # TODO
            # num_players example: 150
            # prev_players: an array of `Player` objects
            import heapq, copy
            top_k =[]
            heap = []
            children = []
            for i in range(len(prev_players)):
                heapq.heappush(heap,(-prev_players[i].fitness, i))
            for _ in range(num_players):
                top_k.append(heapq.heappop(heap)[1])
            for i in range(len(top_k)):
                top_k[i] = prev_players[top_k[i]]
            for player in top_k:
                child = copy.deepcopy(player)
                children.append(self.mutate(child))

            # TODO (additional): a selection method other than `fitness proportionate`
            # TODO (additional): implementing crossover

            new_players = children
            return new_players

    def next_population_selection(self, players, num_players):
        import heapq
        top_k =[]
        heap = []
        for i in range(len(players)):
            heapq.heappush(heap,(-players[i].fitness, i))
        for _ in range(num_players):
            top_k.append(heapq.heappop(heap)[1])
        for i in range(len(top_k)):
            top_k[i] = players[top_k[i]]
        # TODO
        # num_players example: 100
        # players: an array of `Player` objects

        # TODO (additional): a selection method other than `top-k`
        # TODO (additional): plotting

        return top_k
