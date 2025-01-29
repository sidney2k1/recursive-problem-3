#phone keypad
keypad=[" "," ","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
def printcombination(combination,curr,output,n):
    if curr==n:
        print(*output,sep=" ")
        return
    for i in range(len(keypad[combination[curr]])):
        output.append(keypad[combination[curr]][i])
        printcombination(combination,curr+1,output,n)
        output.pop()
        if(combination[curr]==0 or combination[curr]==1):
            return
combination=[4,3,4]
n=len(combination)
printcombination(combination,0,[],n)