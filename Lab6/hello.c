#include <stdio.h>

void cExpressions() {
    printf("C EXPRESSIONS\n");
    // Declarations
    int a = -1, b=2;
    float x = 0.1;
    float y = 1.5;
    char c = 'p';

    printf("A\n");

    printf("%d / %d = %d\n", a, b, a/b); // a / b
    printf("%d * %d = %d\n", a, b, a*b); // a * b
    printf("(%d * 3) % 4 = %d\n", b, (b * 3) % 4);  // (b * 3) % 4
    printf("%f * %d = %f\n", x, a, x * a); // x * a
    printf("%f * %f = %f\n", x, y, x * y); // x * y
    printf("%f / %f = %f\n", y, x, y / x); // y / x
    printf("%c - 3 = %c\n", c, c - 3);  // c - 3

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
}

int main() {
    printf("Hello world!\n");
    printf("Welcome to INF1002!\n");

    cExpressions();

    return 0;

}