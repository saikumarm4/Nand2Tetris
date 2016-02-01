// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// Put your code here.
	
	@8191
	D=A
	
	@SCRLEN
	M=D

(LOOP)
	@KBD
	D=M
	
	@BSCRLOOP
	D;JGT
	
	@WSCRLOOP
	0;JMP
	
(BSCRLOOP)
	@i
	M=0
	
(BLACKL)
	
	@SCREEN
	D=A
	
	@i
	A=D+M
	M=-1
	
	@i
	M=M+1
	
	@SCRLEN
	D=M
	
	@i
	D=D-M
	
	@BLACKL
	D;JGT
	
	@LOOP
	0;JMP
	

(WSCRLOOP)
	@i
	M=0
	
(WBLACKL)
	@SCREEN
	D=A
	
	@i
	A=D+M
	M=0
	
	@i
	M=M+1
	
	@SCRLEN
	D=M
	
	@i
	D=D-M
	
	@WBLACKL
	D;JGT
	
	@LOOP
	0;JMP