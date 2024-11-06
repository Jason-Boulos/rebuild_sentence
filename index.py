


def rebuild_sentence(words, lengths):
    new_list=[]
    for i in range(len(words)):
    #googled it' In Python, [:] after a variable name denotes slicing a list or string. 
       new_list.append(words[i][:lengths[i]])
    return " ".join(new_list)

#another method if i dont wana use slice for strings
# def rebuild_sentence(words, lengths):
#new_list=[]
#for i in range(len(words)):
# new_word=''
# for j in range length[i]:
# new_world+=words[i][j]
# new_list.append(new_world)


result = rebuild_sentence(["the", "sky", "is", "blue"], [3, 2, 2, 1])
print(result) 
            
            
    