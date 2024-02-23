#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>


/**
 * infinite_while - Creates an infinite loop to keep the parent process running
 * Return: returns 0
 */
int infinite_while(void)
{
while (1)
{
sleep(1);
}
return (0);
}

/**
 * main - Creates 5 zombie processes
 * Return: returns 0
 */
int main(void)
{
pid_t zombie_pid;
int numb;

for (numb = 0; numb < 5; numb++)
{
zombie_pid = fork();
if (zombie_pid == -1)
{
return (1);
}
if (zombie_pid == 0)
exit(0);
else
printf("Zombie process created, PID: %d\n", zombie_pid);
}
infinite_while();
return (0);
}

