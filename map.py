import pprint
import heapq
import math


class Map:
    def __init__(self):
        self.graph = {}
        self.locations = {}

        self.bfs_frontier = []
        self.bfs_avg_frontier = 0
        self.dls_frontier = []
        self.dls_avg_frontier = 0
        self.ucs_frontier = []
        self.ucs_avg_frontier = 0
        self.astar_frontier = []
        self.astar_avg_frontier = 0

        self.bfs_explored = []
        self.bfs_avg_explored = 0
        self.dls_explored = []
        self.dls_avg_explored = 0
        self.ucs_explored = []
        self.ucs_avg_explored = 0
        self.astar_explored = []
        self.astar_avg_explored = 0

        self.bfs_expanded = []
        self.bfs_avg_expanded = 0
        self.dls_expanded = []
        self.dls_avg_expanded = 0
        self.ucs_expanded = []
        self.ucs_avg_expanded = 0
        self.astar_expanded = []
        self.astar_avg_expanded = 0

    def add_city(self, city, connections):
        local_connections = connections
        if city not in self.graph:
            self.graph[city] = local_connections
        else:
            self.graph[city].extend(local_connections)

    def print_map(self):
        for city, connections in self.graph.items():
            print(city, connections)
        
    def add_location(self, city, lat_deg, lat_min, lat_sec, lat_direction, lon_deg, lon_min, lon_sec, lon_direction):
        self.locations[city] = self.dms_to_dd(int(lat_deg), int(lat_min), int(lat_sec), lat_direction), self.dms_to_dd(int(lon_deg), int(lon_min), int(lon_sec), lon_direction)
        # print(city, self.locations[city])

    def euclidean_distance(self, city1, city2):
        return ((self.locations[city2][0] - self.locations[city1][0])**2 + (self.locations[city2][1] - self.locations[city1][1])**2)**0.5
   
    def dms_to_dd(self, degrees, minutes, seconds, hemisphere):
      dd = degrees + minutes/60 + seconds/3600
      if hemisphere == 'S' or hemisphere == 'W':
        dd *= -1
      return dd

    def BFS(self, start, goal):
        explored = []
        queue = [[start]]
        if start == goal:
            # print("Start and goal are the same")
            return "Start and goal are the same"
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in explored:
                neighbors = self.graph[node]
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
                    if neighbor == goal:
                        # print("Path found: ", new_path)
                        self.bfs_explored = explored
                        if queue:
                          self.bfs_frontier = [path[-1] for path in queue]
                        for i in self.bfs_explored:
                          if i not in self.bfs_frontier:
                            self.bfs_expanded.append(i)
                        return new_path
                explored.append(node)
        print("Path not found")
        return

    def DLS(self, start, goal):
      explored = []

      depth_limit = 0
      
      while True:
          result = self.iterative_dls(start, goal, depth_limit,explored)
          if result:
            # print("Depth limit: ", depth_limit)
            return result
          depth_limit += 1
    
    def iterative_dls(self, start, goal, max_depth,explored):
        stack = [(start,[start])]

        while stack:
            node,path = stack.pop()
            if node not in explored:
              explored.append(node)

            if node == goal:
                self.dls_explored = explored
                if stack:
                  for i in range(len(stack)):
                    self.dls_frontier.append(stack[i][0])
                for i in self.dls_explored:
                  if i not in self.dls_frontier:
                    self.dls_expanded.append(i)
                return path
            
            if len(path) <= max_depth:
                
                for neighbor in self.graph[node]:
                    # if neighbor not in path:
                        stack.append((neighbor, path + [neighbor]))
        
    
    
    
        
        
        
        
        
        
        # explored = []
        # stack = [[start]]
        # if start == goal:
        #     # print("Start and goal are the same")
        #     return "Start and goal are the same"
        # while stack:
        #     path = stack.pop()
        #     node = path[-1]
        #     if node not in explored:
        #         neighbors = self.graph[node]
        #         for neighbor in neighbors:
        #             new_path = list(path)
        #             new_path.append(neighbor)
        #             stack.append(new_path)
        #             if neighbor == goal:
        #                 # print("Path found: ", new_path)
        #                 return str(new_path) + "\n"
        #         explored.append(node)
        # print("Path not found")
        # return
    
    def UCS(self, start, goal):
        explored = []
        queue = [(0, [start])]  
        if start == goal:
            return "Start and goal are the same"
        while queue:
            cost, path = heapq.heappop(queue)  
            node = path[-1]
            if node == goal:
              self.ucs_explored = explored
              if queue:
                self.ucs_frontier = queue[0][1]
              for i in self.ucs_explored:
                if i not in self.ucs_frontier:
                  self.ucs_expanded.append(i)     
              return path,cost
            if node not in explored:
                explored.append(node)
                neighbors = self.graph[node]
                for neighbor, edge_cost in neighbors.items():
                    new_path = list(path)
                    new_path.append(neighbor)
                    new_cost = cost + int(edge_cost)
                    heapq.heappush(queue, (new_cost, new_path))
        return "Path not found"


    def reset_instance_lists(self):
       #💀💀💀💀💀💀💀💀💀💀💀
        self.bfs_frontier = []
        self.dls_frontier = []
        self.ucs_frontier = []
        self.astar_frontier = []

        self.bfs_explored = []
        self.dls_explored = []
        self.ucs_explored = []
        self.astar_explored = []

        self.bfs_expanded = []
        self.dls_expanded = []
        self.ucs_expanded = []
        self.astar_expanded = []


#Frontier =[c,d,e]
        #Explored = [a,b,c,d,e]
        #Expanded = [ab] (ES-FR)
    def AStar(self, start, goal):
        explored = []
        queue = [(0,0,  [start])]  
        if start == goal:
            # print("Start and goal are the same")
            return "Start and goal are the same"
        while queue:
            heuristic_cost, path_cost, path = heapq.heappop(queue) 
            node = path[-1]
            if node not in explored:
                if node == goal:
                  self.astar_explored = explored
                  if queue:
                    self.astar_frontier = queue[0][2]
                  for i in self.astar_explored:
                    if i not in self.astar_frontier:
                      self.astar_expanded.append(i)
                  return path, path_cost
                explored.append(node)
                neighbors = self.graph[node]
                for neighbor, edge_cost in neighbors.items():
                    new_path = list(path)
                    new_path.append(neighbor)
                    # heuristic_cost = path_cost + int(edge_cost)
                    new_cost = path_cost + int(edge_cost)
                    heuristic_cost = self.euclidean_distance(neighbor, goal)
                    total_cost = new_cost + heuristic_cost
                    heapq.heappush(queue, (total_cost, new_cost, new_path))
        return "Path not found" 
    
    
    
    def get_path_cost(self, path):
        cost = 0
        for i in range(len(path)-1):
          cost += int(self.graph[path[i]][path[i+1]])
        return cost