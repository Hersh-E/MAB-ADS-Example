import pandas as pd
from random import random, uniform, choice

class Creative():
    ad_list = []
    history = pd.DataFrame(columns=['eg_pick', 'rand_pick', 'eg_rev', 'rand_rev'], index=[0], data=[[0,0,0,0]])

    def __init__(self, name, rate=random(), reward=uniform(1,10)):
        self.name = name
        self.reward = reward
        self.rate = rate
        self.sum_rewards = 0.0
        self.clicks = 0
        self.displays = 0
        self.Q = 0
        self.__class__.ad_list.append(self)

    def is_clicked(self, rand_trial=False):
        self.displays += 1 if not rand_trial else 0
        if random() < self.rate:
            self.clicks += 1 if not rand_trial else 0
            return True
        else:
            return False

    def get_reward(self, rand_trial=False):
        if self.is_clicked(rand_trial):
            self.sum_rewards += self.reward if not rand_trial else 0
            return self.reward
        else:
            return 0

    def calc_Q(self):
        if self.displays == 0:
            return 0
        else:
            self.Q = self.sum_rewards / self.displays
            return self.Q

    def calc_rate(self):
        if self.displays == 0:
            return 0
        else:
            return (self.clicks / self.displays)


    @classmethod
    def epsilon_greedy(cls, epsilon):
        if random() < epsilon:
            return choice(cls.ad_list)
        else:
            max = -1
            for ad in cls.ad_list:
                if ad.calc_Q() > max:
                    max = ad.Q
                    top_performer = ad
            return top_performer

    @classmethod
    def random_selection(cls):
        return choice(cls.ad_list)

    @classmethod
    def simulate_n(cls, epsilon=0.5, n_steps=100):
        start = cls.history.index.max() + 1

        for step in range(start, start + n_steps):
            eg_ad = cls.epsilon_greedy(epsilon)
            rand_ad = cls.random_selection()

            cls.history.loc[step, 'eg_pick'] = eg_ad.name
            cls.history.loc[step, 'rand_pick'] = rand_ad.name
            cls.history.loc[step, 'eg_rev'] = eg_ad.get_reward()
            cls.history.loc[step, 'rand_rev'] = rand_ad.get_reward(rand_trial=True)



    @classmethod
    def reset_ads(cls):
        cls.ad_list = []
        cls.history = pd.DataFrame(columns=['eg_pick', 'rand_pick', 'eg_rev', 'rand_rev'], index=[0], data=[[0,0,0,0]])
