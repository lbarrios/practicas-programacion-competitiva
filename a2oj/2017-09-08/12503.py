T = int(input())
for t in range(T):
    n = int(input())
    instrucciones = list()
    for i in range(n):
        instruction = input()
        # left
        if len(instruction) == 4:
            instrucciones.append(-1)
        # right
        if len(instruction) == 5:
            instrucciones.append(1)
        # same as
        if len(instruction) > 5:
            old_instruction = int(instruction[8:])-1
            instrucciones.append(instrucciones[old_instruction])
    print(sum(instrucciones))