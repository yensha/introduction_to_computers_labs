import json

#排列函式(截自網路)
def Perm(arrs): 
    # 若輸入 [1,2,3]，則先取出1，將剩餘的 [2,3]全排列得到 [[2,3],[3,2]]，
    #               再將 1加到全排列 [[2,3],[3,2]]上變成 [[1,2,3],[1,3,2]]
    # 同理，取出2或者3時，得到的分別是 [[2,1,3],[2,3,1]]和 [[3,1,2],[3,2,1]]
    if len(arrs)==1:
        return [arrs]
    result = []  # 最終的結果（即全排列的各種情況）
    for i in range(len(arrs)):  
        rest_arrs = arrs[:i]+arrs[i+1:]  # 取出arrs中的第 i個元素後剩餘的元素
        rest_lists = Perm(rest_arrs)   # 剩餘的元素完成全排列
        lists = []
        for term in rest_lists:
            lists.append(arrs[i:i+1]+term)  # 將取出的第 i個元素加到剩餘全排列的前面
        result += lists
    return result #二維矩陣
  
#計算assignment & cost
def BF(input):
    #N-->員工人數
    N = len(input)
    #agent當作員工們
    agent = []
    #cost_list 儲存: agent所有排列方式下的cost總和(cost_sum)
    cost_list = []
    for i in range(N):
        agent.append(i)
    #將Perm回傳的所有陣列排列存入agent_pointer
    agent_pointer = Perm(agent)
    for j in range(len(agent_pointer)):
        #cost_sum儲存某種排列下的總成本
        cost_sum = 0
        sequence = agent_pointer[j]
        #用for迴圈讀取input中的值
        for k in range(N):
            cost_sum += input[k][sequence[k]]
        cost_list.append(cost_sum)
    #cost儲存成本最小值
    cost = min(cost_list)
    #儲存成本最小值在cost_list中位置
    index = cost_list.index(cost)
    assignment = agent_pointer[index]
    return assignment, cost

# main
with open('input.json', 'r') as inputFile:
    data = json.load(inputFile) # load data
    for key in data:
        input = data[key] # load each input

        # show input data and number of the Tasks
        #print(input)-->可檢查是否正確取得數據
        
        # Brute Force Algorithm
        assignment, cost = BF(input)

        print('Question: ' + str(key))
        print('Assignment:', assignment)
        print('Cost:', cost)
        print()
