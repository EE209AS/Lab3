#include <stdlib.h>
#include <stdio.h>
#include <mraa/aio.h>
#include<unistd.h>
#include<mraa/pwm.h>
#include<string.h>
#include <time.h>

void runMotor(mraa_pwm_context pwm,int potValue);
int
main(int argc, char* argv[])
{
    char* ptr = argv[1];
    int fd = atoi(ptr);
    time_t start,stop;
    time(&start);
    mraa_aio_context adc_a0;
    uint16_t adc_value = 0;
    adc_a0 = mraa_aio_init(0);

    if (adc_a0 == NULL) {
    return 1;
    }


        mraa_pwm_context pwm;
        pwm= mraa_pwm_init(6);
        if(pwm==NULL)
        {
        fprintf(stderr,"failed");
        return 1;
        }

        mraa_pwm_period_ms(pwm,20);

        mraa_pwm_enable(pwm, 1);
        fd = open("test.txt", O_WRONLY);
        dup2(fd,5);

    while(1) {
        char* buf = (char*)calloc(100,sizeof(char));
        adc_value = mraa_aio_read(adc_a0);
        time(&stop);
        sprintf(buf, "%d\t%f\n",adc_value,difftime(stop,start));

        int nbytes=strlen(buf);

       int nbytes=strlen(buf);
        printf("%d\n",nbytes);
        write(fd, buf, nbytes);
        printf("%d\n",adc_value);
        free(buf);
        if (adc_value>300)
                runMotor(pwm,adc_value);
    }
        close(fd);

    mraa_aio_close(adc_a0);
    return MRAA_SUCCESS;
}

void runMotor(mraa_pwm_context pwm,int potValue){
usleep(1000*potValue);
mraa_pwm_write(pwm,0.05f);
usleep(2000*potValue);
mraa_pwm_write(pwm,0.1f);
usleep(200000);
return ;
}


