total = 0
i = 0
ans=[]
word=[]
with open('words.txt', 'r', encoding='utf_8') as file_1:
    for line1 in file_1:
        word.append(line1.rstrip())
with open('org.txt', 'r', encoding='utf_8') as file_2:
    for line2 in file_2:
        i = i + 1
        for j in word:
            if j in line2:
                total += 1
                ans.append('Line'+str(i)+':'+'<'+j+'>'+j)
with open('ans3.txt','a',encoding='utf_8') as file_3:
    file_3.write('Total:'+str(total))
    for k in ans:
        file_3.write('\n'+k)
