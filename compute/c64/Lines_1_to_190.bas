1 GOTO800
2 POKE53280,6:POKE53281,1
5 S=1304:EX=1:L=3:SC=0:5O=54272
10 POKESO+24,15:POKESO+5,17:POKESO+6,241:
   POKESO,100
20 TC=27:POKE251,112:POKE831,0:POKE832,0:
   POKE829,20
30 TB(1)=112
40 TB(2)=197
50 SS$="{19 RIGHT}{3 SPACES}{DOWN}
   {4 LEFT}{5 SPACES}{DOWN}{3 LEFT} "
60 SC$="{19 RIGHT}{GRN}###{DOWN}{4 LEFT)
   {BLU}#####{DOWN}{3 LEFT}$"
70 POKE53272,(PEEK(53272)AND240)+12
80 T(1)=38:T(2)=40
90 PRINT"{CLR}{2 DOWN}{RED}##############
   ##########################";
91 PRINT"{GRN}###################
   {3 SPACES}##################";
92 PRINT"{BLU}##################
   {5 SPACES}#################";
100 FORI=16TOlSTEP-1
110 PRINT"{HOME}{3 DOWN}";:FORT=1TOI:PRIN
    T"{DOWN}";:NEXT:PRINTSC$
120 FORY=1TO75:NEXT
130 PRINT"{HOME}{3 DOWN}";:FORT=1TOI:PRIN
    T"{DOWN}";:NEXT:PRINTSS$
140 NEXT
150 PRINT"{CLR}{2 DOWN}{RED}#############
    ###########################";
151 PRINT"{GRN}##########################
    ##############";
152 PRINT"{BLU}##########################
    ##############"
160 PRINT"{HOME}{DOWN}+++++++++++++++++++
    +++++++++++++++++++++"
170 PRINT"{HOME}{23 DOWN},,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,";
180 TT=1:D=-1:A0=40:MP=1244:MC=55516:TP=1
    9:BA=121:Z=0:POKE834,TP
185 W=INT(RND(1)*39)+1104
190 POKE251,TB(TT):SYS49152
