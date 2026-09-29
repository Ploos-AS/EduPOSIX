#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(void)
{
    printf("Hello from EduPOSIX! PID=%ld\n", (long)getpid());
    return 0;
}
