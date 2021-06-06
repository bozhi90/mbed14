#include"mbed.h"

BufferedSerial pc(USBTX,USBRX); //tx,rx
BufferedSerial uart(D1,D0); //tx,rx

int main(){
   printf("111111\n");
   uart.set_baud(9600);
   while(1){
      if(uart.readable()){
         char recv[1];
         uart.read(recv, sizeof(recv));
         //printf("%c\n", recv);
         pc.write(recv, sizeof(recv));
      }
   }
}