This repository is for the CSC-407 Final Project:
Team Members are: Matt Mitchell, Nick Vino, and Logan Jolicoeur

Final Team Project (Tasks):

1. Assume there are N=1,000 people in the small place. Use a simple array to record the 
status of each person, call it “infected”. For example, infected[1]=TRUE if user 1 is 
infected.
2. Each infected individual may come into contact with 0 ≤𝛼≤1 ratio of all people in each 
round of infection.
3. Each contact between an infected individual and a healthy individual has a chance of 
0 ≤𝛽≤1 that the healthy individual will be infected.
4. Output the number of infected individuals after each round. There are T=2,000 rounds.
5. Use some reasonable 𝛼 and 𝛽, for example, 𝛼=0.005 and 𝛽=0.01, to generate the curve 
of total infection as a function of rounds.
6. Repeat step 5 and simulate the fact that each infected person stays infectious for 𝑡1 = 5 
rounds, after which s/he becomes non-infectious and immune forever. Note that you 
may want to choose a slightly larger values of 𝛼 and 𝛽 for your results to be interesting.
7. Repeat step 6 and simulate the fact that each immune person stays non-infectious and 
immune only for 𝑡2 = 20 rounds, after which s/he may be infected again. Again, 
different values of 𝛼 and 𝛽 may be needed.
8. 𝑅0 is defined as the total number of new infected caused by each infected individual, on 
an average. Compute 𝑅0 for step 6 and 7. 
Once the above is done, explore the following directions in your program. I expect different 
teams to explore different ways to approach each of the following steps. Just make sure that 
your approaches make sense and you can explain them as well as the results. 


a. Introduce a connection of 𝐺(𝑛,𝑝) instead of using the random connections made in each 
infection round. Therefore, each individual has a fixed set of connections (as in our 
social lives). In each infection round, each infectious individual would come into contact 
with a ratio of 0 < 𝛾≤1 of its social connections. Simulate how infection would spread 
with different 𝛾 and 𝛽.

b. Suppose an effective vaccine is introduced at 𝑡3 round and it protects each vaccinated 
individual with a 0 < 𝜃< 1 chance. Simulate and demonstrate how two communities 
would see infection spread with different vaccination rates (rate of population that will 
take the vaccine), e.g., 𝑣1 = 0.5 and  𝑣2 = 0.85. 

c. Extend from part b and draw the total infection as a function of vaccination rate,  𝑣. 
Adjust other parameters so that your graph looks interesting. 

d. Simulate a vaccine wear-off effect: this is a decrease of 𝜃 over time. Show different 
curves as a function of time for different rates of 𝜃 decrease. That is, one decrease rate 
per curve.  

e. Introduce some additional connections, e.g., 30% more links, to simulate a period of 
more active social activities. Compare the infection increase rate with those in part b 
without these additional connections. 

f. Can your team think of anything else to simulate with your simulator? Perhaps a football 
or basketball game that connects more people in a short period of time? Explain and 
demonstrate the results.


Final Presentation: each team will present its results for about 8 minutes with every team 
member going over 1-2 slides each in its presentation. Focus on results and explanations. 
Presentation date is our last lecture time. 

Final Report and Presentation: your final report should include title, team members, Section I, 
Introduction; Section II, execution screenshots, graphs, and explanations for each parts above; 
Section III, Conclusion. Please include all source files, final report, and your presentation file in 
your submission in a zip file. 
