This is a solution file for the programming assignment 1: search 

most optimal path for each search method: 
AStar was optimal: 9 times.
UCS was optimal: 9 times.
BFS was optimal: 0 times.
DLS was optimal: 0 times.
AStar average frontier: 4.222222222222222
AStar average explored: 14.0
AStar average expanded: 20.11111111111111
UCS average frontier: 4.444444444444445
UCS average explored: 14.0
UCS average expanded: 19.666666666666668
BFS average frontier: 12.11111111111111
BFS average explored: 9.333333333333334
BFS average expanded: 9.555555555555555
DLS average frontier: 12.11111111111111
DLS average explored: 14.777777777777779
DLS average expanded: 15.777777777777779
Preface of Summary
After "Completing" this assignment, I feel it is necessary to address the quality of work, or rather lack thereof,
that is present in this code. While I do believe that I have the ability to code in a properly abstract and
object-oriented manner, I do not feel that I represented that well in this project. While the code does run and
provide output, I have no direct way to verify the integrity of the provided statistics, and many of them do not
logically check out. After reflecting on this project, I would like to state clearly that this will not be the
status quo for my projects moving forward, as it is not representative of my abilities as a software engineer or
student, and it is disrespectful to you as my professor.

On to the statistics. While the data is not completely reliable on its own, based on the data, through doing research 
for this project, and past academic experience, it is apparent that UCS and Astar are much more efficient at searching 
maps when compared to BFS or DLS. Cost-wise, UCS and Astar were never less optimal than either BFS or DLS. Space-wise, 
Astar seemed to require less expansion/exploration of nodes when compared to UCS, while UCS seemed to be slightly more 
optimal (not reflected in this data set due to errors in Astar behavior and data gathering techniques). These conclusions 
make sense, as UCS tries to look across the map and backtrace to find the best/most optimal route. In comparison, Astar uses 
a heuristic that incorporates the distance to the goal, which discourages moving away from the goal chasing small short sections, 
helping to keep the optimization level high and the number of expanded/visited nodes low.
               
Collaboration Disclosure:
               Throughout this project, I collaborated with several people, including Nate Sweet, Tristan Hook, Patrick Punch, and Kevin Walsh. 
               Additionally, I used Github Copilot to help write some repetitive code, but I did not use it to generate any of the core logic 
               or fundamental concepts for this project, including the search algorithms or the map data structure.