import random
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

#TODO: Quarantine, lockdowns, masks, percentage of who follows a lock down?

#hold our persons in a nested dict
person_info = []
persons = dict(person_info)
infection_stat = {}
healthy_stat = {}
recovery_stat = {}


G = nx.Graph()

#set up the simulator for use
def initialize():
    global lockdown
    lockdown = False

    global num_people
    num_people = 50
    
    #so we can use in other functions
    global people_infected
    people_infected = 10
    
    global people_vaccinated
    people_vaccinated = 0
    
    global healthy_people
    healthy_people = num_people - people_infected
    
    global people_recovered
    people_recovered = 0
    
    healthy_stat[0] = healthy_people
        
    #populate the persons list 
    for i in range(0, num_people):
        persons[i] = {}
        persons[i]['id'] = i
        persons[i]['infected'] = False
        persons[i]['immune'] = False
        persons[i]['contacts'] = []
        persons[i]['infection_prob'] = 0
        persons[i]['when_infected'] = 0
        persons[i]['days_infected'] = 0
        persons[i]['how_many_infected'] = 0
        persons[i]['vaccinated'] = False
        persons[i]['recovered'] = False #If they recovered before the vaccine.
        persons[i]['masked'] = False
        persons[i]['attending_event'] = random.uniform(0, 1)

    #how many family/friends, chance of events to take place
    connect_people(random.randint(0, 5), False)

    infect_person(people_infected)
    #run_graph()
    run()
    
def run():
    #our T rounds
    how_many_days = 2000
    days_elapsed = 0
    chance_to_contact = 0.68 #higher the number the more contacts
    chance_to_infect = 0.50 #higher the number less chance to get infected
    how_long_infected = 5
    #how_long_immune = 20
    lockdown_when = 5
    wear_masks = 0.5 #higher the number the more people that will wear masks 
    
    vaccine_intro = 3 #random.randint(days_elapsed, how_many_days)
    vaccine_chance = 0.4 # chance that a person can be vaccinated
    take_vaccine = 0.6 #higher it is the less people will take it
    
    attend_event = 0.4 #attend an event for the total community
    

    #Check if the days(rounds) comply too
    while(days_elapsed <= how_many_days-1):

        chance_for_event = random.randint(0,1)#chance that an event will take place over the course of our sim. Accounts for randomness
        
        #implement lockdown
        #if(days_elapsed == lockdown_when):
            #globals()['lockdown'] = True

        #If people are all infected, stop the sim
        if(people_infected <= 0):
           break

        if(lockdown == False and attend_event > chance_for_event):
            connect_people(random.randint(1, 4), True)
        
        for i in range(0, len(persons)):
            if days_elapsed >= vaccine_intro: 
              select = random.randint(0,len(persons)-1)
              if(persons[select]['infected'] == False and persons[select]['vaccinated'] == False):
                    chance_for_vax = random.uniform(0,1) #chance that someone will get the vaccine for the invidiual person
                    wants_vaccine = random.uniform(0, 1) #chance that our person 'wants' the vaccine
                    if(chance_for_vax >= vaccine_chance and wants_vaccine > take_vaccine):
                        persons[select]['vaccinated'] = True
                        globals()['people_vaccinated'] += 1

            #Check our infected people
            #If our person has been infected for more than a certain time, make them immune
            if(persons[i]['infected'] and (persons[i]['vaccinated'] == False)):
                if(persons[i]['days_infected'] < how_long_infected):
                    persons[i]['days_infected'] += 1
                else:
                    persons[i]['infected'] = False
                    persons[i]['recovered'] = True
                    globals()['people_infected'] -= 1   
                    globals()['people_recovered'] += 1

            #masks
            if(random.uniform(0,1) < wear_masks):
               persons[i]['masked'] = True
               persons[i]['infection_prob'] /= 2
            
            if(persons[i]['infected'] and len(persons[i]['contacts']) > 0 and persons[i]['infection_prob'] > chance_to_infect):

                could_meet_today = np.floor((int(len(persons[i]['contacts']) * chance_to_contact))) #round down not up
                
                if(could_meet_today > 0 ):
                    met_today = int(could_meet_today)
                else:
                    met_today = 0
                
                if(lockdown):
                    met_today = 0
                
                #loop how many times through their node connections G(n, p)
                for m in range(met_today):
                    select_friend = persons[i]['contacts'][m]
                    person_to_infect = persons[select_friend]
                    
                    #Don't want to double infect others and want to check if that person is immune
                    if(person_to_infect['infected'] or person_to_infect['recovered'] or person_to_infect['vaccinated']):
                        pass
                    else:
                        person_to_infect['infected'] = True
                        person_to_infect['infection_prob'] = round(random.uniform(0,1), 2)
                        person_to_infect['when_infected'] = days_elapsed
                        persons[i]['how_many_infected'] += 1
                        globals()['people_infected'] += 1  
                        globals()['healthy_people'] -= 1 
                    
        days_elapsed += 1
        print(f"Day: {days_elapsed}, Number of people now infected: {people_infected}")
        infection_stat[days_elapsed] = people_infected #save our data for statisitcs, very simple right now
        healthy_stat[days_elapsed] = healthy_people
        recovery_stat[days_elapsed] = people_recovered
    
    print(f"Infected {people_infected}") 
    print(f"Total vaccinated {people_vaccinated}")
    print(f"Total recovered {people_recovered}")

    print(calculate_R())
    
     
    run_graph() #Anything higher than 1000 of N, will crash the program (BE AWARE)
    run_stats()

def calculate_R():
    R = 0
    total_infected = 0
    for r in range(0, len(persons)):
        if(persons[r]['how_many_infected'] > 0 ):
            R += persons[r]['how_many_infected']
            total_infected += 1
    if(total_infected > 0):
        R /= total_infected
    return R

#call this function to print out the list
def debug_persons():
    for i in range(0, len(persons)):
        print(str(persons[i]) + "\n")
    
#randomly select our infected
#argument takes an integer which will be from 0-amount to infect 
def infect_person(infect):
    for i in range(0, infect):
        who = random.randint(0, num_people-1)
        persons[who]['infected'] = True
        persons[who]['infection_prob'] = round(random.uniform(0,1), 2)
        persons[who]['when_infected'] = 0
        infection_stat[0] = infect #make sure we count our initial infected
        print("Infected Person: " + str(persons[who])) 

#TODO make it update and run while the program is a active
def run_graph():
    nodes = []
    edges = []

    #loop to add nodes to the graph
    for i in range(0 , len(persons)):
        nodes.append(persons[i]['id'])
        for edge in persons[i]['contacts']:
            edges.append(tuple((persons[i]['id'], edge)))
            
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    nx.draw(G, with_labels = True)
    plt.show()
    
def run_stats():
    #simple stats, we should flesh out later, to assist with our report
    x, y = zip(*infection_stat.items()) #I(t)
    b, z = zip(*healthy_stat.items()) #S(t)
    a, g = zip(*recovery_stat.items()) #R(t)
    plt.plot(x, y, color='r', label="Infected")
    plt.plot(b, z, color='b', label="Healthy")
    plt.plot(a, g, color='g', label="Recovered")
    plt.title("Rate of Infection: Days per infection")
    plt.ylabel("Infected")
    plt.xlabel("Days")
    plt.legend()
    plt.show()

def connect_people(friends_family, occur):
   
    should_attend = 0.5

    #Create our G(n,p) connections
    for j in range(0, num_people):

        #if we are attending an event with a chance of greater than 
        if(occur == True and persons[j]['attending_event'] > should_attend):
            #simulate more connections with others, allowing for more social actitives 
            #Set event_occurence to 0, to not allow social activities to occur
            friends_family * 2 
        #select our random people
        #range between 0 and x iterate over how many times who we know
        for k in range(0, friends_family):
            who = random.randint(0, num_people-1)
            #make sure we are not duplicating nodes
            if who in persons[j]['contacts'] or who == persons[j]['id'] :
                pass
            else:
                persons[j]['contacts'].append(persons[who]['id'])
                persons[who]['contacts'].append(persons[j]['id'])
