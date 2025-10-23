#include <stdio.h>

void decimalToBinary(int n) {
    // Array to store binary number
    int binaryNum[32];
  
    // Counter for binary array
    int i = 0;
    while (n > 0) {
        // Store remainder when number is divided by 2
        binaryNum[i] = n % 2;
        n = n / 2;
        i++ ;
    }
  
    // Print binary array in reverse order
    for (int j = i - 1; j >= 0; j--)
        printf("%d", binaryNum[j]);
}

int main() {
    int num;
    printf("Enter a decimal number: ");
    scanf("%d", &num);
    printf("The binary equivalent is: ");
    decimalToBinary(num);
    printf("\n");
    return 0;
}
