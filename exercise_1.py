test_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
length = len(test_dna)
a_count = test_dna.count('A')
t_count = test_dna.count('T')

at_content = (a_count + t_count) / length
print("AT content is " + str(at_content))
