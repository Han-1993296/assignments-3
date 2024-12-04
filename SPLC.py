from Bio import SeqIO
with open("/Users/han3/Downloads/rosalind_sseq.txt") as file:
    s, t = [str(record.seq) for record in SeqIO.parse(file, "fasta")]
    indices = []
start = 0
for char in t:
    start = s.find(char, start) + 1
    indices.append(start)


print(" ".join(map(str, indices)))


