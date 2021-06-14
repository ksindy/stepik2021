'''
This code uses find() to return the first location of a motif within a larger string.
It then proceeds to loop using find() with a new start point n+1 of last found motif. 

- Expects and skips header in input file.
'''

# Open files and initialize variables, list, and string.
file = open("test-B.txt", "r")
out = open("ans-B.txt", "w")
string = ""
motif = ""
motif_list = []
motif_string = ""

a_file = file.readlines()[1:] #skip first line 
for line in a_file:
    line_len = len(line) 
    if line_len > 15:
        string = line.strip()
    else:
        motif = line.strip()
    if string and motif: # this allows the code to loop through again and assign the motif
        motif_loc = string.find(motif) # finds first motif in string
        if motif_loc == -1:
            print(f"motif {motif} not found in {string}.")
            break
        print(f"First motif is found at: {motif_loc}")
        motif_list.append(str(motif_loc+1))
        for m in range(len(string)): # ensures the code loops enough times to find all motifs
            motif_loc = string.find(motif, motif_loc+1) # searches again for the first occuring motif, this time starting n+1 from the last start location.
            if motif_loc != -1:
                motif_list.append(str(motif_loc+1))
            else:
                print(f"No more motifs to be found")
                break
        out.write(" ".join(motif_list))
        out.write("\n")
        motif_list = [] # reset list
        motif = "" # these ensure the correct motif and string are searched
        string = ""
out.close()

    
    