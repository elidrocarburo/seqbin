def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1  
    while left <= right:
        mid = left + (right - left) // 2  
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target: 
            left = mid + 1  
        else: 
            right = mid - 1  
    return -1 

arr = [3, 5, 7, 9, 11, 13, 15]
target = int(input("¿Qué número desea buscar?: "))

result = binary_search_iterative(arr, target)
if result != -1:
    print(f"El número {target} encontrado en el índice: {result}")
else:
    print(f"El número {target} no fue encontrado.")