**3 Sum closest problem**  

*complexity:* O(n*n)  
*Approach :* 
> Sort the given list  
> Have three pointers: current, next and last  
> sum = current+next+last, min = sum - target  
> if sum > target: last = last -1 or if sum < target: next = next + 1

---
