#include <fcntl.h>
#include <sys/mman.h>
#include <stdio.h>

#define GPIO1_START_ADDR 0x4804C000
#define GPIO1_END_ADDR   0x4804e000
#define GPIO1_SIZE (GPIO1_END_ADDR - GPIO1_START_ADDR)

#define GPIO3_START_ADDR 0x481AE000
#define GPIO3_END_ADDR   0x481B0000
#define GPIO3_SIZE (GPIO3_END_ADDR - GPIO3_START_ADDR)

#define GPIO_SETDATAOUT 0x194
#define GPIO_CLEARDATAOUT 0x190
#define P9_12 (1<<23)
#define P9_25 (1<<24)
#define GPIO_DATAIN 0x138

int main(){
    volatile void *gpio_addr1;
    volatile unsigned int *gpio_setdataout_addr1;
    volatile unsigned int *gpio_cleardataout_addr1;
    volatile unsigned int *gpio_datain_addr1;
    
    volatile void *gpio_addr2;
    volatile unsigned int *gpio_setdataout_addr2;
    volatile unsigned int *gpio_cleardataout_addr2;
    volatile unsigned int *gpio_datain_addr2;
    
    int fd = open("/dev/mem", O_RDWR);
    gpio_addr1 = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);
    gpio_addr2 = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO3_START_ADDR);
    
    gpio_setdataout_addr1   = gpio_addr1 + GPIO_SETDATAOUT;
    gpio_cleardataout_addr1 = gpio_addr1 + GPIO_CLEARDATAOUT;
    gpio_datain_addr1 = gpio_addr1 + GPIO_DATAIN;
    
    gpio_setdataout_addr2   = gpio_addr2 + GPIO_SETDATAOUT;
    gpio_cleardataout_addr2 = gpio_addr2 + GPIO_CLEARDATAOUT;
    gpio_datain_addr2 = gpio_addr2 + GPIO_DATAIN;
    
    unsigned int period = 100000;
    
    while(1)
    {
        *gpio_setdataout_addr1 = P9_12;
        usleep(period/2);
        *gpio_cleardataout_addr1 = P9_12;
        usleep(period/2);
    }
    
    //clear what we have done
    munmap ((void *) gpio_addr1, GPIO1_SIZE);
    munmap ((void *) gpio_addr1, GPIO3_SIZE);
    close(fd);
}