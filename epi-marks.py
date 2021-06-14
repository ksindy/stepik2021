from posixpath import split
import pandas as pd
import numpy as np

# Open files and initialize variables, list, and string.
file = open("2.txt", "r")
out = open("ans-2.txt", "w")
num_lines = ''
col_num = ''
df = None
state_dict = {}

def split_char(word):
    return [char for char in word]

a_file = file.readlines()[1:] #skip first line 
for line in a_file:
    if (' ' in line):
        print('space detected')
        num_lines = int(line.split()[0])
        col_num = int(line.split()[1])
        state_dict ={}
        max_state_list = []
        if df is not None:   
            df.drop(df.index, inplace=True)
    else:
        chars = split_char(line.strip())
        if df is None:
            df = pd.DataFrame([chars])
        else:
            a_series = pd.Series(chars)
            df = df.append(a_series, ignore_index=True)
        if df.shape[0] == num_lines:
            for cols in range(col_num):
                if state_dict:
                    max_state = max(state_dict.values())+1
                else:
                    max_state = 1
                for next_mod in range(col_num):
                    if next_mod+1 not in state_dict.keys():
                        if df[cols].equals(df[next_mod]):
                            state_dict[next_mod+1] = max_state
            max_val = max(state_dict.values())
            for key, value in sorted(state_dict.items()): # Note the () after items!
                max_state_list.append(str(value))
            # out.write(str(max(max_state_list)))
            out.write(str(max_val))
            out.write("\n")
            out.write(" ".join(max_state_list))
            out.write("\n")
            print(max_val)
            print(max_state_list)

            
                    
                
        
    
        
        
    