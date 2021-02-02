#include <msp430g2553.h>

int main (void){
  // Stop the watchdog timer                                                    
  WDTCTL = WDTPW + WDTHOLD;

  // Initialize GPIO pins for LED operation                                     
  P1OUT |= BIT0; // Set red LED on P1.0 to HIGH
  P1DIR |= BIT0; // Set the direction of P1.0 to OUTPUT

}