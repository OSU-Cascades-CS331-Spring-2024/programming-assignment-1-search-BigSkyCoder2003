import astar
import bfs
import dfs
import ucs
import sys  

def determine_search_method(search_method):
  if search_method == "astar":
    astar_obj = astar.AStar()
    astar_obj.testAStar()
  elif search_method == "bfs":
    bfs_obj = bfs.BFS()
    bfs_obj.testBFS()
  elif search_method == "dfs":
    dfs_obj = dfs.DFS()
    dfs_obj.testDFS()
  elif search_method == "ucs":
    ucs_obj = ucs.UCS()
    ucs_obj.testUCS()
  else:
    print("Invalid search method: executing default search method (bfs)")
    bfs_obj = bfs.BFS()
    bfs_obj.testBFS()
    return
  print("search_method", search_method)

search_method = sys.argv[1]
determine_search_method(search_method)













# "nice" "43 43 12 N 7 15 59 E" "-->" "va-marseille" "197"
