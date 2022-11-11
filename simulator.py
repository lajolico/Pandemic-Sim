import random
import matplotlib.pyplot as plt
import numpy as np
import person

#hold our persons in a nested dict
person_info = []
persons = dict(person_info)
stat_data = {}

#set up the simulator for use
def initialize():
    num_people = 40
    #so we can use in other functions
    global people_infected
    people_infected = 3
    
    #populate the persons list 
    for i in range(0, num_people):
        persons[i] = {}
        person.Person().id = i
        persons[i]['id'] = i
        persons[i]['infected'] = person.Person().infected
        persons[i]['immune'] = person.Person().immune
        persons[i]['contacts'] = person.Person().contacts
        persons[i]['infection_prob'] = person.Person().infection_prob
        persons[i]['when_infected'] = person.Person().when_infected
        persons[i]['days_infected'] = person.Person().days_infected
                              
    #randomly select our infected 
    for i in range(0, people_infected):
        select = random.randint(0, num_people-1)
        persons[select]['infected'] = True
        persons[select]['infection_prob'] = round(random.uniform(0,1), 2)
        persons[select]['when_infected'] = 0
        stat_data[0] = people_infected #make sure we count our initial infected
        print("Infected Person: " + str(persons[select]))  
    run()
    
def run():
    #our T rounds
    how_many_days = 200
    days_elapsed = 0
    chance_to_contact = 0.4
    chance_to_infect = 0.1
    how_long_infected = 5

    #Set up to where if the total population is infected stop the sim
    #Also check if the days(rounds) comply too
    while(people_infected < len(persons) and days_elapsed <= how_many_days-1):
        
        i
        
        for i in range(0, len(persons)):
            
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
                        globals()['people_infected'] += 1   
                        #print(str(persons[i]['id']) + " infected " + str(person_to_infect['id']) + " on day " + str(days_elapsed))  
           
            #Check our infected people
            #If our person has been infected for more than a certain time, make them immune
          
                    
        days_elapsed += 1
        print(f"Day: {days_elapsed}, Number of people now infected: {people_infected}")
        stat_data[days_elapsed] = people_infected #save our data for statisitcs, very simple right now
    
    print(f"Total infected {people_infected}") 
     
    #simple stats, we should flesh out later, to assist with our report
    x, y = zip(*stat_data.items())
    plt.bar(x, y, color='r', width=0.4)
    plt.title("Rate of Infection: Days per infection")
    plt.ylabel("Infected")
    plt.xlabel("Days")
    plt.show()
    
    

    
    