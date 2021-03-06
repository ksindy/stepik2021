import pandas as pd
import numpy as np

# Open files and initialize variables, list, and string.
# file = open("diag-A.txt", "r")
# out = open("diag-A-ans.txt", "w")
file = open("test3_diag.txt", "r")
out = open("ans-A3-diag.txt", "w")
tree_dict = {}
values_dict = {}
n_disease = 0
disease_dict = {}
pat_dict = {}
n_patient = 0
final_dict = {}
ordered_vert_list = []
prev_dis_id = ""
prev_vert_value = 0
for i, line in enumerate(file, 1):
    line = line.strip() 
    int_list = list(line.split(" "))  
    if i == 2:
        vert_key = 1
        step = 0
        prev_vert = 1 
        child_vert = 1
        verts = []
        for index, vert in enumerate(int_list, 2):
            vert = int(vert)
            parent = vert
            child_vert += 1
            if parent == 1:
                tree_dict[child_vert] = [parent, child_vert]
            else:
                verts = list(tree_dict.get(vert))
                verts.append(child_vert)
                tree_dict[child_vert] = verts
                prev_vert = vert
    if i == 3:
        for vertex, value in enumerate(int_list, 1): 
            value = int(value)
            vertex = int(vertex)
            values_dict[vertex] = value
        
    if i == 4:
        n_disease = int(int_list[0])
    if i > 4:
        for disease in range(n_disease):
            disease += 1
            if i == 4 + disease:
                dis_id = int(int_list[0])
                dis_vert = int_list[1:]
                disease_dict[disease] = dis_vert
    if i == 4 + n_disease + 1:
        n_patient = int(int_list[0])
    if i > 4 + n_disease:
        for patient in range(n_patient):
            patient += 1
            if i == 4 + n_disease + 1 + patient:
                pat_id = int(int_list[0])
                pat_vert = int_list[1:]
                pat_dict[patient] = pat_vert


for pat_id, pat_vertx in pat_dict.items():
    final_dict = {}
    for vert_id in pat_vertx:
        vert_id = int(vert_id)
        pat_vertxs = tree_dict[vert_id]
        vertxs_set = set(pat_vertxs)
        for dis_id in range(n_disease):
            dis_id += 1
            dis_vert_ids = disease_dict[dis_id]
            total = 0
            vert_value = 0
            prev_vert_value = 0
            for dis_vert in dis_vert_ids:
                dis_vert = int(dis_vert)
                dis_vertxs = tree_dict[dis_vert]
                common = max(vertxs_set.intersection(dis_vertxs))
                vert_value = values_dict[common]
                vert_value = int(vert_value)
                if prev_vert_value > vert_value:
                    vert_value = prev_vert_value
                prev_vert_value = vert_value
            total += vert_value
            if dis_id in final_dict.keys():
                prev_total = final_dict.get(dis_id)
                sum = total + prev_total
                final_dict[dis_id] = sum
            else:
                final_dict[dis_id] = total
    print(f'final dict for patient {pat_id} - {final_dict}')
    max_key = max(final_dict, key=final_dict.get)
    out.write(str(max_key))
    out.write('\n')
            
        







            
    

    
        
        
