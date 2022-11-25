#### This question has two different solution  
  
1. **Recursive**  
    view in this code and will know how to slove!  
  
    ```python  
         10  
       /    \  
     5      19  
           /  
         17  
    ```  
    this is the Problem three   
    ```python  
    self. maxDepth(10)  
    max(self. maxDepth(5), self. maxDepth(19)) + 1 # First recursive call from node 10  
    max(max(self. maxDepth(None), self. maxDepth(None)) + 1, self. maxDepth(19)) + 1  # Recursive call on node 5 and its expansion  
    max(1, self. maxDepth(19)) + 1 # Replacing for self. maxDepth(None) = 0   
    max(1, max(self. maxDepth(17), self. maxDepth(None)) + 1) + 1 # Recursive call from node 19  
    max(1, max(self. maxDepth(17), 0) + 1) + 1 # Replacing for self. maxDepth(None) = 0   
    max(1, max(max(self. maxDepth(None), self. maxDepth(None)) + 1, 0) + 1) + 1 # Recursive call from node 17  
    max(1, max(max(0, 0) + 1, 0) + 1) + 1 # Replacing for self. maxDepth(None) = 0  
    max(1, max(0 + 1, 0) + 1) + 1 # Replacing the inner most max  
    max(1, 1 + 1) + 1 # Replacing the inner most max  
    max(1, 2) + 1  
    2 + 1 # Replacing the inner most max  
    3  
    ```  
      
    ### And this slove's  
    * Time Complexity : O(n)  
    * Space C : ?  

2. **Iterative**  