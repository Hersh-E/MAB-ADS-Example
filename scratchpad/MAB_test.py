
from random import random, uniform, choice


from py_classes.epsilon_greedy_class import Creative

Creative.reset_ads()

ad_1 = Creative('puppies', random(), uniform(1,10))
ad_2 = Creative('cats', random(), uniform(1,10))
ad_3 = Creative('elephants', random(), uniform(1,10))
ad_4 = Creative('bears', random(), uniform(1,10))
ad_5 = Creative('rhinos', random(), uniform(1,10))
# ad_5 = Creative('sports', .2, 10)


ad_1.rate = random()
ad_1.reward = uniform(1,10)
ad_2.rate = random()
ad_2.reward = uniform(1,10)
ad_3.rate = random()
ad_3.reward = uniform(1,10)
ad_4.rate = random()
ad_4.reward = uniform(1,10)

# Creative.history.head(20)
#
# Creative.history.tail()


Creative.simulate_n(epsilon=0.7, n_steps=500)

Creative.history[['eg_rev', 'rand_rev']].sum(axis=0)

import plotly.express as px

running_total = Creative.history[['eg_rev', 'rand_rev']].cumsum()

x = running_total.stack().reset_index().rename({'level_0':'step', 'level_1':'type', 0:'Running Total'}, axis=1)

px.line(x, x='step', y="Running Total", color='type')



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

ad_1.reward
ad_2.reward
ad_3.reward
ad_4.reward
ad_5.reward



ad_1.calc_rate()

ad_1.calc_Q()
ad_1.displays
ad_2.displays
ad_3.displays
ad_4.displays

x = [1,2,3]
y = ['a', 'b', 'c']

for n, l in enumerate(zip(x,y)):
    print(f'{n}: {l}')


x = 1

x += 1 if not True else 0
x
x += 1 if not False else 0
x


import pandas as pd
x = pd.DataFrame(columns=['eg_pick', 'ran_pick', 'eg_rev', 'rand_rev'], index=[0], data=[[0,0,0,0]])

step = 1
x.loc[1,'eg_pick'] = 1
x.loc[1,'ran_pick'] = 2
x

x.index.max()
