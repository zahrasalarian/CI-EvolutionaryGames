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
        import random
        prob = 0.9
        
        # w1
        noise = np.random.normal(0,0.5,child.nn.w[0].shape)
        rand = random.uniform(0, 1)
        if rand < prob:
            child.nn.w[0] += noise
        # w2 
        noise = np.random.normal(0,0.5,child.nn.w[1].shape)
        rand = random.uniform(0, 1)
        if rand < prob:
            child.nn.w[1] += noise
        # b1
        noise = np.random.normal(0,0.5,child.nn.b[0].shape)
        rand = random.uniform(0, 1)
        if rand < prob:
            child.nn.b[0] += noise
        # b2
        noise = np.random.normal(0,0.5,child.nn.b[1].shape)
        rand = random.uniform(0, 1)
        if rand < prob:
            child.nn.b[1] += noise
        return child


    def generate_new_population(self, num_players, prev_players=None):
        import random, copy
        # in first generation, we create random players
        if prev_players is None:
            return [Player(self.mode) for _ in range(num_players)]

        else:
            # Q tournoment
            Q = 5
            children = []
            # TODO
            # num_players example: 150
            # prev_players: an array of `Player` objects
            for _ in range(num_players):
                random_players = random.sample(prev_players, Q)
                best_player = max(random_players, key=lambda x: x.fitness)
                children.append(self.mutate(copy.deepcopy(best_player)))
            # TODO (additional): a selection method other than `fitness proportionate`
            # TODO (additional): implementing crossover

            new_players = children
            return new_players

    def next_population_selection(self, players, num_players):
        import heapq, random, copy
        #top_k =[]
        #heap = []
        #for i in range(len(players)):
        #    heapq.heappush(heap,(-players[i].fitness, i))
        #for _ in range(num_players):
        #    top_k.append(heapq.heappop(heap)[1])
        #for i in range(len(top_k)):
        #    top_k[i] = players[top_k[i]]
        
        next_pop = []
            # TODO
            # num_players example: 150
            # prev_players: an array of `Player` objects
        if num_players > len(players):
            num_players = len(players)
        max = sum(player.fitness for player in players)
        for _ in range(num_players):
            pick = random.uniform(0, max)
            current = 0
            for prev_player in players:
                current += prev_player.fitness
                if current > pick:
                    m_child = copy.deepcopy(prev_player)
                    next_pop.append(self.mutate(m_child))
                    break

        # TODO
        # num_players example: 100
        # players: an array of `Player` objects

        # TODO (additional): a selection method other than `top-k`
        # TODO (additional): plotting

        return next_pop
