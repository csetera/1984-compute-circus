500 POKESO+4,32:IFTT=1THENMP=1787+TP:MC=M
    P+SO
510 IFTT=2THENMP=1785+TP:MC=MP+SO
520 TT=TT+1:IFTT>2THENTT=1
530 D=1
540 POKE251,TB(TT):SYS49152
550 AO=INT(RND(1)*3)+39
555 PRINT"{HOME}{6 SPACES}SCORE=";SC:PRIN
    T"{HOME}{25 RIGHT}LIFE=";L:GOT0240
560 POKESO+1,10:POKESO+4,129:FORI=1TO10:N
    EXT:POKESO+4,128
563 IFMP=WANDC=0THENL=L-1:GOTO150
566 IFMP=WANDC=7THENSC=SC+250:GOTO600
570 IFMP>1103ANDMP<1144THENSC=SC+100
580 IFMP>1143ANDMP<1184THENSC=SC+75
590 IFMP>1183ANDMP<1224THENSC=SC+50
609 IFSC>EX*2000THENL=L+1:EX=EX+1
605 BA=BA-1:IFBA=1THEN150
610 AO=INT(RND(1)*3)+39
620 PRINT"{HOME}{6 SPACES}SCORE=";SC:PRIN
    T"{HOME}{25 RIGHT}LIFE=";L:RETURN
630 G$=" G A M E{3 SPACES}O V E R"
640 FORI=2TO19STEP2
650 PRINT"{HOME}{9 DOWN}";TAB(I*2-1);MID$
    (G$,I,1)
