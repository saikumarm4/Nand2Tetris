	@shift
	M=0
	
	@R0
	D=M

	@value
	M=D
	
(LOOP)
	@5
	D=A
	
	@shift
	D=D-M
	
	@END
	D;JEQ
	
	@value
	D=M
	
	@value
	M=D+M
	
	@shift
	M=M+1
	
	@LOOP
	0;JMP
	
(END)
	@END
	0;JMP