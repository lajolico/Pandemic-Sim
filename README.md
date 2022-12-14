# final_project_407



This repository is for the CSC-407 Final Project: Team Members are: Matt Mitchell, Nick Vino, and Logan Jolicoeur

Final Team Project (Tasks):
1. Assume there are N=1,000 people in the small place. Use a simple array to record the 
status of each person, call it βinfectedβ. For example, infected[1]=TRUE if user 1 is 
infected.
2. Each infected individual may come into contact with 0 β€πΌβ€1 ratio of all people in each 
round of infection.
3. Each contact between an infected individual and a healthy individual has a chance of 
0 β€π½β€1 that the healthy individual will be infected.
4. Output the number of infected individuals after each round. There are T=2,000 rounds.
5. Use some reasonable πΌ and π½, for example, πΌ=0.005 and π½=0.01, to generate the curve 
of total infection as a function of rounds.
6. Repeat step 5 and simulate the fact that each infected person stays infectious for π‘1 = 5 
rounds, after which s/he becomes non-infectious and immune forever. Note that you 
may want to choose a slightly larger values of πΌ and π½ for your results to be interesting.
7. Repeat step 6 and simulate the fact that each immune person stays non-infectious and 
immune only for π‘2 = 20 rounds, after which s/he may be infected again. Again, 
different values of πΌ and π½ may be needed.
8. π0 is defined as the total number of new infected caused by each infected individual, on 
an average. Compute π0 for step 6 and 7. 

a. Introduce a connection of πΊ(π,π) instead of using the random connections made in each infection round. Therefore, each individual has a fixed set of connections (as in our social lives). In each infection round, each infectious individual would come into contact with a ratio of 0 < πΎβ€1 of its social connections. Simulate how infection would spread with different πΎ and π½.

b. Suppose an effective vaccine is introduced at π‘3 round and it protects each vaccinated individual with a 0 < π< 1 chance. Simulate and demonstrate how two communities would see infection spread with different vaccination rates (rate of population that will take the vaccine), e.g., π£1 = 0.5 and π£2 = 0.85.

c. Extend from part b and draw the total infection as a function of vaccination rate, π£. Adjust other parameters so that your graph looks interesting.

d. Simulate a vaccine wear-off effect: this is a decrease of π over time. Show different curves as a function of time for different rates of π decrease. That is, one decrease rate per curve.

e. Introduce some additional connections, e.g., 30% more links, to simulate a period of more active social activities. Compare the infection increase rate with those in part b without these additional connections.

f. Can your team think of anything else to simulate with your simulator? Perhaps a football or basketball game that connects more people in a short period of time? Explain and demonstrate the results.

Final Presentation: each team will present its results for about 8 minutes with every team member going over 1-2 slides each in its presentation. Focus on results and explanations. Presentation date is our last lecture time.

Final Report and Presentation: your final report should include title, team members, Section I, Introduction; Section II, execution screenshots, graphs, and explanations for each parts above; Section III, Conclusion. Please include all source files, final report, and your presentation file in your submission in a zip file.
