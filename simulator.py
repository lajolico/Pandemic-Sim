import random
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

#TODO: Quarantine, lockdowns, masks, percentage of who follows a lock down?

#hold our persons in a nested dict
person_info = []
persons = dict(person_info)
stat_data = {}

G = nx.Graph()

#set up the simulator for use
def initialize():
    global num_people
    num_people = 100
    #so we can use in other functions
    global people_infected
    people_infected = 4
    
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
        persons[i]['days_immune'] = 0

    #Create our G(n,p) connections
    for j in range(0, num_people):
        #select our random people
        #range between 0 and x iterate over how many times who we know
        for k in range(0, random.randint(0, 6)):
            who = random.randint(0, num_people-1)
            #make sure we are duplicating nodes
            if who in persons[j]['contacts'] or who == persons[j]['id']  :
                pass
            else:
                persons[j]['contacts'].append(persons[who]['id'])
                persons[who]['contacts'].append(persons[j]['id'])

    #infect_person(people_infected)      
    run_graph()                  
    #run()
    
def run():
    #our T rounds
    how_many_days = 200
    days_elapsed = 0
    chance_to_contact = 0.5 #higher the number the more contacts
    chance_to_infect = 0.003 #higher the number less chance to get infected
    how_long_infected = 5
    how_long_immune = 20

    #Check if the days(rounds) comply too
    while(days_elapsed <= how_many_days-1):

        if(people_infected <= 0):
            break

        for i in range(0, len(persons)):
            if(persons[i]['immune']):
                if(persons[i]['days_immune'] < how_long_immune):
                    persons[i]['days_immune'] += 1
                else:
                    persons[i]['immune'] = False

            #Check our infected people
            #If our person has been infected for more than a certain time, make them immune
            if(persons[i]['infected']):
                if(persons[i]['days_infected'] < how_long_infected):
                    persons[i]['days_infected'] += 1
                else:
                    persons[i]['infected'] = False
                    persons[i]['immune'] = True
                    globals()['people_infected'] -= 1   
            
            if(persons[i]['infected'] and persons[i]['contacts'] > 0 and persons[i]['infection_prob'] >= chance_to_infect):

                #chance for somone to meet another person
                could_meet_today = round(persons[i]['contacts'] * chance_to_contact)
                     
                if(could_meet_today > 0 ):
                    met_today = random.randint(0,could_meet_today)
                else:
                    met_today = 0

                for m in range(met_today):
                    person_to_infect = persons[random.randint(0, len(persons)-1)]
                    
                    #Don't want to double infect others and want to check if that person is immune
                    if(person_to_infect['infected'] or person_to_infect['immune']):
                        pass
                    else:
                        person_to_infect['infected'] = True
                        person_to_infect['infection_prob'] = round(random.uniform(0,1), 2)
                        person_to_infect['when_infected'] = days_elapsed
                        persons[i]['how_many_infected'] += 1
                        globals()['people_infected'] += 1   
                    
        days_elapsed += 1
        print(f"Day: {days_elapsed}, Number of people now infected: {people_infected}")
        stat_data[days_elapsed] = people_infected #save our data for statisitcs, very simple right now
    
    print(f"Total infected {people_infected}") 

    
    debug_persons()
    print(calculate_R())
     
    #simple stats, we should flesh out later, to assist with our report
    x, y = zip(*stat_data.items())
    plt.bar(x, y, color='r', width=1)
    plt.title("Rate of Infection: Days per infection")
    plt.ylabel("Infected")
    plt.xlabel("Days")
    plt.show()

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

def debug_persons():
    for i in range(0, len(persons)):
        print(str(persons[i]) + "\n")
    

def infect_person(infect):
    #randomly select our infected 
    for i in range(0, infect):
        who = random.randint(0, num_people-1)
        persons[who]['infected'] = True
        persons[who]['infection_prob'] = round(random.uniform(0,1), 2)
        persons[who]['when_infected'] = 0
        stat_data[0] = infect #make sure we count our initial infected
        #print("Infected Person: " + str(persons[who])) 


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