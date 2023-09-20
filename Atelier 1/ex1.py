def message_imc( imc :float ) -> str:
     if imc<16.5 :
          mesg ="dénutrition ou famine"
         
     elif imc<18.5 :
         mesg ="maigreur"
    
     elif imc<25 :
          mesg ="corpulence normale"
     
     elif imc<30 :
          mesg ="surpoids"
    
     elif imc<35 :
          mesg ="obésite modérée"
         
     elif imc<40 :
          mesg ="obésité sévère"
         
     else :
          mesg = "obésité mrbide"
     return mesg
 
 
def test() :    
 print(message_imc(19))
 print(message_imc(13))
 print(message_imc(-1))
 
test()

