# Tiny13_dance_lights_with_dft
copy and learn

### original author  
BSD-3-Clause license  
https://github.com/lpodkalicki/blog/tree/master/avr/attiny13/018_dance_lights_with_dft  
https://blog.podkalicki.pl/attiny13-dance-lights-with-dft/#comment-186  

### my code
follow the license but we did not know what is or try what, just follow.  
add python code dft.py to build twiddle_factors.h  
main.c, include twiddle_factors.h  
dosmake.bat and build_hex.bat for avr firmware build,  output folder /firmware
updates build_hex.bat to uses AVR 8-Bit Toolchain (Windows) 3.7.0   

main.c, changed and snippet, for testing and memo  
```
#include "twiddle_factors.h"	// try differnet N value, by xioalaba 2018
/*
#define	N			(6)
const int8_t W[N] = {10, 4, -5, -9, -4, 5};
int16_t samples[N] = {0};
int16_t re[N];
*/

```
