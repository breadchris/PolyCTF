#include <string.h>
#include <stdio.h>
#include <unistd.h>

struct node {
    struct node* left;
    int value;
    struct node* right;
};

int main() {
    struct node paths[] = {
        {&paths[18], 0xdeadbeef, &paths[5]},
        {&paths[13], 0xcafebabe, &paths[0]},
        {&paths[4], 0xdeadbabe, &paths[0]},
        {&paths[2], 0x8badf00d, &paths[0]},
        {&paths[9], 0xb16b00b5, &paths[0]},
        {&paths[8], 0xcafed00d, &paths[0]},
        {&paths[5], 0xdeadc0de, &paths[0]},
        {&paths[7], 0xdeadfa11, &paths[0]},
        {&paths[10], 0xdefec8ed, &paths[0]},
        {&paths[11], 0xdeadfeed, &paths[0]},
        {&paths[0], 0xfee1dead, &paths[0]},
        {&paths[0], 0xfaceb00b, &paths[0]},
        {&paths[0], 0xfacefeed, &paths[0]},
        {&paths[0], 0x000ff1ce, &paths[0]},
        {&paths[0], 0x12345678, &paths[0]},
        {&paths[0], 0x743029ab, &paths[0]},
        {&paths[0], 0xdeed1234, &paths[0]},
        {&paths[0], 0x00000000, &paths[0]},
        {&paths[0], 0x11111111, &paths[0]},
        {&paths[0], 0x11111112, &paths[0]},
        {&paths[0], 0x11111113, &paths[0]},
        {&paths[0], 0x42424242, &paths[0]},
    };
    puts("Welcome to the Rabbit Hole");
    puts("--------------------------");
    puts("If you go down far enough, you will find what you are looking for.\n");
    puts("Where do you want to go in the rabbit hole?: ");
    

	return 0;
}
