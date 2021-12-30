#PATH SETTINGS
#--------------------------------------------------------------------------
import os.path
#NOTE: Slightly nicer way of handling paths
#save_path = "C:/Users/micha/OneDrive/GoodNotes/Projects/Protein_Identification"
#npep_dir = os.path.join(save_path, 'npep')
#--------------------------------------------------------------------------


#GENERATE PEPTIDES
#--------------------------------------------------------------------------
from itertools import permutations

#list of aminoacids
aacids = ["A","R","N","D","C","E","Q","G","H","I","L","K","M","F","P","S","T","W","Y","V"]

def generatePermutations(chars, n):
    """
    Generate all combinations of letters in chars of size n
    """
    combilist = [''.join(perm) for perm in permutations(chars, n)]
    return combilist

# create npeps
dipeps = generatePermutations(aacids, 2)
tripeps = generatePermutations(aacids, 3)
tetrapeps = generatePermutations(aacids, 4)
di = len(dipeps)
tri = len(tripeps)
tetra = len(tetrapeps)
print("di", di)
print("tri", tri)
print("tetra", tetra)

#output location file header preparation
#f_tripeps = open(os.path.join(npep_dir, "tripeps.txt"), "w")
f_tripeps = open("C:\\Users\\sergi\\Desktop\\projects\\peptides\\tripep.txt", "w") #ACHTUNG CHANGE PATH

#fill file with combinations in proper format
f_tripeps.write("name")
for j in tripep:
    f_tripeps.write("\t")
    f_tripeps.write(j)
f_tripeps.write("\t")
f_tripeps.write("total")
f_tripeps.write("\n")
f_tripeps.close()

#f_tripeps_tot = open(os.path.join(npep_dir, "tripeps_tot.txt"), "w")  #ACHTUNG CHANGE PATH
f_tripeps_tot = open("C:\\Users\\sergi\\Desktop\\projects\\peptides\\tripep_tot.txt", "w")  #ACHTUNG CHANGE PATH
f_tripeps_tot.write("total")
for j in tripeps:
    f_tripeps_tot.write("\t")
    f_tripeps_tot.write(j)
else: f_tripeps_tot.write("\n")
f_tripeps_tot.close()
#--------------------------------------------------------------------------


#PREPARE PROTEOME
#--------------------------------------------------------------------------
# Open a file: file
#f_proteome = open(os.path.join(save_path, "uniproteomerev.fasta"))
f_proteome = open('C:\\Users\\sergi\\Downloads\\uniproteomerev.fasta' , "r")  #ACHTUNG CHANGE PATH
proteome = f_proteome.read()
f_proteome.close()
#--------------------------------------------------------------------------


#COUNT OCCURENCES
#--------------------------------------------------------------------------
import timeit
import random

#filling files
#f_tripeps = open(os.path.join(npep_dir, "tripeps.txt"), "a")  #ACHTUNG CHANGE PATH
f_tripeps = open("C:\\Users\\sergi\\Desktop\\projects\\peptides\\tripep.txt", "a") #ACHTUNG CHANGE PATH

#split and clip
entries = proteome.split(">")
entries = entries[1:]

#time runtime of algorithm
starttime = timeit.default_timer()

#for each protein, count occurences of specific tripeptides
for entry in entries:
    #seperate entry format
    prot = entry.split("\n", 1)
    
    #if input is not accessible, ignore
    #NOTE: Here should be some sort of error handling - why does it not work sometimes?
    try:
        seq = prot[1].replace("\n", "")
    except:
        seq = ""
    
    #extract protein ID
    prot_id = prot[0]
    
    #write ID to file
    f_tripeps.write(prot_id)
    
    #counter for total number of occurences
    tot = 0
    
    #count number of occurences of each motif in each protein
    for tripep in tripeps:
        #counts occurences of substring of another string
        count = seq.count(tripep)
        #count = len(re.findall(tripep,seq)) -> This caused it to be relatively slow
        
        #document results
        f_tripeps.write("\t")
        f_tripeps.write(str(count))
        
        #add to total occurences
        tot += count
        
    #NOTE: Where is the if for this else?
    else:
        #
        f_tripeps.write("\t")
        f_tripeps.write (str(tot))
        
    #format
    f_tripeps.write ("\n")

#close outstream
f_tripeps.close()

#print time it took
print("The time difference is :", timeit.default_timer() - starttime)
#--------------------------------------------------------------------------
