import time,resource,sys

resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)
# Constants and global scope variables declaration
FILES_ACCES_MODE = 'r'
DEPTH_LIM = 2
LOG_OUT = "./logs/"
LOG_FILENAME = str( time.time() ) + ".log"
LOG_AND_PRINT = True
LINES = 3
COLS = 3
QUEUE = set()
ROOT = [{"order":1,"value":1}, [
            [{"order":2,"value":2},[
                [{"order":5,"value":5},[
                    [{"order":8,"value":8}]
                ]]
            ]],
            [{"order":3,"value":3},[
                [{"order":6,"value":6},[
                    [{"order":9,"value":9}]
                ]]
            ]],
            [{"order":4,"value":4},[
                [{"order":7,"value":7},[
                    [{"order":10,"value":10}]
                ]]
            ]]
]]
INIT_STATE = [
    [7,2,4],
    [5,0,6],
    [8,3,1]
]

END_STATE = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
]

LOG_FILE = open(LOG_OUT + LOG_FILENAME , "w")

def log(msg,newline=True,explicit_log_and_print=False):
    if LOG_FILE:
        prefix = "\n" if newline else ""
        LOG_FILE.write(str( msg )+ prefix)
    if LOG_AND_PRINT or explicit_log_and_print :
        print(msg)



def limited_dfs(root, depth_limit, lvl=0):
    print("lvl:" + str(lvl) + ",node:")
    print(root[0])
    if len(root) > 1 and lvl < depth_limit:
        nodes = root[1]
        for node in nodes:
            limited_dfs(node, depth_limit, lvl + 1)


def iterative_limited_dfs(root, max_depth):
    for depth in range(1, max_depth + 1):
        print("DFS with depth limited to "+str(depth)+":")
        limited_dfs(root,depth)        

def bfs(roots,lvl=-1):
        while len(roots) > 0:
            lvl += 1
            queue = []
            for root in roots:
                print("lvl:" + str(lvl) + ",node:")
                print(root[0])
                if len(root) > 1:
                    for node in root[1]:
                            queue.append(node) 
            roots = queue

def is_acceptable(state):
    line,col = state
    return line >= 0 and line < LINES and col >= 0 and col < COLS

def generate_node(node,old_state,new_state):
    node,old_state,new_state = list(vect[:] for vect in node ), old_state[:] , new_state[:]
    old_line, old_col = old_state
    new_line, new_col = new_state
    #print("ol,oc:",old_line,old_col)
    #print(node)
    node[old_line][old_col], node[new_line][new_col] = node[new_line][new_col], node[old_line][old_col]
    #print("nl,nc:",new_line,new_col)
    #print(node)
    return node

def generate_nodes(root, line, col):
    possible_states = [
        [line + 1,col],
        [line - 1,col ],
        [line, col + 1],
        [line, col - 1]
        ]
    res = []
    for possible_state in possible_states:
       if is_acceptable(possible_state):
          node = generate_node(root,[line,col],possible_state)
          if not str(node) in QUEUE:
             res.append([node,possible_state])
    return res

def dfs(root,end_state,line=0,col=0,lvl=0):
    print("lvl:" + str(lvl) + ",node:")
    print(root)
    QUEUE.add(str(root))
    if root == end_state:
        print("END STATE REACHED!!!")
        exit(0)
    results = generate_nodes(root, line, col)
    if len(results) > 0:
        for result in results:
            node = result[0]
            line,col = result[1]
            dfs(node,end_state, line, col , lvl + 1)


def start():
    dfs(INIT_STATE,END_STATE,1,1)

# Main program
start()
LOG_FILE.close()
