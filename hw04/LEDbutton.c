#include <fcntl.h>
#include <sys/mman.h>
#include <stdio.h>

#define GPIO1_START_ADDR 0x4804C000
#define GPIO1_END_ADDR   0x480d000
#define GPIO1_SIZE (GPIO1_END_ADDR - GPIO1_START_ADDR)

#define GPIO2_START_ADDR 0x481Af000
#define GPIO2_END_ADDR   0X481B0000
#define GPIO2_SIZE (GPIO2_END_ADDR - GPIO2_START_ADDR)

#define GPIO_SETDATAOUT 0x194
#define GPIO_CLEARDATAOUT 0x190
#define USR3 (1<<24)
#define USR2 (1<<23)
#define GPIO_DATAIN 0x138

int main() {

volatile void *gpio_addr;
volatile unsigned int *gpio_setdataout_addr;
volatile unsigned int *gpio_cleardataout_addr;
volatile unsigned int *gpio_datain_addr;

volatile void *gpio_addr2;
volatile unsigned int *gpio_setdataout_addr2;
volatile unsigned int *gpio_cleardataout_addr2;
volatile unsigned int *gpio_datain_addr2;

int fd = open("/dev/mem", O_RDWR);
gpio_addr = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);
gpio_addr2 = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO2_START_ADDR);

gpio_setdataout_addr = gpio_addr + GPIO_SETDATAOUT;
gpio_cleardataout_addr = gpio_addr + GPIO_CLEARDATAOUT;
gpio_datain_addr = gpio_addr + GPIO_DATAIN;

gpio_setdataout_addr2 = gpio_addr + GPIO_SETDATAOUT;
gpio_cleardataout_addr2 = gpio_addr + GPIO_CLEARDATAOUT;
gpio_datain_addr2 = gpio_addr + GPIO_DATAIN;

for (int c = 0; c<1234; c++) {
    
    if ((*gpio_datain_addr2 & (1<<19)) == 0) *gpio_cleardataout_addr = USR3;
    else gpio_cleardataout_addr = USR3;
    
    if ((*gpio_datain_addr2 & (1<<21)) == 0) *gpio_cleardataout_addr = USR2;
    else gpio_cleardataout_addr = USR2;
    
    usleep(12345);
}

munmap ((void *) gpio_addr, GPIO1_SIZE);
munmap ((void *) gpio_addr, GPIO2_SIZE);
close(fd);

}