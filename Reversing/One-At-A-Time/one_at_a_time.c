#include <string.h>
#include <stdio.h>
#include <unistd.h>

// password = "flag{simple_right?}"

int main() {
    char eP[20];

    puts("Welcome to the Secret Door");
    puts("--------------------------");
    puts("If you know the secret, you can come in.\n");
    puts("Secret phrase please: ");
    fgets(eP, sizeof(eP), stdin);

    // Get rid of the trailing newline character
    size_t len = strlen(eP) - 1;
    if (eP[len] == '\n')
        eP[len] =  '\0';
    
    if (eP[0] == 'f' && eP[1] == 'l' && eP[2] == 'a' && eP[3] == 'g'
            && eP[4]  == '{' && eP[5]  == 's' && eP[6]  == 'i'
            && eP[7]  == 'm' && eP[8]  == 'p' && eP[9]  == 'l'
            && eP[10] == 'e' && eP[11] == '_' && eP[12] == 'r'
            && eP[13] == 'i' && eP[14] == 'g' && eP[15] == 'h'
            && eP[16] == 't' && eP[17] == '?' && eP[18] == '}')
        puts("Alright, come on in.");
    else
        puts("Sorry, I guess you don't know the secret.");

	return 0;
}
