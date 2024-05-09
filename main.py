import sys  
import map
import argparse
import pprint

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('--map_file','-M', type=str, help='file name for map data', required=True)
parser.add_argument('--search_method','-S', default='BFS', type=str, help='search method to use')
parser.add_argument('--initial_city','-A', type=str, help='initial city')
parser.add_argument('--goal_city','-B', type=str, help='goal city')
args = parser.parse_args()


def determine_search_method():
  search_method= args.search_method.upper()
  if search_method == "BFS":
    path= map.BFS(args.initial_city, args.goal_city)
    print("BFS:", path, "cost: ", str(map.get_path_cost(path)))
    # print("explored", map.bfs_explored)
    # print("frontier", map.bfs_frontier)
    # print("expanded", map.bfs_expanded)
  elif search_method == "DLS":
    path= map.DLS(args.initial_city, args.goal_city)
    print("DLS:", path, "cost: ", str(map.get_path_cost(path)))
    # print("frontier", map.dls_frontier)
    # print("expanded", map.dls_expanded)
    # print("explored", map.dls_explored)
  elif search_method == "UCS":
    path= map.UCS(args.initial_city, args.goal_city)
    print("UCS:", path[0], "cost: ", str(map.get_path_cost(path[0])))
    # print("explored", map.ucs_explored)
    # print("frontier", map.ucs_frontier)
    # print("expanded", map.ucs_expanded)
  elif search_method == "ASTAR":
    path= map.AStar(args.initial_city, args.goal_city)
    print("AStar:", path[0], "cost: ", str(map.get_path_cost(path[0])))
    # print("explored", map.astar_explored)
    # print("frontier", map.astar_frontier)
    # print("expanded", map.astar_expanded)
  else:
    print("Invalid search method: default execution selected with all search methods")
    f = open('solution.txt', 'w')
    default_execution(f)


def determine_initial_and_goal_cities():
  if args.initial_city in map.graph and args.goal_city in map.graph:
    determine_search_method()  
  else:
    print("Initial or goal city missing: default execution selected with all search methods")
    f = open('solution.txt', 'w')
    default_execution(f)
  
  

def all_search_methods(start, goal,):
  output_string = ""
  Astar_path, Astar_cost = map.AStar(start, goal)
  UCS_path, UCS_cost = map.UCS(start, goal)
  BFS_path = map.BFS(start, goal)
  BFS_cost = map.get_path_cost(BFS_path)
  DLS_path = map.DLS(start, goal)
  DLS_cost = map.get_path_cost(DLS_path)
  map.bfs_avg_frontier += len(map.bfs_frontier)
  map.bfs_avg_explored += len(map.bfs_explored)
  map.bfs_avg_expanded += len(map.bfs_expanded)
  map.dls_avg_frontier += len(map.dls_frontier)
  map.dls_avg_explored += len(map.dls_explored)
  map.dls_avg_expanded += len(map.dls_expanded)
  map.ucs_avg_frontier += len(map.ucs_frontier)
  map.ucs_avg_explored += len(map.ucs_explored)
  map.ucs_avg_expanded += len(map.ucs_expanded)
  map.astar_avg_frontier += len(map.astar_frontier)
  map.astar_avg_explored += len(map.astar_explored)
  map.astar_avg_expanded += len(map.astar_expanded)
  output_string = ""
  output_string += "BFS: " + str(BFS_path) + " cost: " + str(BFS_cost) + '\n' + "explored: "+ str(len(map.bfs_explored)) + '\n' + "frontier: "+ str(len(map.bfs_frontier)) + '\n' + "expanded: "+ str(len(map.bfs_expanded)) + '\n'
  output_string += "DLS: " + str(DLS_path) + " cost: " + str(DLS_cost) + '\n' + "explored: "+ str(len(map.dls_explored)) + '\n' + "frontier: "+ str(len(map.dls_frontier)) + '\n' + "expanded: "+ str(len(map.dls_expanded)) + '\n'
  output_string += "UCS: " + str(UCS_path) + " cost: " + str(UCS_cost) + '\n' + "explored: "+ str(len(map.ucs_explored)) + '\n' + "frontier: "+ str(len(map.ucs_frontier)) + '\n' + "expanded: "+ str(len(map.ucs_expanded)) + '\n'
  output_string += "AStar: " + str(Astar_path) + " cost: " + str(Astar_cost) + '\n' + "explored: "+ str(len(map.astar_explored)) + '\n' + "frontier: "+ str(len(map.astar_frontier)) + '\n' + "expanded: "+ str(len(map.astar_expanded)) + '\n'
  
  map.reset_instance_lists() 
  return output_string

def most_optimal(start,goal, Astar_optimal, UCS_optimal, BFS_optimal, DLS_optimal):
  Astar_most_optimal = Astar_optimal
  UCS_most_optimal = UCS_optimal
  BFS_most_optimal = BFS_optimal
  DLS_most_optimal = DLS_optimal

  Astar_path = map.AStar(start, goal)
  Astar_cost = map.get_path_cost(Astar_path[0])
  UCS_path = map.UCS(start, goal)
  UCS_cost = map.get_path_cost(UCS_path[0])
  BFS_path = map.BFS(start, goal)
  BFS_cost = map.get_path_cost(BFS_path)
  DLS_path = map.DLS(start, goal)
  DLS_cost = map.get_path_cost(DLS_path)
  if Astar_cost < UCS_cost and Astar_cost < BFS_cost and Astar_cost < DLS_cost:
    Astar_most_optimal += 1
  elif UCS_cost < Astar_cost and UCS_cost < BFS_cost and UCS_cost < DLS_cost:
    UCS_most_optimal += 1
  elif BFS_cost < Astar_cost and BFS_cost < UCS_cost and BFS_cost < DLS_cost:
    BFS_most_optimal += 1
  elif DLS_cost < Astar_cost and DLS_cost < UCS_cost and DLS_cost < BFS_cost:
    DLS_most_optimal += 1
  elif Astar_cost == UCS_cost:
    Astar_most_optimal += 1
    UCS_most_optimal += 1
  return (Astar_most_optimal, UCS_most_optimal, BFS_most_optimal, DLS_most_optimal)


def statistics_cruncher():
  pass


def default_execution(file):
  Astar_most_optimal = 0
  UCS_most_optimal = 0
  BFS_most_optimal = 0
  DLS_most_optimal = 0
  
  print("Default execution: all search methods")
  file.write(all_search_methods("brest" ,"nice"))
  Astar_most_optimal, UCS_most_optimal, BFS_most_optimal, DLS_most_optimal = most_optimal("brest" ,"nice", Astar_most_optimal, UCS_most_optimal, BFS_most_optimal, DLS_most_optimal)
  file.write(all_search_methods("montpellier" ,"calais"))
  Astar_most_optimal, UCS_most_optimal, BFS_most_optimal, DLS_most_optimal = most_optimal("montpellier" ,"calais", Astar_most_optimal, UCS_most_optimal, BFS_most_optimal, DLS_most_optimal)
  file.write(all_search_methods("strasbourg" ,"bordeaux"))
  Astar_most_optimal, UCS_most_optimal, BFS_most_optimal, DLS_most_optimal = most_optimal("strasbourg" ,"bordeaux", Astar_most_optimal, UCS_most_optimal, BFS_most_optimal, DLS_most_optimal)
  file.write(all_search_methods("paris" ,"grenoble"))
  Astar_most_optimal, UCS_most_optimal, BFS_most_optimal, DLS_most_optimal = most_optimal("paris" ,"grenoble", Astar_most_optimal, UCS_most_optimal, BFS_most_optimal, DLS_most_optimal)
  file.write(all_search_methods("grenoble" ,"paris"))
  Astar_most_optimal, UCS_most_optimal, BFS_most_optimal, DLS_most_optimal = most_optimal("grenoble" ,"paris", Astar_most_optimal, UCS_most_optimal, BFS_most_optimal, DLS_most_optimal)
  file.write(all_search_methods("brest" ,"grenoble"))
  Astar_most_optimal, UCS_most_optimal, BFS_most_optimal, DLS_most_optimal = most_optimal("brest" ,"grenoble", Astar_most_optimal, UCS_most_optimal, BFS_most_optimal, DLS_most_optimal)
  file.write(all_search_methods("grenoble" ,"brest"))
  Astar_most_optimal, UCS_most_optimal, BFS_most_optimal, DLS_most_optimal = most_optimal("grenoble" ,"brest", Astar_most_optimal, UCS_most_optimal, BFS_most_optimal, DLS_most_optimal)
  file.write(all_search_methods("nice" ,"nantes"))
  Astar_most_optimal, UCS_most_optimal, BFS_most_optimal, DLS_most_optimal = most_optimal("nice" ,"nantes", Astar_most_optimal, UCS_most_optimal, BFS_most_optimal, DLS_most_optimal)
  file.write(all_search_methods("caen" ,"strasbourg"))
  Astar_most_optimal, UCS_most_optimal, BFS_most_optimal, DLS_most_optimal = most_optimal("caen" ,"strasbourg", Astar_most_optimal, UCS_most_optimal, BFS_most_optimal, DLS_most_optimal)
  file.close()
  readme_writer(Astar_most_optimal, UCS_most_optimal, BFS_most_optimal, DLS_most_optimal)
  print(Astar_most_optimal, UCS_most_optimal, BFS_most_optimal, DLS_most_optimal)
  exit()

def readme_writer(Astar_most_optimal, UCS_most_optimal, BFS_most_optimal, DLS_most_optimal):
  readme = open("README.md", "w")
  readme.write("This is a solution file for the programming assignment 1: search \n\n")
  readme.write("most optimal path for each search method: \n")
  readme.write("AStar was optimal: " + str(Astar_most_optimal) + ' times.\n')
  readme.write("UCS was optimal: " + str(UCS_most_optimal) + ' times.\n')
  readme.write("BFS was optimal: " + str(BFS_most_optimal) + ' times.\n')
  readme.write("DLS was optimal: " + str(DLS_most_optimal) + ' times.\n')
  readme.write("AStar average frontier: " + str(map.astar_avg_frontier/9) + '\n')
  readme.write("AStar average explored: " + str(map.astar_avg_explored/9) + '\n')
  readme.write("AStar average expanded: " + str(map.astar_avg_expanded/9) + '\n')
  readme.write("UCS average frontier: " + str(map.ucs_avg_frontier/9) + '\n')
  readme.write("UCS average explored: " + str(map.ucs_avg_explored/9) + '\n')
  readme.write("UCS average expanded: " + str(map.ucs_avg_expanded/9) + '\n')
  readme.write("BFS average frontier: " + str(map.bfs_avg_frontier/9) + '\n')
  readme.write("BFS average explored: " + str(map.bfs_avg_explored/9) + '\n')
  readme.write("BFS average expanded: " + str(map.bfs_avg_expanded/9) + '\n')
  readme.write("DLS average frontier: " + str(map.dls_avg_frontier/9) + '\n')
  readme.write("DLS average explored: " + str(map.dls_avg_explored/9) + '\n')
  readme.write("DLS average expanded: " + str(map.dls_avg_expanded/9) + '\n')
  readme.write("""Preface of Summary
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
               or fundamental concepts for this project, including the search algorithms or the map data structure.""")
  readme.write
  readme.close()

def build_map():
  file = open(args.map_file, "r")
  lines = file.readlines()
  connections = {}
  connections_array = []
  # lines = []
  for index, line in enumerate(lines):

    #stores an array of the connection for the current line
    for ind, connection in enumerate(line.split()):
      if connection == "-->":
        connections_array = line.split()[ind+1:]

    for i in range(0, len(connections_array),2):
      connections[connections_array[i].replace("va-", "")] = connections_array[i+1]
    
    map.add_city(line.split()[0], connections)
    map.add_location(line.split()[0], line.split()[1], line.split()[2], line.split()[3], line.split()[4], line.split()[5], line.split()[6], line.split()[7], line.split()[8])
    connections = {}

map = map.Map()
build_map()
determine_initial_and_goal_cities()





#USE argparse to parse arguments
