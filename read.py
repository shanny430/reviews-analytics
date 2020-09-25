#留言分析程式
#print花時間，讓電腦讀取資料後少量print 使用計數count

data = []
count = 0
with open('reviews.txt', 'r')as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0 # %是用來求餘數
print(len(data)) #清單
print(data[0]) #印出清單第0個位置
print('--------') 
print(data[1]) 

