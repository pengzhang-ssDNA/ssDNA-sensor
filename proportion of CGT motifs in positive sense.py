import re

# Read the AAV2 genome sequence from the FASTA file
with open("D:/R/CGT_Motif/AAV2.fasta", "r") as f:
    genome = f.read()

# Remove FASTA header line and concatenate sequence lines
genome = "".join(genome.split("\n")[1:])

# Define the pattern and search for matches. For CGT/A motif, replace the following regular express with 'CG[TA]'
matches = re.findall(r'(CG[TA][CGTA]{0,30}GGG)', genome)

# Calculate the proportion of the pattern in the genome
proportion = len(matches) / len(genome)

print(f"The proportion of the pattern CGTA in the AAV2 genome is {proportion:.5f}")


input("Press any key to exit...")
