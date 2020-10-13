#include <stdio.h>
int main()
{
    char *s = ".";
    fprintf(stderr, "0:%s\n", s);
    *s = 'x';
    fprintf(stderr, "1:%s\n", s);
    return 0;
}
