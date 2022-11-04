vetor0 = []
vetor1 = []
vetorsoma = []

for i in range(2,21):
    if(i % 2 == 0):
        vetor0.append(i**2)
   
    if(i in range(10,20)):
        vetor1.append(i)

j = 0

while j < len(vetor0):
    vetorsoma.append(vetor0[j] + vetor1[j])
    
    j = j + 1

print('-'*50)
print('', vetorsoma, '')
print('-'*50)