30 IFZ=7ANDU>7THENZ=0:GOTO31
31 IFPEEK(W)=35THENPOKEW+CL,Z
32 OS=S:S=S+1:IFS>7855THENS=7834
33 POKEOS,32:POKES,43:POKES+CL,0
34 IFJ0THENTP=TP+1:IFTP>16THENTP=16
35 IFJ2THENTP=TP-1:IFTP<0THENTP=0
36 PRINTGP$;TAB(TP);TB$(TT)
37 IFD=-1THEN40
38 IFD=1THEN49
39 GOTO37
40 OP=MP:MP=MP+AO:MC=MP+CL:PM=PEEK(MP)
41 IF(OP-7679)/22=INT((OP-7679)/22)ANDAO=
   23THENMP=MP-22:PM=PEEK(MP):MC=MP+CL
42 IFPM=32THEN48
43 IFPM=35THENGOSUB67:GOTO48
44 IFPM=T(TT)THEN56
45 IFPM=43ORPM=45THENMP=OP:D=1:A0=INT(RND
   (1)*3)+21:GOTO27
46 L=L-1:IFL<=0THEN77
47 GOTO16
