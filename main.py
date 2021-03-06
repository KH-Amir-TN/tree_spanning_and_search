import time

# Constants and global scope variables declaration
FILES_ACCES_MODE = 'r'
SEP = ','
LOG_OUT = "./logs/"
LOG_FILENAME = str( time.time() ) + ".log"
LOG_AND_PRINT = True
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

LOG_FILE = open(LOG_OUT + LOG_FILENAME , "w")

def log(msg,newline=True,explicit_log_and_print=False):
    if LOG_FILE:
        prefix = "\n" if newline else ""
        LOG_FILE.write(str( msg )+ prefix)
    if LOG_AND_PRINT or explicit_log_and_print :
        print(msg)


def dfs(root,lvl=0):
    log("lvl:" + str(lvl) + ",node:",newline=False)
    log(root[0])
    if len(root) > 1:
        nodes = root[1]
        for node in nodes:
            dfs(node, lvl + 1)


def bfs(roots,lvl=-1):
        while len(roots) > 0:
            lvl += 1
            queue = []
            for root in roots:
                log("lvl:" + str(lvl) + ",node:",newline=False)
                log(root[0])
                if len(root) > 1:
                    for node in root[1]:
                            queue.append(node) 
            roots = queue

def start():
    log("###BFS#####")
    bfs([ROOT])
    log("###DFS#####")
    dfs(ROOT)
    
    

# Main program
start()
LOG_FILE.close()
