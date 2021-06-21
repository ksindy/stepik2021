import pandas as pd
import numpy as np

# Open files and initialize variables, list, and string.
# file = open("diag-A.txt", "r")
# out = open("diag-A-ans.txt", "w")
file = open("test3_diag.txt", "r")
out = open("ans-A3-diag.txt", "w")
# out2 = open("ans-A1-diag.txt", "w")
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
        # for vert_index, vert in enumerate(int_list):
        # for index, vert in enumerate(int_list, 1):
        #     vert = int(vert)
        #     ordered_vert_list.append(vert)
        # ordered_vert_list.sort()
        # # print(ordered_vert_list)
        # print(int_list)
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
        # print(tree_dict)
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
    # print(f'\n')
    # print(f'pat_id {pat_id}')
    for vert_id in pat_vertx:
        vert_id = int(vert_id)
        pat_vertxs = tree_dict[vert_id]
        # print(f'\n')
        # print("patient vertx")
        # print(pat_vertxs)
        vertxs_set = set(pat_vertxs)
        for dis_id in range(n_disease):
            # print(f'vert_id {vert_id}')
            
            dis_id += 1
            dis_vert_ids = disease_dict[dis_id]
            total = 0
            vert_value = 0
            prev_vert_value = 0
            for dis_vert in dis_vert_ids:
                # print(f'dis_vert {dis_vert}')
                dis_vert = int(dis_vert)
                dis_vertxs = tree_dict[dis_vert]
                common = max(vertxs_set.intersection(dis_vertxs))
                vert_value = values_dict[common]
                vert_value = int(vert_value)
                if prev_vert_value > vert_value:
                    vert_value = prev_vert_value
                prev_vert_value = vert_value
                # print(f'prev_vert_value {prev_vert_value}')
            total += vert_value
            # print(f'total for disease {dis_id} in {pat_id} is {total}')

            # print(f"total {total}")
            # print(f"DISEASE {dis_id} vertx")
            # print(dis_vertxs)
            if dis_id in final_dict.keys():
                prev_total = final_dict.get(dis_id)
                sum = total + prev_total
                final_dict[dis_id] = sum
            else:
                final_dict[dis_id] = total
    print(f'final dict for patient {pat_id} - {final_dict}')
    # print(f'FINAL DICT {final_dict}')
    max_key = max(final_dict, key=final_dict.get)
    # print(f'max key {max_key}')
    out.write(str(max_key))
    out.write('\n')
            
        
    #for dis_id, dis_vertx in disease_dict.items():
# print(tree_dict)
# print(values_dict)
# print(pat_dict)
# print(disease_dict)






            
    

    
            # if vert == prev_vert:
            #     child_vert += 1
            #     if verts: 
            #         vert_list.append(child_vert)
            #         tree_dict[child_vert] = vert_list
            #     else:
            #         tree_dict[child_vert] = [vert, child_vert]
            #     prev_vert = vert
                
            # else:
            #     print('else')
            #     child_vert += 1
            #     print(vert)
            #     verts = list(tree_dict.get(vert))
            #     print(type(verts))
            #     print(type(child_vert))
            #     verts.append(child_vert)
            #     tree_dict[child_vert] = verts
            #     prev_vert = vert
            # print(tree_dict)
            # # if vert == prev_vert:
            # #     tree_dict[vert_key] = [vert, vert+step]
            # #     step += 1
            # #     vert_key += 1
            # # if vert != prev_vert:
            # #     tree_dict[vert_key] = [vert, vert+step]
            # #     step += 1
            # #     vert_key += 1
            

            
            # # while int(vert_list[vert_index+1]) ==  vert:
            # # #if int(vert_list[vert_key+1]) ==  vert:
            # #     vert_key += 1
            # #     vert_index += 1
            # #     step += 1
            # #     tree_dict[vert_key] = [vert, step]
            # #     print(tree_dict)
        
