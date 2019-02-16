import random

def Randomize_array(arr, n):
    for j in range(n-1,0,-1):
            # select a random index
        i = random.randint(0,j+1)
            #swapping
        arr[j],arr[i] = arr[i],arr[j]
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(arr)
shuffled_array = Randomize_array(arr,n)
print(shuffled_array)

