import time

LOG_OUT = "./logs/"
LOG_FILENAME = str( time.time() ) + ".log"
LOG_AND_PRINT = False 

LOG_FILE = open(LOG_OUT + LOG_FILENAME , "w")

def log(msg,explicit_log_and_print=False):
    if LOG_FILE:
        LOG_FILE.writelines(str( msg ) + "\n")
    if LOG_AND_PRINT or explicit_log_and_print :
        print(msg)


log("Test")

LOG_FILE.close()