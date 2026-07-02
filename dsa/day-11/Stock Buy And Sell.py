#Stock Buy and Sell
arr = [7,1,5,3,6,4]
def stock(arr):
    
    smallest = arr[0]
    largest_profit = 0
    
    for i in range(1,len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            
        profit = arr[i] - smallest
        
        if profit > largest_profit:
            largest_profit = profit
    
    return largest_profit

stock(arr)
