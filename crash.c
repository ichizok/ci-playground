#include <stdlib.h>
int main()
{
    free((void *)0x1);
    return 0;
}
