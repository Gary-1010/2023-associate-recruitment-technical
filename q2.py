lines = None
with open("file.txt") as file:
    lines = [line.rstrip().split() for line in file]
    
allValid = True

errorCodes = []

for line in lines[1:]:
    # print(line[1])
    if line[1] == "false":
        allValid = False
        errorCodes.append(line[2])
        
if allValid:
    print("Yes")
else:
    print("No")
    print(errorCodes)