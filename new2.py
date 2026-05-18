def linear_search(arr, target):
      for i in range(len(arr)):
          if arr[i] == target:
              return i
      return -1
  
arr = ['Rice','Sugar','Milk','Oil','Soap']
target = 'Milk'
result = linear_search(arr, target)
  
if result != -1:
    print(f"Product found ")
else:
    print("Product not found")
  
