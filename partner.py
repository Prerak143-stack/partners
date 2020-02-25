
usr_name = input( "Hi, What's your Name?" )
partner_name = input ( "What is your partner's name?" )
message = ( "Let's see will you be able to sit together" )
usr_row1 = input ( "What is the row number of the " + str ( usr_name ) + "?")
usr_column1 = input ( "What is the column number of the " + str ( usr_name ) + "?" )
partner_row1= input ( "What is the row number of the " + str( partner_name ) + "?" )
partner_column1 = input ( "What is the column number of the " + str( partner_name ) + "?" )
usr_row = int ( usr_row1 )
usr_column = int ( usr_column1 )
partner_row = int ( partner_row1 )
partner_column = int ( partner_column1 )
calculation = float ( int ( usr_row - partner_row )**2 + int ( usr_column - partner_column )**2 )**0.5
print ( float ( calculation ) )
if  calculation >= 3:
  print ( "Instructor has allowed you to sit together" )
else:
  print ( "Sorry, you can't sit together you have to sit with another partner" )  
