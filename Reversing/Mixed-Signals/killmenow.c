/*
 * INT  | 1 | 2 | 3 | 4 | 5 -> key
 * QUIT | 3 | 6 | 1 | 8 | L
 * ABRT | 5 | 3 | 3 | 2 | A
 * TRAP | 1 | 1 | 3 | 6 | P
 * TSTP | 4 | 3 | 6 | 1 | L
 * CONT | 3 | 2 | 4 | 7 | A
 * USR1 | 1 | 2 | 7 | 3 | C
 * USR2 | 2 | 5 | 9 | 1 | E
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <signal.h>
#include <unistd.h>
#include <fcntl.h>

void int1(int signum);
void int2(int signum);
void int3(int signum);
void int4(int signum);
void int5(int signum);
void quit1(int signum);
void quit2(int signum);
void quit3(int signum);
void quit4(int signum);
void quit5(int signum);
void quit6(int signum);
void quit7(int signum);
void quit8(int signum);
void quit9(int signum);
void abrt1(int signum);
void abrt2(int signum);
void abrt3(int signum);
void abrt4(int signum);
void abrt5(int signum);
void abrt6(int signum);
void abrt7(int signum);
void abrt8(int signum);
void abrt9(int signum);
void trap1(int signum);
void trap2(int signum);
void trap3(int signum);
void trap4(int signum);
void trap5(int signum);
void trap6(int signum);
void trap7(int signum);
void trap8(int signum);
void trap9(int signum);
void tstp1(int signum);
void tstp2(int signum);
void tstp3(int signum);
void tstp4(int signum);
void tstp5(int signum);
void tstp6(int signum);
void tstp7(int signum);
void tstp8(int signum);
void tstp9(int signum);
void cont1(int signum);
void cont2(int signum);
void cont3(int signum);
void cont4(int signum);
void cont5(int signum);
void cont6(int signum);
void cont7(int signum);
void cont8(int signum);
void cont9(int signum);
void usr11(int signum);
void usr12(int signum);
void usr13(int signum);
void usr14(int signum);
void usr15(int signum);
void usr16(int signum);
void usr17(int signum);
void usr18(int signum);
void usr19(int signum);
void usr21(int signum);
void usr22(int signum);
void usr23(int signum);
void usr24(int signum);
void usr25(int signum);
void usr26(int signum);
void usr27(int signum);
void usr28(int signum);
void usr29(int signum);
void keyme(int signum);

int SIGNALS[] = { SIGQUIT, SIGABRT, SIGTRAP, SIGTSTP, SIGCONT, SIGUSR1, SIGUSR2 };

void int1(int signum) {
  signal(signum, SIG_IGN);
  puts("won't stop");
  void (*p[]) (int signum) = { quit3, abrt5, trap1, tstp4, cont3, usr11, usr22 };
  struct sigaction test_act;
  for(int i = 0; i < 7; i++) {
    sigaction(SIGNALS[i], NULL, &test_act);
    if(test_act.sa_handler != p[i]) {
      signal(signum, int1);
      return;
    }
  }
  signal(signum, int2);
}

void int2(int signum) {
  signal(signum, SIG_IGN);
  puts("ok I might stop");
  void (*p[]) (int signum) = { quit6, abrt3, trap1, tstp3, cont2, usr12, usr25 };
  struct sigaction test_act;
  for(int i = 0; i < 7; i++) {
    sigaction(SIGNALS[i], NULL, &test_act);
    if(test_act.sa_handler != p[i]) {
      signal(signum, int1);
      return;
    }
  }
  signal(signum, int3);
}

void int3(int signum) {
  signal(signum, SIG_IGN);
  puts("but not now");
  void (*p[]) (int signum) = { quit1, abrt3, trap3, tstp6, cont4, usr17, usr29 };
  struct sigaction test_act;
  for(int i = 0; i < 7; i++) {
    sigaction(SIGNALS[i], NULL, &test_act);
    if(test_act.sa_handler != p[i]) {
      signal(signum, int1);
      return;
    }
  }
  signal(signum, int4);
}

void int4(int signum) {
  signal(signum, SIG_IGN);
  puts("Congrats, here's the key: flag{fool_me_once}");
  sleep(1);
  puts("PSYCH!");
  void (*p[]) (int signum) = { quit8, abrt2, trap6, tstp1, cont7, usr13, usr21 };
  struct sigaction test_act;
  for(int i = 0; i < 7; i++) {
    sigaction(SIGNALS[i], NULL, &test_act);
    if(test_act.sa_handler != p[i]) {
      signal(signum, int1);
      return;
    }
  }
  signal(signum, int5);
}

void int5(int signum) {
  signal(signum, SIG_IGN);
  void (*p[]) (int signum) = { quit2, abrt4, trap7, tstp7, cont3, usr16, usr29 };
  struct sigaction test_act;
  for(int i = 0; i < 7; i++) {
    sigaction(SIGNALS[i], NULL, &test_act);
    if(test_act.sa_handler != p[i]) {
      signal(signum, int1);
      return;
    }
  }
  puts("YOU WIN! EXIT AS YOU NORMALLY WOULD.");
  signal(signum, keyme);
}

void quit1(int signum) {
  signal(signum, SIG_IGN);
  puts("IIIII");
  signal(signum, quit2);
}

void quit2(int signum) {
  signal(signum, SIG_IGN);
  puts("Just want to telL you how I'm feeling");
  signal(signum, quit3);
}

void quit3(int signum) {
  signal(signum, SIG_IGN);
  puts("Gotta make you understand");
  signal(signum, quit4);
}

void quit4(int signum) {
  signal(signum, SIG_IGN);
  puts("Never gonna give you up");
  signal(signum, quit5);
}

void quit5(int signum) {
  signal(signum, SIG_IGN);
  puts("Never gonna let you down");
  signal(signum, quit6);
}

void quit6(int signum) {
  signal(signum, SIG_IGN);
  puts("Never gonna run around and desert you");
  signal(signum, quit7);
}

void quit7(int signum) {
  signal(signum, SIG_IGN);
  puts("Never gonna make you cry");
  signal(signum, quit8);
}

void quit8(int signum) {
  signal(signum, SIG_IGN);
  puts("Never gonna say goodbye");
  signal(signum, quit9);
}

void quit9(int signum) {
  signal(signum, SIG_IGN);
  puts("Never gonna tell a lie and hurt you");
  signal(signum, quit1);
}

void abrt1(int signum) {
  signal(signum, SIG_IGN);
  puts("IIIIIn");
  signal(signum, abrt2);
}

void abrt2(int signum) {
  signal(signum, SIG_IGN);
  puts("West Philadelphia born and raised");
  signal(signum, abrt3);
}

void abrt3(int signum) {
  signal(signum, SIG_IGN);
  puts("On the playground was where I spent most of my days");
  signal(signum, abrt4);
}

void abrt4(int signum) {
  signal(signum, SIG_IGN);
  puts("Chillin' out maxin' relAxin' all cool");
  signal(signum, abrt5);
}

void abrt5(int signum) {
  signal(signum, SIG_IGN);
  puts("And all shooting some b-ball outside of the school");
  signal(signum, abrt6);
}

void abrt6(int signum) {
  signal(signum, SIG_IGN);
  puts("When a couple of guys who were up to no good");
  signal(signum, abrt7);
}

void abrt7(int signum) {
  signal(signum, SIG_IGN);
  puts("Started making trouble in my neighborhood");
  signal(signum, abrt8);
}

void abrt8(int signum) {
  signal(signum, SIG_IGN);
  puts("I got in one little fight and my mom got scared");
  signal(signum, abrt9);
}

void abrt9(int signum) {
  signal(signum, SIG_IGN);
  puts("She said, \"You're movin' with your auntie and uncle in Bel-Air.\"");
  signal(signum, abrt1);
}

void trap1(int signum) {
  signal(signum, SIG_IGN);
  puts("May the Force be with us.");
  signal(signum, trap2);
}

void trap2(int signum) {
  signal(signum, SIG_IGN);
  puts("We've got to be able to get some kind of a reading on that shield, up or down.");
  signal(signum, trap3);
}

void trap3(int signum) {
  signal(signum, SIG_IGN);
  puts("Well, how could they be jamming us if they don't know if we're coming.");
  signal(signum, trap4);
}

void trap4(int signum) {
  signal(signum, SIG_IGN);
  puts("Break off the attack! The shield is still up.");
  signal(signum, trap5);
}

void trap5(int signum) {
  signal(signum, SIG_IGN);
  puts("I get no reading. Are you sure?");
  signal(signum, trap6);
}

void trap6(int signum) {
  signal(signum, SIG_IGN);
  puts("Pull up! All craft pull up!");
  signal(signum, trap7);
}

void trap7(int signum) {
  signal(signum, SIG_IGN);
  puts("Take evasive action! Green GrouP, stick close to holding sector MV-7.");
  signal(signum, trap8);
}

void trap8(int signum) {
  signal(signum, SIG_IGN);
  puts("Admiral, we have enemy ships in sector 47.");
  signal(signum, trap9);
}

void trap9(int signum) {
  signal(signum, SIG_IGN);
  puts(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ___________");
  puts(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ./ It’s a trap! \\");
  puts(". . . . . . . . . . . . . . . . _,,,--~~~~~~~~--,_ . . . . . . . . . \\ .___________/");
  puts(". . . . . . . . . . . . . . ,-‘ : : : :::: :::: :: : : : : :º ‘-, . . \\/. . . . . .. . .");
  puts(". . . . . . . . . . . . .,-‘ :: : : :::: :::: :::: :::: : : :o : ‘-, . . . . . . . . . .");
  puts(". . . . . . . . . . . ,-‘ :: ::: :: : : :: :::: :::: :: : : : : :O ‘-, . . . . . . . . .");
  puts(". . . . . . . . . .,-‘ : :: :: :: :: :: : : : : : , : : :º :::: :::: ::’; . . . . . . . .");
  puts(". . . . . . . . .,-‘ / / : :: :: :: :: : : :::: :::-, ;; ;; ;; ;; ;; ;; ;\\ . . . .  . . .");
  puts(". . . . . . . . /,-‘,’ :: : : : : : : : : :: :: :: : ‘-, ;; ;; ;; ;; ;; ;;| . . . . . . .");
  puts(". . . . . . . /,’,-‘ :: :: :: :: :: :: :: : ::_,-~~,_’-, ;; ;; ;; ;; | . . . . . . .");
  puts(". . . . . _/ :,’ :/ :: :: :: : : :: :: _,-‘/ : ,-‘;’-‘’’’’~-, ;; ;; ;;,’ . . . . . . . .");
  puts(". . . ,-‘ / : : : : : : ,-‘’’ : : :,--‘’ :|| /,-‘-‘--‘’’__,’’’ \\ ;; ;,-‘ . . . . . . . .");
  puts(". . . \\ :/,, : : : _,-‘ --,,_ : : \\ :\\ ||/ /,-‘-‘x### ::\\ \\ ;;/ . . . . . . . . . .");
  puts(". . . . \\/ /---‘’’’ : \\ #\\ : :\\ : : \\ :\\ \\| | : (O##º : :/ /-‘’ . . . . . . . . . . .");
  puts(". . . . /,’____ : :\\ ‘-#\\ : \\, : :\\ :\\ \\ \\ : ‘-,___,-‘,-`-,, . . . . . . . . . . .");
  puts(". . . . ‘ ) : : : :’’’’--,,--,,,,,,¯ \\ \\ :: ::--,,_’’-,,’’’¯ :’- :’-, . . . . . . . . .");
  puts(". . . . .) : : : : : : ,, : ‘’’’~~~~’ \\ :: :: :: :’’’’’¯ :: ,-‘ :,/\\ . . . . . . . . .");
  puts(". . . . .\\,/ /|\\\\| | :/ / : : : : : : : ,’-, :: :: :: :: ::,--‘’ :,-‘ \\ \\ . . . . . . . .");
  puts(". . . . .\\\\’|\\\\ \\|/ ‘/ / :: :_--,, : , | )’; :: :: :: :,-‘’ : ,-‘ : : :\\ \\, . . . . . . .");
  puts(". . . ./¯ :| \\ |\\ : |/\\ :: ::----, :\\/ :|/ :: :: ,-‘’ : :,-‘ : : : : : : ‘’-,,_ . . . .");
  puts(". . ..| : : :/ ‘’-(, :: :: :: ‘’’’’~,,,,,’’ :: ,-‘’ : :,-‘ : : : : : : : : :,-‘’’\\\\ . . . .");
  puts(". ,-‘ : : : | : : ‘’) : : :¯’’’’~-,: : ,--‘’’ : :,-‘’ : : : : : : : : : ,-‘ :¯’’’’’-,_ .");
  puts("./ : : : : :’-, :: | :: :: :: _,,-‘’’’¯ : ,--‘’ : : : : : : : : : : : / : : : : : : :’’-,");
  puts("/ : : : : : -, :¯’’’’’’’’’’’¯ : : _,,-~’’ : : : : : : : : : : : : : :| : : : : : : : : :");
  puts(": : : : : : :¯’’~~~~~~’’’ : : : : : : : : : : : : : : : : : : | : : : : : : : : :");
  signal(signum, trap1);
}

void tstp1(int signum) {
  signal(signum, SIG_IGN);
  puts("And who are you, the proud lord said, that I must bow so low?");
  signal(signum, tstp2);
}

void tstp2(int signum) {
  signal(signum, SIG_IGN);
  puts("Only a cat of a different coat, that's all the truth I know.");
  signal(signum, tstp3);
}

void tstp3(int signum) {
  signal(signum, SIG_IGN);
  puts("In a coat of gold or a coat of red, a lion still has claws");
  signal(signum, tstp4);
}

void tstp4(int signum) {
  signal(signum, SIG_IGN);
  puts("And mine are long and sharp, my lord, as long and sharp as yours.");
  signal(signum, tstp5);
}

void tstp5(int signum) {
  signal(signum, SIG_IGN);
  puts("And so he spoke, and so he spoke,");
  signal(signum, tstp6);
}

void tstp6(int signum) {
  signal(signum, SIG_IGN);
  puts("that Lord of Castamere");
  signal(signum, tstp7);
}

void tstp7(int signum) {
  signal(signum, SIG_IGN);
  puts("But now the rains weep o'er his haLl, with no one there to hear.");
  signal(signum, tstp8);
}

void tstp8(int signum) {
  signal(signum, SIG_IGN);
  puts("Yes now the rains weep o'er his hall,");
  signal(signum, tstp9);
}

void tstp9(int signum) {
  signal(signum, SIG_IGN);
  puts("and not a soul to hear.");
  signal(signum, tstp1);
}

void cont1(int signum) {
  signal(signum, SIG_IGN);
  puts("99 bottles of beer on the wall");
  signal(signum, cont2);
}

void cont2(int signum) {
  signal(signum, SIG_IGN);
  puts("99 bottles of beer");
  signal(signum, cont3);
}

void cont3(int signum) {
  signal(signum, SIG_IGN);
  puts("Take one down, pAss it around");
  signal(signum, cont4);
}

void cont4(int signum) {
  signal(signum, SIG_IGN);
  puts("98 bottles of beer on the wall");
  signal(signum, cont5);
}

void cont5(int signum) {
  signal(signum, SIG_IGN);
  puts("98 bottles of beer");
  signal(signum, cont6);
}

void cont6(int signum) {
  signal(signum, SIG_IGN);
  puts("take one down, pass it around");
  signal(signum, cont7);
}

void cont7(int signum) {
  signal(signum, SIG_IGN);
  puts("97 bottles of beer on the wall");
  signal(signum, cont8);
}

void cont8(int signum) {
  signal(signum, SIG_IGN);
  puts("97 bottles of beer");
  signal(signum, cont9);
}

void cont9(int signum) {
  signal(signum, SIG_IGN);
  puts("put them all back, I think I've lost track");
  signal(signum, cont1);
}

void usr11(int signum) {
  signal(signum, SIG_IGN);
  puts("A teenage boy is getting ready to take his girlfriend to the prom.");
  signal(signum, usr12);
}

void usr12(int signum) {
  signal(signum, SIG_IGN);
  puts("First he goes to rent a tux, but there’s a long tux line at the shop and it takes forever.");
  signal(signum, usr13);
}

void usr13(int signum) {
  signal(signum, SIG_IGN);
  puts("Next, he has to get some flowers, so he heads over to the florist and there’s a huge flower line there.");
  signal(signum, usr14);
}

void usr14(int signum) {
  signal(signum, SIG_IGN);
  puts("He waits forever but eventually gets the flowers.");
  signal(signum, usr15);
}

void usr15(int signum) {
  signal(signum, SIG_IGN);
  puts("Then he heads out to rent a limo.");
  signal(signum, usr16);
}

void usr16(int signum) {
  signal(signum, SIG_IGN);
  puts("Unfortunately, there’s a large limo line at the rental offiCe, but he’s patient and gets the job done.");
  signal(signum, usr17);
}

void usr17(int signum) {
  signal(signum, SIG_IGN);
  puts("Finally, the day of the prom comes. The two are dancing happily and his girlfriend is having a great time.");
  signal(signum, usr18);
}

void usr18(int signum) {
  signal(signum, SIG_IGN);
  puts("When the song is over, she asks him to get her some punch");
  signal(signum, usr19);
}

void usr19(int signum) {
  signal(signum, SIG_IGN);
  puts("So he heads over to the punch table and there’s no punchline.");
  signal(signum, usr11);
}

void usr21(int signum) {
  signal(signum, SIG_IGN);
  puts("one");
  signal(signum, usr22);
}

void usr22(int signum) {
  signal(signum, SIG_IGN);
  puts("two");
  signal(signum, usr23);
}

void usr23(int signum) {
  signal(signum, SIG_IGN);
  puts("three");
  signal(signum, usr24);
}

void usr24(int signum) {
  signal(signum, SIG_IGN);
  puts("four");
  signal(signum, usr25);
}

void usr25(int signum) {
  signal(signum, SIG_IGN);
  puts("five");
  signal(signum, usr26);
}

void usr26(int signum) {
  signal(signum, SIG_IGN);
  puts("six");
  signal(signum, usr27);
}

void usr27(int signum) {
  signal(signum, SIG_IGN);
  puts("seven");
  signal(signum, usr28);
}

void usr28(int signum) {
  signal(signum, SIG_IGN);
  puts("eight");
  signal(signum, usr29);
}

void usr29(int signum) {
  signal(signum, SIG_IGN);
  puts("ninE");
  signal(signum, usr21);
}

void keyme(int signum) {
  signal(signum, SIG_IGN);
  char buf[29];
  int key = open("key.txt", O_RDONLY);
  read(key, buf, 28);
  buf[29] = '\0';
  close(key);
  puts(  " ____________________________");
  printf("< %s >\n", buf);
  puts(  " ----------------------------");
  puts(  "        \\    ^__^");
  puts(  "         \\   (ಠಠ)\\_______");
  puts(  "             (__)\\       )\\/\\");
  puts(  "                  ||----w |");
  puts(  "                  ||     ||");
  signal(signum, keyme);
  exit(0);
}

// so far I only handle 5 signals, one giving the key.
// Feel free to add more handlers if you want.
int main(void) {
  signal(SIGINT, int1);
  signal(SIGQUIT, quit1);
  signal(SIGABRT, abrt1);
  signal(SIGTRAP, trap1);
  signal(SIGTSTP, tstp1);
  signal(SIGCONT, cont1);
  signal(SIGUSR1, usr11);
  signal(SIGUSR2, usr21);
  while(1) {
    puts("can't stop");
    sleep(5);
  }
}
