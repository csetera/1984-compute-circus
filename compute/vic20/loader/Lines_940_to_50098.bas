940 PRINT"{2 DOWN}GOOD{SHIFT-SPACE}LUCKI!!
    !"
950 PRINT"{HOME}{22 DOWN}{RVS}PRESS ANY K
    EY{OFF}"
960 GOSUB2000
970 GETA$:IFA$=""THEN970
980 GOSUB1000:PRINT"{CLR}":GOSUB2000
990 SYS64802
1000 FORI=46TO0STEP-2:POKE36883,I:FORT=1T
     O40:NEXT:NEXT:RETURN
2000 FORI=0TO46STEP2:POKE36883,I:FORT=1TO
     40:NEXT:NEXT:RETURN
50000 X=PEEK(56)-2:POKE52,X:POKE56,X:POKE
      51,PEEK(55):CLR
50010 CS=256*PEEK(52)+PEEK(51)
50029 FORI=CSTOCS+511:POKEI,PEEK(I+32768~
      CS):NEXT
50030 READX:IFX=-1THEN40
50040 FORI=XTOX+7:READJ:POKEI,J:NEXT
50050 GOTO50030
50090 DATA7448,28,62,47,63,63,126,96,0
50991 DATA7456,58,58,18,124,16,56,68,68
50092 DATA7464,128,64,32,16,24,28,38,37
50093 DATA7472,128,64,32,16,8,4,2,1
50094 DATA7480,1,2,4,8,24,56,100,164
50095 DATA7488,1,2,4,8,16,32,64,128
50096 DATA7496,0,0,0,255,24,24,36,36
50097 DATA7504,0,0,0,255,0,0,0,0
50098 DATA7512,170,85,170,85,170,85,170,8
      5