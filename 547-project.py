#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 23:00:35 2019

@author: rohanghuge, wenfeitang
"""

import numpy as np
import time
import matplotlib.pyplot as plt 


# default option cost
phi = 20

# setting the structure: S, G, d
m = 1000
k = 5

# set number of agents to 3000
N = 800 

# setting a permutation over the agents
pi = np.random.permutation(N)

# upper and lower bounds for max distance (can vary these)
m_lb = 200
m_ub = 500

# sample m_j values for each agent uniformly at random in range (200, 500, 50)
max_distances = np.round(np.random.uniform(200, 500, N))

# set goals for each agent at random
elements = [0, 1, 2, 3, 4]
probabilities = [0.3, 0.2, 0.15, 0.15, 0.2]
#probabilities = [0.2, 0.2, 0.2, 0.2, 0.2]
goals = np.random.choice(elements, N, p=probabilities)


# prefernce of an agent based on max-distance
def pref(j, s):
    if 0 <= s < 300: 
        if goals(j) == 1 or goals(j) == 2:
            return phi+5
        else: return 0
        
    if 300 <= s < 400: 
        if goals(j) == 3 or goals(j) == 4:
            return phi+5
        else: return 0
        
    if 400 <= s < 500: 
        if goals(j) == 5:
            return phi+5
        else: return 0
    return 0
    

# begin simulation
maxdist_profit = []
lin_profit = []

maxdist_profit_res = []
lin_profit_res = []

N = 1500
prob=1
#for N in range(100, 2000, 100):
#for prob in [0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
for res_prob in [0.1, 0.15, 0.2, 0.25, 0.3]:
    print(res_prob)
    
    # set goals for each agent at random
    elements = [0, 1, 2, 3, 4]
    probabilities = [0.3, 0.2, 0.15, 0.15, 0.2]
    #probabilities = [0.2, 0.2, 0.2, 0.2, 0.2]
    goals = np.random.choice(elements, N, p=probabilities)

    days = 10
    price = 20
    soc_welfare = np.zeros(days)
    profit = np.zeros(days)
    slots_filled = np.zeros(days)
    
    for i in range(days):
        
        matchings = np.zeros(N)
        pi = np.random.permutation(N)
        slots = np.zeros(m)
        
        for agent in pi:
            
            shows_up = np.random.binomial(1, prob)
            if shows_up == 0:
                continue
            
            #print('Agent ', agent, ' arrived')
            goal = goals[agent]
            matched = 0
            s = 'Agent ' + str(agent) + ' arrived.'
            #print(s)
            
            if goal == 0 or goal == 1:
                for k in range(int(0.6*m)):
                    if slots[k] == 0 and matched == 0:
                        matchings[agent] = k
                        slots[k] = 1
                        profit[i] = profit[i] + price
                        matched = 1
                        s = 'Agent ' + str(agent) + ' found a slot.'
                        #print(s)
                if matched == 0:
                    s = 'Agent ' + str(agent) + ' did not find a slot.'
                    #print(s)
                    profit[i] = profit[i] + 5
                
            if goal == 2 or goal == 3:
                for k in range(int(0.6*m), int(0.8*m)):
                    if slots[k] == 0 and matched == 0:
                        matchings[agent] = k
                        slots[k] = 1
                        profit[i] = profit[i] + price
                        matched = 1
                        s = 'Agent ' + str(agent) + ' found a slot.'
                        #print(s)
                if matched == 0:
                    s = 'Agent ' + str(agent) + ' did not find a slot.'
                    #print(s)
                    profit[i] = profit[i] + 5
                    
            if goal == 4:
                for k in range(int(0.8*m), m):
                    if slots[k] == 0 and matched == 0:
                        matchings[agent] = k
                        slots[k] = 1
                        profit[i] = profit[i] + price
                        matched = 1
                        s = 'Agent ' + str(agent) + ' found a slot.'
                        #print(s)
                if matched == 0:
                    s = 'Agent ' + str(agent) + ' did not find a slot.'
                    #print(s)
                    profit[i] = profit[i] + 5
                    
        slots_filled[i] = sum(slots)
            
    maxdist_profit = maxdist_profit + [np.mean(profit)]    
        
        
    # begin simulation 2 - variable prices
    days = 10
    price = 20
    soc_welfare2 = np.zeros(days)
    profit2 = np.zeros(days)
    slots_filled2 = np.zeros(days)
    
        
    for i in range(days):
        
        matchings2 = np.zeros(N)
        pi = np.random.permutation(N)
        slots = np.zeros(m)
        
        for agent in pi:
            
            shows_up = np.random.binomial(1, prob)
            if shows_up == 0:
                continue
            
            #print('Agent ', agent, ' arrived')
            goal = goals[agent]
            matched = 0
            s = 'Agent ' + str(agent) + ' arrived.'
            #print(s)
            
            if goal == 0 or goal == 1:
                for k in range(int(0.6*m)):
                    if slots[k] == 0 and matched == 0:
                        matchings[agent] = k
                        slots[k] = 1
                        profit2[i] = profit2[i] + price
                        matched = 1
                        s = 'Agent ' + str(agent) + ' found a slot.'
                        #print(s)
                
                for k in range(int(0.6*m), m):
                    if slots[k] == 0 and matched == 0:
                        matchings[agent] = k
                        slots[k] = 1
                        profit2[i] = profit2[i] + price - 5 # offer cheaper price to agent for other parking
                        matched = 1
                        s = 'Agent ' + str(agent) + ' found a slot.'
                        #print(s)
                        
                if matched == 0:
                    s = 'Agent ' + str(agent) + ' did not find a slot.'
                    #print(s)
                    profit2[i] = profit2[i] + 5
                
            if goal == 2 or goal == 3:
                for k in range(int(0.6*m), int(0.8*m)):
                    if slots[k] == 0 and matched == 0:
                        matchings[agent] = k
                        slots[k] = 1
                        profit2[i] = profit2[i] + price
                        matched = 1
                        s = 'Agent ' + str(agent) + ' found a slot.'
                        #print(s)
                        
                for k in range(int(0.6*m)):
                    if slots[k] == 0 and matched == 0:
                        matchings[agent] = k
                        slots[k] = 1
                        profit2[i] = profit2[i] + price - 5 # offer cheaper price to agent for other parking
                        matched = 1
                        s = 'Agent ' + str(agent) + ' found a slot.'
                        #print(s)
                
                for k in range(int(0.8*m), m):
                    if slots[k] == 0 and matched == 0:
                        matchings[agent] = k
                        slots[k] = 1
                        profit2[i] = profit2[i] + price - 5 # offer cheaper price to agent for other parking
                        matched = 1
                        s = 'Agent ' + str(agent) + ' found a slot.'
                        #print(s)       
                
                
                
                if matched == 0:
                    s = 'Agent ' + str(agent) + ' did not find a slot.'
                    #print(s)
                    profit2[i] = profit2[i] + 5
                    
            if goal == 4:
                for k in range(int(0.8*m), m):
                    if slots[k] == 0 and matched == 0:
                        matchings[agent] = k
                        slots[k] = 1
                        profit2[i] = profit2[i] + price
                        matched = 1
                        s = 'Agent ' + str(agent) + ' found a slot.'
                        #print(s)
                        
                for k in range(int(0.8*m)):
                    if slots[k] == 0 and matched == 0:
                        matchings[agent] = k
                        slots[k] = 1
                        profit2[i] = profit2[i] + price - 5 # offer cheaper price to agent for other parking
                        matched = 1
                        s = 'Agent ' + str(agent) + ' found a slot.'
                        #print(s)
                
                if matched == 0:
                    s = 'Agent ' + str(agent) + ' did not find a slot.'
                    #print(s)
                    profit2[i] = profit2[i] + 5
                    
        slots_filled2[i] = sum(slots)
    
    lin_profit = lin_profit + [np.mean(profit2)]
    
    days = 10
    price = 20
    exp_price = 40
    wtp = 0.2 # prob that an agent will purchase reserved parking
    
    profit = np.zeros(days)
    slots_filled = np.zeros(days)
    
    for i in range(days):
        
        matchings = np.zeros(N)
        pi = np.random.permutation(N)
        slots = np.zeros(m)
        
        for agent in pi:
            
            shows_up = np.random.binomial(1, prob)
            if shows_up == 0:
                continue
            
            #print('Agent ', agent, ' arrived')
            goal = goals[agent]
            matched = 0
            s = 'Agent ' + str(agent) + ' arrived.'
            #print(s)
            
            if goal == 0 or goal == 1:
                for k in range(int(0.6*m-res_prob*0.6*m)):
                    if slots[k] == 0 and matched == 0:
                        matchings[agent] = k
                        slots[k] = 1
                        profit[i] = profit[i] + price
                        matched = 1
                        s = 'Agent ' + str(agent) + ' found a slot.'
                        #print(s)
                        
                willing_to_pay = np.random.binomial(1, wtp)
                if matched == 0 and willing_to_pay == 1:
                    for k in range(int(0.6*m-res_prob*0.6*m)+1, int(0.6*m)):
                        if slots[k] == 0 and matched == 0:
                            matchings[agent] = k
                            slots[k] = 1
                            profit[i] = profit[i] + exp_price
                            matched = 1
                            s = 'Agent ' + str(agent) + ' found a slot.'
                            #print(s)
                            
                        
                if matched == 0:
                    s = 'Agent ' + str(agent) + ' did not find a slot.'
                    #print(s)
                    profit[i] = profit[i] + 5
            
        
            if goal == 2 or goal == 3:
                for k in range(int(0.6*m), int(0.8*m)-int(0.8*m-res_prob*0.8*m)):
                    if slots[k] == 0 and matched == 0:
                        matchings[agent] = k
                        slots[k] = 1
                        profit[i] = profit[i] + price
                        matched = 1
                        s = 'Agent ' + str(agent) + ' found a slot.'
                        #print(s)
                
                willing_to_pay = np.random.binomial(1, wtp)
                if matched == 0 and willing_to_pay == 1:
                    for k in range(int(0.8*m-res_prob*0.8*m)+1, int(0.8*m)):
                        if slots[k] == 0 and matched == 0:
                            matchings[agent] = k
                            slots[k] = 1
                            profit[i] = profit[i] + exp_price
                            matched = 1
                            s = 'Agent ' + str(agent) + ' found a slot.'
                            #print(s)
                    
                    
                if matched == 0:
                    s = 'Agent ' + str(agent) + ' did not find a slot.'
                    #print(s)
                    profit[i] = profit[i] + 5
                    
            if goal == 4:
                for k in range(int(0.8*m), m - int(res_prob*0.8*m)):
                    if slots[k] == 0 and matched == 0:
                        matchings[agent] = k
                        slots[k] = 1
                        profit[i] = profit[i] + price
                        matched = 1
                        s = 'Agent ' + str(agent) + ' found a slot.'
                        #print(s)
                willing_to_pay = np.random.binomial(1, wtp)
                if matched == 0 and willing_to_pay == 1:
                    for k in range(m - int(res_prob*0.8*m)+1, m):
                        if slots[k] == 0 and matched == 0:
                            matchings[agent] = k
                            slots[k] = 1
                            profit[i] = profit[i] + exp_price
                            matched = 1
                            s = 'Agent ' + str(agent) + ' found a slot.'
                            #print(s)
                                    
                            
                            
                if matched == 0:
                    s = 'Agent ' + str(agent) + ' did not find a slot.'
                    #print(s)
                    profit[i] = profit[i] + 5
                    
        slots_filled[i] = sum(slots)
            
    maxdist_profit_res = maxdist_profit_res + [np.mean(profit)]    
        
        
    # begin simulation 2 - variable prices
    days = 10
    price = 20
    soc_welfare2 = np.zeros(days)
    profit2 = np.zeros(days)
    slots_filled2 = np.zeros(days)
    
    # the agent is less likely to pay for reserved slot since she can try to park in another parking lot
    wtp2 = wtp 
    
        
    for i in range(days):
        
        matchings2 = np.zeros(N)
        pi = np.random.permutation(N)
        slots = np.zeros(m)
        
        for agent in pi:
            
            shows_up = np.random.binomial(1, prob)
            if shows_up == 0:
                continue
            
            #print('Agent ', agent, ' arrived')
            goal = goals[agent]
            matched = 0
            s = 'Agent ' + str(agent) + ' arrived.'
            #print(s)
            
            if goal == 0 or goal == 1:
                for k in range(int(0.6*m-res_prob*0.6*m)):
                    if slots[k] == 0 and matched == 0:
                        matchings[agent] = k
                        slots[k] = 1
                        profit[i] = profit[i] + price
                        matched = 1
                        s = 'Agent ' + str(agent) + ' found a slot.'
                        #print(s)
                        
                willing_to_pay = np.random.binomial(1, wtp2)
                if matched == 0 and willing_to_pay == 1:
                    for k in range(int(0.6*m-res_prob*0.6*m)+1, int(0.6*m)):
                        if slots[k] == 0 and matched == 0:
                            matchings[agent] = k
                            slots[k] = 1
                            profit[i] = profit[i] + exp_price
                            matched = 1
                            s = 'Agent ' + str(agent) + ' found a slot.'
                            #print(s)
                        
                
                for k in range(int(0.6*m), int(0.8*m)-int(0.8*m-res_prob*0.8*m)):
                    if slots[k] == 0 and matched == 0:
                        matchings[agent] = k
                        slots[k] = 1
                        profit2[i] = profit2[i] + price - 5 # offer cheaper price to agent for other parking
                        matched = 1
                        s = 'Agent ' + str(agent) + ' found a slot.'
                        #print(s)
                
                for k in range(int(0.8*m), m - int(res_prob*0.8*m)):
                    if slots[k] == 0 and matched == 0:
                        matchings[agent] = k
                        slots[k] = 1
                        profit2[i] = profit2[i] + price - 5 # offer cheaper price to agent for other parking
                        matched = 1
                        s = 'Agent ' + str(agent) + ' found a slot.'
                        #print(s)
                
                        
                if matched == 0:
                    s = 'Agent ' + str(agent) + ' did not find a slot.'
                    #print(s)
                    profit2[i] = profit2[i] + 5
                
            if goal == 2 or goal == 3:
                for k in range(int(0.6*m), int(0.8*m)-int(0.8*m-res_prob*0.8*m)):
                    if slots[k] == 0 and matched == 0:
                        matchings[agent] = k
                        slots[k] = 1
                        profit[i] = profit[i] + price
                        matched = 1
                        s = 'Agent ' + str(agent) + ' found a slot.'
                        #print(s)
                
                willing_to_pay = np.random.binomial(1, wtp)
                if matched == 0 and willing_to_pay == 1:
                    for k in range(int(0.8*m-res_prob*0.8*m)+1, int(0.8*m)):
                        if slots[k] == 0 and matched == 0:
                            matchings[agent] = k
                            slots[k] = 1
                            profit[i] = profit[i] + exp_price
                            matched = 1
                            s = 'Agent ' + str(agent) + ' found a slot.'
                            #print(s)
                        
                for k in range(int(0.6*m-res_prob*0.6*m)):
                    if slots[k] == 0 and matched == 0:
                        matchings[agent] = k
                        slots[k] = 1
                        profit2[i] = profit2[i] + price - 5 # offer cheaper price to agent for other parking
                        matched = 1
                        s = 'Agent ' + str(agent) + ' found a slot.'
                        #print(s)
                
                for k in range(int(0.8*m), m - int(res_prob*0.8*m)):
                    if slots[k] == 0 and matched == 0:
                        matchings[agent] = k
                        slots[k] = 1
                        profit2[i] = profit2[i] + price - 5 # offer cheaper price to agent for other parking
                        matched = 1
                        s = 'Agent ' + str(agent) + ' found a slot.'
                        #print(s)       
                
                
                
                if matched == 0:
                    s = 'Agent ' + str(agent) + ' did not find a slot.'
                    #print(s)
                    profit2[i] = profit2[i] + 5
                    
            if goal == 4:
                for k in range(int(0.8*m), m - int(res_prob*0.8*m)):
                    if slots[k] == 0 and matched == 0:
                        matchings[agent] = k
                        slots[k] = 1
                        profit[i] = profit[i] + price
                        matched = 1
                        s = 'Agent ' + str(agent) + ' found a slot.'
                        #print(s)
                willing_to_pay = np.random.binomial(1, wtp)
                if matched == 0 and willing_to_pay == 1:
                    for k in range(m - int(res_prob*0.8*m)+1, m):
                        if slots[k] == 0 and matched == 0:
                            matchings[agent] = k
                            slots[k] = 1
                            profit[i] = profit[i] + exp_price
                            matched = 1
                            s = 'Agent ' + str(agent) + ' found a slot.'
                            #print(s)
                        
                for k in range(int(0.6*m-res_prob*0.6*m)):
                    if slots[k] == 0 and matched == 0:
                        matchings[agent] = k
                        slots[k] = 1
                        profit2[i] = profit2[i] + price - 5 # offer cheaper price to agent for other parking
                        matched = 1
                        s = 'Agent ' + str(agent) + ' found a slot.'
                        #print(s)
                    
                for k in range(int(0.6*m), int(0.8*m)-int(0.8*m-res_prob*0.8*m)):
                    if slots[k] == 0 and matched == 0:
                        matchings[agent] = k
                        slots[k] = 1
                        profit2[i] = profit2[i] + price - 5 # offer cheaper price to agent for other parking
                        matched = 1
                        s = 'Agent ' + str(agent) + ' found a slot.'
                        #print(s)
                
                
                if matched == 0:
                    s = 'Agent ' + str(agent) + ' did not find a slot.'
                    #print(s)
                    profit2[i] = profit2[i] + 5
                    
        slots_filled2[i] = sum(slots)
    
    lin_profit_res = lin_profit_res + [np.mean(profit2)]
        
        
        
x = [0.1, 0.15, 0.2, 0.25, 0.3]
 
  
# plotting the points  
plt.plot(x, lin_profit, label='Linear Cost')
#plt.plot(x, maxdist_profit, label='Max Distance')
plt.plot(x, lin_profit_res, label='Linear Cost w/ Reserved Slots')
#plt.plot(x, maxdist_profit_res, label='Max Distance w/ Reserved Slots')

plt.xlabel('fraction of slots reserved')  
plt.ylabel('profit')  
plt.legend() 
plt.savefig('plt8.pdf')  
plt.show()       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        