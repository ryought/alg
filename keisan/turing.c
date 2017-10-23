/****************************/
/* Turing Machine Simulator */
/*     by Ryo Kashima       */
/*      January 2009        */
/****************************/

#include <stdio.h>
#include <ctype.h>

#define WAIT 100000000
#define TAPE_SIZE 30
#define HEAD_START_POINT 10
#define COMMAND_SIZE 100
#define BLANK '.'
#define COMMENT '%'
#define TAPE_START '<'
#define TAPE_END '>'
#define COMMAND_START '{'
#define COMMAND_END '}'
#define LEFT 'L'
#define RIGHT 'R'

char next_char(void);
void initialize(void);
int input_success(void);
void action(void);
void display_command(void);
void display_tape(void);
void wait(void);


char tape[TAPE_SIZE];
char state;
int head;
int last_command;
struct command {
  char state;
  char read;
  char write;
  char move;
  char next_state; 
};
struct command command_table[COMMAND_SIZE];


main()
{
  initialize();
  if (input_success()) {
   action();
  }
}


void initialize(void)
{
  int i;

  for (i=0; i<TAPE_SIZE; i++){
    tape[i] = BLANK;
  }
}


int input_success(void)
{
  int i;
  char c;

  c = next_char();
  if (c != COMMAND_START){
    printf("'%c' is wrong. \n", c);
    return(0);
  }

  i = -1;
  while(1) {

    c = next_char();
    if (c == COMMAND_END) {
      break;
    }

    i++;
    if (i == COMMAND_SIZE) {
      printf("There is no '%c'. \n", COMMAND_END);
      return(0);
    }

    command_table[i].state = c;

    c = next_char();
    if (c == COMMAND_END) {
      return(1);
    }
    command_table[i].read = c;

    c = next_char();
    if (c == COMMAND_END) {
      printf("'%c' is wrong. \n", c);
      return(0);
    }
    command_table[i].write = c;

    c = next_char();
    if (c == COMMAND_END) {
      printf("'%c' is wrong. \n", c);
      return(0);
    }
    command_table[i].move = c;

    c = next_char();
    if (c == COMMAND_END) {
      printf("'%c' is wrong. \n", c);
      return(0);
    }
    command_table[i].next_state = c;
  }

  last_command = i;


  c = next_char();
  if (c != TAPE_START){
    printf("'%c' is wrong. \n", c);
    return(0);
  }

  i = HEAD_START_POINT - 1;
  while((c = getchar()) != TAPE_END) {
    i++;
    if (i == TAPE_SIZE) {
      printf("There is no '%c'. \n", TAPE_END);
      return(0);
    }
    if (c == ' ')
      tape[i] = BLANK;
    else
      tape[i] = c;
  }

  return(1);

} /* input_success */



void action(void)
{
  int i, matching;

  display_command();


  state = command_table[0].state;
  head = HEAD_START_POINT;
  while(1) {

    //wait();
    display_tape();

    matching = 0;
    for (i=0; i<=last_command; i++){
      if ((command_table[i].state == state) &&
	  (command_table[i].read == tape[head])){ 
        tape[head] = command_table[i].write;
        if (command_table[i].move == LEFT) {
          head--;
          if (head < 0) {
            printf("Out of tape.\n");
            return;
          }
        }
        if (command_table[i].move == RIGHT) {
          head++;
          if (head >= TAPE_SIZE) {
            printf("Out of tape.\n");
            return;
          }
        }
        state = command_table[i].next_state;
        matching = 1;
        break;
      }
    }
    if (matching == 0) { return; }
  }

} /* action */



void display_tape(void)    
{
  int i;

  printf("%c: ", state);
  for (i=0; i<head; i++)
    printf(" %c", tape[i]);
  printf("[%c]", tape[head]);
  for (i=head+1; i<TAPE_SIZE; i++)
    printf("%c ", tape[i]);
  printf("\n");
}


void display_command(void)
{
  int i;

  printf("\n");
  for (i=0; i<=last_command; i++){
    printf("%c --(%c %c %c)--> %c\n",  
         command_table[i].state,
         command_table[i].read, 
         command_table[i].write, 
         command_table[i].move, 
         command_table[i].next_state);
  }
  printf("\n");
}


char next_char(void)
{
  int c;

  c = getchar();
  while (isspace(c) || (c == COMMENT)) {
    if (c == COMMENT) {
      while ((c = getchar()) != COMMENT){}
    }
    c = getchar();
  }
  return(c);
}


void wait(void)
{
  long i;
  for (i=1; i<=WAIT; i++) {}
}
