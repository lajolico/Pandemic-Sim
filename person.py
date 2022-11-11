import random 

#TODO: Quarantine, lockdowns, masks, percentage of who follows a lock down?


class Person():
    def __init__(self):
        self.id = id             #Id of our person
        self.infected = False    #Are we infected
        self.immune = False      #Are we immune?
        self.vaccinated = False  #Is this person vaccinated?
        self.days_infected = 0
        self.contacts = random.randint(1,6) #TODO: Change this into a list so we can make connections between different nodes
        self.infection_prob = 0  #the chance we can infect someone
        self.when_infected = 0   #what day were we infected
        self.how_many_infected = [] #hold a list of everyone this person infected

    
        