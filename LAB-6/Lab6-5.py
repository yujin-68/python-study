a = [1,2,3]
b = [10,20,30]

a.append(b) #예상 결과 [1,2,3,[10,20,30]]
a.extend(b) #예상 결과 [1,2,3,10,20,30]

n_list = list(range(1,11))
n_list.insert(0,0)
