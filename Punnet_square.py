def combinations(input): 
	if len(input) == 1:
		return [input[0][0], input[0][1]]
	else:
		out = []
		for x in combinations(input[1:]):
			out.append(input[0][0] + x)
			out.append(input[0][1] + x)
		return out

def make_row(genotype,allel):
    out = []
    for i in genotype:
        out.append(allel+i)

    return out

def generate_table(genes,col):
    table = []
    for a in genes:
        table.append(make_row(col,a))
    return table

def print_table(table):
    print(" "*(len(table[0][0])),end = "")
    print(*[i[len(i)//2:] for i in table[0]],sep = " "*(len(table[0][0])-1))
    for row in table:
        print(row[0][:len(row[0])//2],end=" ")
        for item in row:
            print(f'|{item}|',end = "")
        print()


def main(parent_1,parent_2):
    genes_1 = combinations(parent_1)
    genes_2 = combinations(parent_2)
    table = generate_table(genes_1,genes_2)
    print_table(table)

# print("Enter genotypes with space between alleles ")
# parent_1 = str(input("Enter the genotype of parent 1: ")).split()
# parent_2 = str(input("Enter the genotype of parent 2: ")).split()
parent_1 = ['Xx','Yy','Yy']
parent_2 = ['Aa','Bb','Cc']
main(parent_1,parent_2)
