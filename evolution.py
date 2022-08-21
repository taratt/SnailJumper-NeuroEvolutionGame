import copy
import random
from player import Player
import numpy as np
import logging



class Evolution:
    def __init__(self):
        self.game_mode = "Neuroevolution"
        self.logger = self.stats()

    def next_population_selection(self, players, num_players):
        """
        Gets list of previous and current players (μ + λ) and returns num_players number of players based on their
        fitness value.

        :param players: list of players in the previous generation
        :param num_players: number of players that we return
        """
        # TODO (Implement top-k algorithm here)
        # TODO (Additional: Implement roulette wheel here)
        # TODO (Additional: Implement SUS here)

        # TODO (Additional: Learning curve)

        # players = sorted(players, key=lambda player: player.fitness, reverse=True)
        # fitnesses = [player.fitness for player in players[: num_players]]
        # chosen = self.q_tournament(players,num_players)
        chosen = self.sus(players, num_players)
        fitnesses = [player.fitness for player in chosen]
        self.logger.info(str(max(fitnesses)) + " " + str(sum(fitnesses) / len(fitnesses)) + " " + str(min(fitnesses)))
        # return players[: num_players]
        return chosen
    def generate_new_population(self, num_players, prev_players=None):
        """
        Gets survivors and returns a list containing num_players number of children.

        :param num_players: Length of returning list
        :param prev_players: List of survivors
        :return: A list of children
        """
        first_generation = prev_players is None
        if first_generation:
            return [Player(self.game_mode) for _ in range(num_players)]
        else:
            # TODO ( Parent selection and child generation )
            new_players = []
            # for player in prev_players:
            #     new_players.append(self.clone_player(player))
            #parents = prev_players
            alpha = 0.4
            parents = self.q_tournament(prev_players, num_players)
            print(len(parents))
            print(num_players)
            num_layers = len(parents[0].nn.weights.keys())
            cross = np.random.normal()
            for i in range(int(num_players/2)):
                child1 = self.clone_player(parents[i])
                child2 = self.clone_player(parents[i + 1])
                mutation = 1
                # mutation = np.random.normal()
                if mutation == 1:
                    for j in range(num_layers):
                        child1.nn.weights[j] +=0.5 * np.random.normal(size= child1.nn.weights[j].shape)
                        child1.nn.biases[j] += 0.5 * np.random.normal(size= child1.nn.biases[j].shape)
                # mutation = np.random.normal()
                if mutation ==1:
                    for j in range(num_layers):
                        child2.nn.weights[j] += 0.5 * np.random.normal(size=child2.nn.weights[j].shape)
                        child2.nn.biases[j] += 0.5 * np.random.normal(size=child2.nn.biases[j].shape)

                cross = np.random.normal()
                if cross < 0.4:
                    for j in range(num_layers):
                        child1.nn.weights[j] = alpha * parents[i].nn.weights[j] + (1 - alpha) * \
                                               parents[i + 1].nn.weights[j]
                        child2.nn.weights[j] = (1 - alpha) * parents[i].nn.weights[j] + alpha * \
                                               parents[i + 1].nn.weights[j]
                        child1.nn.biases[j] = alpha * parents[i].nn.biases[j] + (1 - alpha) * parents[i + 1].nn.biases[
                            j]
                        child2.nn.biases[j] = (1 - alpha) * parents[i].nn.biases[j] + alpha * parents[i + 1].nn.biases[
                            j]

                new_players.append(child1)
                new_players.append(child2)
            return new_players

    def clone_player(self, player):
        """
        Gets a player as an input and produces a clone of that player.
        """
        new_player = Player(self.game_mode)
        new_player.nn = copy.deepcopy(player.nn)
        new_player.fitness = player.fitness
        return new_player

    def q_tournament(self, players, num_needed):
        q = 2
        chosen = []
        for i in range(num_needed):
            q_rands = []
            for j in range(q):
                q_rands.append(players[random.randint(0,len(players) - 1)])
            chosen.append(max(q_rands, key=lambda rand: rand.fitness))

        return chosen

    def sus(self, players, num_needed):
        fitnesses = np.array([player.fitness for player in players])
        fitnesses = fitnesses/sum(fitnesses)
        chosen = []
        for i in range(len(fitnesses)-1):
            fitnesses[i+1] += fitnesses[i]
        for i in range(num_needed):
            rand = random.random()
            for j in range(len(fitnesses)):
                if rand < fitnesses[j]:
                    chosen.append(players[j])
                    break


        return chosen



    def stats(self):
        logging.basicConfig(filename="generations.txt", format='%(message)s', filemode='w')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger



