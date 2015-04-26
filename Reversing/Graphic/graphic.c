#include <string.h>
#include <stdio.h>
#include <unistd.h>
#define BUFFERSIZE 64

struct node {
    struct node* left;
    int value;
    struct node* right;
};

int main() {
    int endValue = 1984717964;
	char path[64];
    struct node paths[] = {
        {&paths[18], 0xdeadbeef, &paths[5]},
        {&paths[13], 0xcafebabe, &paths[4]},
        {&paths[4], 0xdeadbabe, &paths[15]},
        {&paths[2], 0x8badf00d, &paths[16]},
        {&paths[9], 0xb16b00b5, &paths[20]},
        {&paths[8], 0xcafed00d, &paths[21]},
        {&paths[5], 0xdeadc0de, &paths[13]},
        {&paths[7], 0xdeadfa11, &paths[18]},
        {&paths[10], 0xdefec8ed, &paths[2]},
        {&paths[11], 0xdeadfeed, &paths[9]},
        {&paths[21], 0xfee1dead, &paths[8]},
        {&paths[20], 0xfaceb00b, &paths[14]},
        {&paths[19], 0xfacefeed, &paths[12]},
        {&paths[17], 0x000ff1ce, &paths[6]},
        {&paths[16], 0x12345678, &paths[3]},
        {&paths[15], 0x743029ab, &paths[0]},
        {&paths[1], 0xdeed1234, &paths[1]},
        {&paths[0], 0x00000000, &paths[17]},
        {&paths[3], 0x11111111, &paths[19]},
        {&paths[6], 0x11111112, &paths[1]},
        {&paths[12], 0x11111113, &paths[7]},
        {&paths[14], 0x42424242, &paths[10]},
    };
    puts("Welcome to the Rabbit Hole");
    puts("--------------------------");
    puts("If you go down far enough, you will find what you are looking for.\n");
    puts("Where do you want to go in the rabbit hole?: ");

	fgets(path, BUFFERSIZE, stdin);
    
    struct node* step = &paths[0];
    int value = step->value;

    int i;
    for (i = 0; i < BUFFERSIZE; i++) {
        if (path[i] == 'L') {
            step = step->left;
        } else if (path[i] == 'R') {
            step = step->right;
        } else if (path[i] == '\0' || path[i] == '\n') {
            break;
        }

        printf("You found a: %x!\n", step->value);
        value ^= step->value;
    }

    printf("At the end of your journey, your value became: %d\n", value);

    if (value == endValue) {
        puts("Bueno!");
    } else {
        puts("No Bueno");
    }
 
	return 0;
}
