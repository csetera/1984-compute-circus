335 IF((OP-1023)/40=INT((OP-1023)/40))AND
    AO=41THENMP=MP-40:PM=PEEK(MP):MC=MP+S
    O
340 IFPM=32THEN406
350 IFPM=35THENGOSUB560:GOTO406
370 IFPM=T(TT)THEN460
380 IFPM=430RPM=45THENMP=OP:D=1:AO=INT(RN
    D(1)*3)+39:G0TO240
400 L=L-1:IFL<=0THEN630
404 GOTO150
406 POKEOP,32:POKEMP,36:POKEMC,0:GOT0240
410 OP=MP:MP=MP-AO:MC=MP+SO:PM=PEEK(MP)
415 IF((OP-1024)/40=INT((OP-1024)/40))AND
    AO=41THENMP=MP+40:PM=PEEK(MP):MC=MP+S
    O
420 IFPM=32THEN450
430 IFPM=35THEND=-1:GOSUB560:GOT0450
435 IFPM=45THENPOKEOP,32:MP=MP-AO:MC=MP+S
    O
440 IFPM=43THENMP=OP:D=-1:AO=INT(RND(1)*3
    )+39:GOTO240
450 POKEOP,32:POKEMP,36:POKEMC,0:GOTO240
460 SC=SC+5:POKEOP,32
480 POKESO+1,10:POKESO+4,33
490 POKE251,TC:SYS49152