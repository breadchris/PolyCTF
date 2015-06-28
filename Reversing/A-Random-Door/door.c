#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#define N_RAND 4
typedef unsigned int uint;

void print_flag() {
}

void gen_random_nums(uint *nums, int length)
{
    srand(time(NULL));
    for(int i = 0; i < length; i++)
    {
        nums[i] = rand();
    }
}

void validate_code(uint code, uint *nums, int length)
{
    uint test_code = 0x1337beef;

    for (int i = 0; i < length; i++) {
        test_code += nums[i] >> 7;
    }

    for (int i = 0; i < length; i++) {
        test_code |= nums[i] >> 16;
        test_code |= (nums[i] & 0xffff) << 16;
    }

    for (int i = 0; i < length; i++) {
        test_code ^= nums[i];
    }

    if (code == test_code) {
        puts("\n()()()() CODE ACCEPTED ()()()()");
    } else {
        puts("\n)(-)(-)( CODE REJECTED )(-)(-)(");
    }
}

void system_init()
{
    uint rand_nums[N_RAND];
    uint code;
    
    gen_random_nums(rand_nums, N_RAND);
    puts("------------d--------3-------------c-");
    puts("--6----2--------------------7--------");
    puts("------------ DOOR LOCKED -------b----");
    puts("-----1--e------------4------9--------");
    puts("--5------0------f----------------a---");
    for (int i = 0; i < 37; i++) {
        printf(".");
        fflush(stdout);
        //sleep(1);
    }
    puts("\n\n:::::: SYSTEM CORE MALFUNCTION ::::::");
    for (int i = 1; i < N_RAND + 1; i++)
    {
        printf("------- CORE VALUE %d: %d\n", i, rand_nums[i-1]);
    }
    puts("<<<< Oh well, we will do it live <<<<");
    for (int i = 0; i < 37; i++) {
        printf(".");
        fflush(stdout);
        //sleep(1);
    }
    puts("\n\n>>>> ENTER VALIDATION CODE >>>>");
    printf("CODE: ");
    scanf("%d", &code);

    validate_code(code, rand_nums, N_RAND);
}

int main()
{
    system_init();
	return 0;
}
