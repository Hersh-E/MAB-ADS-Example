
from random import random, uniform, choice

class Creative():
    ad_list = []

    def __init__(self, name, rate=random(), reward=uniform(1,10)):
        self.name = name
        self.reward = reward
        self.rate = rate
        self.sum_rewards = 0.0
        self.clicks = 0
        self.displays = 0
        self.Q = 0
        self.__class__.ad_list.append(self)

    def is_clicked(self):
        self.displays += 1
        if random() < self.rate:
            self.clicks += 1
            return True
        else:
            return False

    def get_reward(self):
        if self.is_clicked():
            self.sum_rewards += self.reward
            return self.reward
        else:
            return 0

    def calc_Q(self):
        if self.displays == 0:
            return 0
        else:
            self.Q = self.sum_rewards / self.displays
            return self.Q

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
    def reset_ads(cls):
        cls.ad_list = []



ad_1 = Creative('puppies')
ad_2 = Creative('cats')
ad_3 = Creative('elephants')
ad_4 = Creative('bears')
ad_5 = Creative('sports', .2, 10)

for i in range(100):
    ad = Creative.epsilon_greedy(.5)
    if ad.get_reward() > 0:
        print(f"{ad.name}: Yay! Making Money")
    else:
        print(f"{ad.name}: ... bust")

ad_1.Q
ad_2.Q
ad_3.Q
ad_4.Q
ad_5.Q

ad_1.displays
ad_2.displays
ad_3.displays
ad_4.displays
