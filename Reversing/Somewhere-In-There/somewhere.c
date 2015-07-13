#include <string.h>
#include <stdio.h>
#include <unistd.h>

int main() {
    char password[20];
    char flag[] = "flag{no_source_no_problem}";

    puts("GImME THE PAssWorDD PLSSS: ");
    fgets(password, sizeof(password), stdin);

    size_t len = strlen(password) - 1;
    if (password[len] == '\n')
        password[len] =  '\0';
    
    if (strcmp(password, flag) == 0)
        puts("YUP THAT's RIghT!!!");
    else
        puts("NOOOOooOOOooooOO DOOOood");

	return 0;
}
