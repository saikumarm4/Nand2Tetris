# Nand2Tetris

The Repository is an implementation of Nand2Tetris. The objective of the course is to build a Hack Hardware Platform, 
a simple computer - part 1, and develop jack language to build the software hierarchy. The Course is divided into 12 modules.
For each module we have to do a project to be used in the next project, to build the hardware and software hierarchy progressively.

Hardware Layer
1. To build Elementary Gate using Hardware Descriptor Language (specific to Nand2Tetris) 
   The implementation of fundamental Nand Gate is provided
2. To build Computational Gate or (Combinational Gates) Full-adder, half-adder, Incrementer and Arithmatic Logic Unit
3. To build Sequential Gates, Counter, Register, RAM, ROM
   The implementation of D-Flip Flop is given
4. Designing Assembly Language for the Hack Platform
5. Build the Hack computer platform, which will be the top most layer of Hardware Architecture
6. To convert Assembly Language to hardware understandable sequence of bits (1 or 0)

Software Layer
Software Architecture is developed using Jack Language (specific to Nand2Tetris), via the language operating system is developed.
Jack is java like language, which achieves compile onces and run anywhere. Hence, Jack has virtual machine and a front end compiler.
we build the jack language using bottom up method, first we take granted the vm is defined, a program to convert it to assembly
language (7 and 8), syntax and symantics of jack in 9, develop front end compiler for Jack Language in 10 and 11.

7. Virtual Machine I, convert static arithmatic and memory access instruction in VM language to assembly language.
8. Virtual Machine II, conver flow control and function calls in VM language to assembly language.
9. Jack language syntax and symantics
10. Compiler I, to break the source file into tokens and produce an XML with code constructs.
11. Compiler II, from the tokens write the vm code for the source file
12. In the last 3 changes, we took for granted the OS, in chapter 12 we build the os using jack language.
    OS, consists of array, string, sys, output, memory handlers (to be implemented)
  
