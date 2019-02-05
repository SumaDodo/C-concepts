#include <stdio.h>

int main()
{
    int var = 1;
    int* ptr_var = NULL;
    ptr_var = &var;
    
    char* char_ptr = NULL;
    char_ptr = (char*)&var;
    
    printf("before increment : int_ptr: %u \t, char_ptr: %u\n", (unsigned int)ptr_var , (unsigned int)char_ptr);
    
    ptr_var++;
    char_ptr++;
    
    printf("After increment : int_ptr: %u \t, char_ptr: %u\n", (unsigned int)ptr_var , (unsigned int)char_ptr);
    
    return 0;
}
