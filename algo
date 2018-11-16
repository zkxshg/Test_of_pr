import numpy as np
# FIFO algorithm
def FIFO(num_of_frame,rand_str,rand_modi):
    # initialize
    page_fault = 0
    disk_write = 0
    count =0
    fin = 0
    memory = np.zeros(num_of_frame, dtype=np.int)
    # main algorithm
    for i in rand_str:
        equal = 0
        # page exist
        for j in memory:
            if j == i:
                equal = 1
                break
        # page fault occur
        if equal == 0:
            memory[fin] = i
            fin += 1
            page_fault += 1
            if rand_modi[count] == 1:
                disk_write += 1
            if fin >= num_of_frame:
                fin = 0
        count += 1
    print("page fault is:", page_fault)
    print("interrupt is:", page_fault + disk_write)
    print("disk write is:", disk_write)
    return 0

# Optimal algorithm
def Optimal(num_of_frame,rand_str,rand_modi):
    # initialize
    page_fault = 0
    disk_write = 0
    count =0
    memory = np.zeros(num_of_frame, dtype=np.int)
    # main algorithm
    # fill the memory  before page fault occur
    for i in rand_str[0:num_of_frame]:
        memory[count] = i
        page_fault += 1
        count += 1
    # Optimal start
    for i in rand_str[num_of_frame:]:
        equal = 0
        # page exist
        for j in memory:
            if j == i:
                equal = 1
                break
        # page fault occur
        if equal == 0:
            distance = np.zeros(num_of_frame, dtype=np.int)
            memory_c = 0
            # calculate cost of all pages in memory
            for k in memory:
                # exist = 0
                string_c = count + 1
                while(string_c < rand_str.size):
                    # page appear
                    if k == rand_str[string_c]:
                        # exist = 1
                        distance[memory_c] = string_c - count
                        break
                    if (string_c - count) > 100:
                        # exist = 1
                        distance[memory_c] = 101
                        break
                    string_c += 1
                # if exist == 0:
                    # distance[memory_c] = 100001
                memory_c += 1
            # select the max_distance page
            memory_c2 = 0
            max = 0
            max_point = -1
            for l in distance:
                if l > max:
                    max = l
                    max_point = memory_c2
                memory_c2 += 1
            # page I/O
            memory[max_point] = i
            page_fault += 1
            if rand_modi[count] == 1:
                disk_write += 1
        count += 1
    print("page fault is:", page_fault)
    print("interrupt is:", page_fault + disk_write)
    print("disk write is:", disk_write)
    return 0

# Enhanced second chance algorithm
def ESC(num_of_frame,rand_str,rand_modi):
    # initialize
    page_fault = 0
    disk_write = 0
    count = 0
    fin = 0
    memory = np.zeros(num_of_frame, dtype=np.int)
    # 0=(0,0); 1=(0,1); 2=(1,0); 3=(1,1)
    memory_bit = np.zeros(num_of_frame, dtype=np.int)
    # main algorithm
    for i in rand_str:
        equal = 0
        c2 = 0
        # page exist
        for j in memory:
            if j == i:
                equal = 1
                if rand_modi[count] == 1:
                    memory_bit[c2] = 3
                else:
                    memory_bit[c2] = 2
                # print("==================equal===========")
                c2 += 1
                break
        # page fault occur
        if equal == 0:
            exist = 0
            # first search
            # search (0,0)
            for k in range(0, num_of_frame):
                point = (fin + k) % num_of_frame
                if memory_bit[point] == 0:
                    memory[point] = i
                    memory_bit[point] = 2
                    exist = 1
                    break
                elif memory_bit[point] == 2:
                    memory_bit[point] = 0
            # search (0,1)
            if exist == 0:
                for k in range(0, num_of_frame):
                    point = (fin + k) % num_of_frame
                    if memory_bit[point] == 1:
                        memory[point] = i
                        memory_bit[point] = 3
                        exist = 1
                        break
                    elif memory_bit[point] == 3:
                        memory_bit[point] = 1
            # second search
            # search (0,0)
            if exist == 0:
                for k in range(0, num_of_frame):
                    point = (fin + k) % num_of_frame
                    if memory_bit[point] == 0:
                        memory[point] = i
                        memory_bit[point] = 2
                        exist = 1
                        break
            # search (0,1)
            if exist == 0:
                for k in range(0, num_of_frame):
                    point = (fin + k) % num_of_frame
                    if memory_bit[point] == 1:
                        memory[point] = i
                        memory_bit[point] = 3
                        break
            fin += 1
            page_fault += 1
            if rand_modi[count] == 1:
                disk_write += 1
            if fin >= num_of_frame:
                fin = 0
        count += 1
    print("page fault is:", page_fault)
    print("interrupt is:", page_fault + disk_write)
    print("disk write is:", disk_write)
    return 0

# DIY algorithm
def DIY(num_of_frame,rand_str,rand_modi):
    # initialize
    page_fault = 0
    disk_write = 0
    count =0
    # fin = 0
    memory = np.zeros(num_of_frame, dtype=np.int)
    # main algorithm
    for i in rand_str:
        equal = 0
        # page exist
        for j in memory:
            if j == i:
                equal = 1
                # print("==================equal===========")
                break
        # page fault occur
        if equal == 0:
            max = 0
            max_c = -1
            memory_c = 0
            for k in memory:
                if abs(i - k) > max:
                    max = abs(i - k)
                    max_c = memory_c
                memory_c += 1
            memory[max_c] = i
            page_fault += 1
            if rand_modi[count] == 1:
                disk_write += 1
        count += 1
    print("page fault is:", page_fault)
    print("interrupt is:", page_fault + disk_write)
    print("disk write is:", disk_write)
    return 0
