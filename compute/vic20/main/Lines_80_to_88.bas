80 FORT=1TO100:NEXT:NEXT:FORI=1T0250:NEXT
82 PRINT"PRESS THE FIRE BUTTON TO PLAY AG
   AIN"
83 PRINT"PUSH THE JOYSTICK DOWN TO END"
84 GOSUB88
85 IFFBTHENRUN
86 IFJ1THENPRINT"{CLR}" :POKE36869,240:END
87 GOTO84
88 POKEDD,127:P=PEEK(P2)AND128:J0=-(P=0):
   POKEDD,255:P=PEEK(P1):FB=-((PAND32)=0)
