## copy https://blog.podkalicki.pl/attiny13-dance-lights-with-dft/#comment-186
## testing and add python code to try different value of "N"
## build the c code, save to file twiddle_factors.h
## by xiaolaba, 2018


## copy https://blog.podkalicki.pl/attiny13-dance-lights-with-dft/#comment-186
import math
#N = 6
N = 10  ## try different N value
PI2 = 6.2832
# Calc twiddle factors
W = [math.cos(n*PI2/N) for n in range(N)]
# Convert W to list of integers
I = [int(n * 10) for n in W]
print("Twiddle Factors: {}".format(I))


## my code and attemps to build c code with differnet N value, ie. 10

print ("/* original C code")
print ("#define    N                   (6)")
print ("const int8_t W[N] = {10, 4, -5, -9, -4, 5};")
print ("int16_t samples[N] = {0};")
print ("int16_t re[N];")
print ("*/\r\n")


## same code write to file
with open("twiddle_factors.h", "w", encoding="utf-8") as f:
    print ("""
/* original C code
#define    N                   (6)
const int8_t W[N] = {10, 4, -5, -9, -4, 5};
int16_t samples[N] = {0};
int16_t re[N];
*/
""",file=f )


#with open("output.txt", "w", encoding="utf-8") as f:
    print("""
// 這是輸出到文件的內容。
// python script build the same C code
""",file=f )

    print ("#define\tN\t(" + str(N) +")", file=f )
    
    print ("const int8_t W[N] = {", end='', file=f )     # do not print crlf, remain same line for next print
    
    ## Print list I, using separator (,)
    print(*I, sep =', ', end='', file=f)
    print("};", end='',  file=f)   
    print("""
int16_t samples[N] = {0};
int16_t re[N];
""",file=f )      