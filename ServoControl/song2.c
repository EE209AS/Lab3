#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<mraa/pwm.h>

void function1(mraa_pwm_context pwm)
{
usleep(100000);
mraa_pwm_write(pwm,0.05f);
usleep(200000);
mraa_pwm_write(pwm,0.1f);
usleep(200000);
return ;
}
void function2(mraa_pwm_context pwm)
{
mraa_pwm_write(pwm,0.1f);
usleep(200000);
mraa_pwm_write(pwm,0.05f);
usleep(200000);
return ;
}
int main()
{

mraa_pwm_context pwm;
pwm= mraa_pwm_init(6);
if(pwm==NULL)
{
fprintf(stderr,"failed");
return 1;
}

mraa_pwm_period_ms(pwm,20);

mraa_pwm_enable(pwm, 1);

while(1){
printf("loop1\n");
function1(pwm);
usleep(500000);
function2(pwm);
}
return 0;
}


