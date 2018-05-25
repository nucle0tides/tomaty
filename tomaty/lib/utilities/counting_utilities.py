from datetime import timedelta
from pdb import set_trace as bp

def calculate_tomatos(total_time, length):
    # idk if this is the best way to calculate it
    # do you consider a completed tomato to be the part you're focusing
    # or the whole work + focus cycle?
    return int(total_time/length)
