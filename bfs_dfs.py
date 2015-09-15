adc_lst = {
            1: [3, 6],
            2: [4, 7],
            3: [1, 5, 7],
            4: [2, 6],
            5: [3, 7],
            6: [1, 4],
            7: [2, 3, 5]
           }

stack = []
seen = []
current = None

def dfs(vtx):
    if len(adc_lst[vtx]) is not 0 and vtx not in seen:
        seen.append(vtx)
        for item in adc_lst[vtx]:
            if len(seen) is len(adc_lst):
                break
            else:
                dfs(item)



def bfs(vtx):
    if vtx not in seen:
        seen.append(vtx)
        for item in adc_lst[vtx]:
            if len(seen) is len(adc_lst):
                break
            else:
                if item not in seen and item not in stack:
                    stack.append(item)
        if stack:
            current = stack[0]
            stack.remove(stack[0])
            bfs(current)


bfs(1)
print seen

