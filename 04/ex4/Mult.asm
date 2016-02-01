	@shift
	M=0
	
    @shiftval
	M=1
	
	@R2
	M=0
	
(AMAIN)
	@15
	D=A
	
	@shift
	D=D-M
	
	@END
	D;JEQ
	
	@shiftval
	D=M
	
	@R1
	D=D&M
	
	@shiftval
	D=D-M
	
	@SHIFT
	D;JEQ
	
	@value 
	M=0

(RETURN)	
	@value
	D=M
	
	@R2	
	M=D+M
	
	@shiftval
	D=M
	
	@shiftval
	M=D+M
	
	@shift
	M=M+1
	
	@AMAIN
	0;JMP

(SHIFT)
	@shiftl
	M=0
	
	@R0
	D=M

	@value
	M=D
	
(LOOP)
	@shift
	D=M
	
	@shiftl
	D=D-M
	
	@RETURN
	D;JEQ
	
	@value
	D=M
	
	@value
	M=D+M
	
	@shiftl
	M=M+1
	
	@LOOP
	0;JMP
	
(END)
	@END
	0;JMP
	
	
	

// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.