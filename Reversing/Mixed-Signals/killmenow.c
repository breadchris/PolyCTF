#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <unistd.h>
#include <fcntl.h>

void lolno(int signum) {
  signal(signum, SIG_IGN);
  puts("won't stop");
  signal(signum, lolno);
}

void keyme(int signum) {
  signal(signum, SIG_IGN);
  char buf[32];
  int key = open("key.txt", O_RDONLY);
  read(key, buf, 32);
  printf("%s\n", buf);
  close(key);
  signal(signum, keyme);
}

void nobreak(int signum) {
  signal(signum, SIG_IGN);
  puts("gimme a break");
  signal(signum, nobreak);
}

void stahp(int signum) {
  signal(signum, SIG_IGN);
  puts("stahp it");
  signal(signum, stahp);
}

// so far I only handle 5 signals, one giving the key.
// Feel free to add more handlers if you want.
int main(void) {
  signal(SIGINT, lolno);
  signal(SIGQUIT, lolno);
  signal(SIGUSR1, keyme);
  signal(SIGTRAP, nobreak);
  signal(SIGABRT, stahp);
  signal(SIGTSTP, stahp);
  
  while(1) {
    puts("can't stop");
    sleep(1);
  }
}
