#include <stdio.h>

void inputAndCalculations(){
    printf("BMI CALCULATOR\n\n");

    float weight, height, bmi;

    printf("Enter your weight in kilograms : ");
    scanf("%f", &weight);

    printf("Enter your height in metres : ");
    scanf("%f", &height);

    bmi = weight / (height * height);

    if (bmi < 18.5) 
    {
        printf("Your BMI is %.1f. That is within the underweight range", bmi);
    }
    else if (bmi > 18.5)
    {
        printf("Your BMI is %.1f. That is within the normal range", bmi);
    }
    else if (bmi > 25.0 && bmi < 29.9)
    {
        printf("Your BMI is %.1f. That is within the overweight range", bmi);
    }
    else
    {
        printf("Your BMI is %.1f. That is within the obese range", bmi);
    }

}// inputAndCalculations

void cExpressions() {
    printf("C EXPRESSIONS\n");
    // Declarations
    int a = -1, b=2;
    float x = 0.1;
    float y = 1.5;
    char c = 'p';

    printf("********A********\n");

    printf("%d / %d = %d\n", a, b, a/b); // a / b
    printf("%d * %d = %d\n", a, b, a*b); // a * b
    printf("(%d * 3) % 4 = %d\n", b, (b * 3) % 4);  // (b * 3) % 4
    printf("%f * %d = %f\n", x, a, x * a); // x * a
    printf("%f * %f = %f\n", x, y, x * y); // x * y
    printf("%f / %f = %f\n", y, x, y / x); // y / x
    printf("%c - 3 = %c\n", c, c - 3);  // c - 3

    printf("********B********\n");

    printf("%4d\n", a);             //   -1
    printf("%04d\n", a);            // -001
    printf("a / b = %d\n", a / b);  // a / b = 0
    printf("%x\n", b);              // 2
    printf("%.2f\n", y);            // 1.50
    printf("%10.1f\n", x);          //       0.1
    printf("c = \t%c\n", c);          // c =    p
    
    /*
        format specifiers in C
        %d or %i    decimal int or signed int
        %c          signed character
        %f          signed float
        %e          a floating-point number
        %s          a string or a sequence of character
        %lf         double          lowercase L
        %Lf         long double     uppercase L
        %o          octal integer
        %u          short signed integer
        %ld         long decimal integer
        %x          hexadecimal integer
        %p          print memory address in the hexadecimal form
    */
} // cExpressions

int main() {
    printf("Hello world!\n");
    printf("Welcome to INF1002!\n");

    // cExpressions();
    inputAndCalculations();

    return 0;

} // main