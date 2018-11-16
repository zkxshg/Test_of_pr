import numpy as np
import matplotlib.pyplot as plt
import time
from OS import gener_str as gener
from OS import algo
#gener the reference strings
rand_str,rand_modi = gener.generate_rand()
local_str,local_modi = gener.generate_local()
own_str,own_modi = gener.generate_own()
#set the memory
num_of_frame = 20

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
# test the FIFO

print("FIFO+Random")
algo.FIFO(num_of_frame, rand_str, rand_modi)
print("FIFO+Local")
algo.FIFO(num_of_frame, local_str, local_modi)
print("FIFO+own")
algo.FIFO(num_of_frame, own_str, own_modi)

# test the Optimal
print("Optimal+Random")
algo.Optimal(num_of_frame, rand_str, rand_modi)
print("Optimal+Local")
algo.Optimal(num_of_frame, local_str, local_modi)
print("Optimal+own")
algo.Optimal(num_of_frame, own_str, own_modi)


# test the ESC
print("ESC+Random")
algo.ESC(num_of_frame, rand_str, rand_modi)
print("ESC+Local")
algo.ESC(num_of_frame, local_str, local_modi)
print("ESC+own")
algo.ESC(num_of_frame, own_str, own_modi)

# test the DIY
print("DIY+Random")
algo.DIY(num_of_frame, rand_str, rand_modi)
print("DIY+Local")
algo.DIY(num_of_frame, local_str, local_modi)
print("DIY+own")
algo.DIY(num_of_frame, own_str, own_modi)

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

