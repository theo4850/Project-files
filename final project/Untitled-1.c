#include <stdio.h>

int main() 
{
    int i, arr[] = {10, 20, 30, 40, 50}

    for(i=0; i < sizeof(arr)/sizeof(int); i++){
        printf("%d\n", arr[i]);
    }

    return 0;
}