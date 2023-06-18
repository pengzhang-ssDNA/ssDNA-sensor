import re

# Read the AAV2 genome sequence from the FASTA file
with open("D:/R/CGT_Motif/AAV2.fasta", "r") as f:
    genome = f.read()

# Remove FASTA header line and concatenate sequence lines
genome = "".join(genome.split("\n")[1:])

# Define the pattern and search for matches
matches = re.findall(r'(?<=.{7})(.{7}CG[TA][CGTA]{3,5}GGG.{7})(?=.{7})', genome)

sequences = [match for match in matches]

with open('AAV2.txt', 'w') as f:
    for seq in sequences:
        f.write(seq + '\n')

# Calculate the proportion of the pattern in the genome
proportion = len(matches) / len(genome)

print(f"The proportion of the pattern CG[T,A]N{{3,5}}GGG in the AAV2 genome is {proportion:.5f}")


input("Press any key to exit...")


