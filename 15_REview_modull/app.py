from anmeldung import*
from registerung import*
from bestätigung import*



print("willkommen bei WBS")
print(" ~~~~~~~~~~~~~~~~~~~~~")



# Anmeldunsgphase
name, plz , weiterbildung = get_user_information

# Registerunsgphase
confirmation = save_data_to_db(name,plz,weiterbildung)

# Bestätungphase
if confirmation == True:
    send_email_to_tn(name,plz,weiterbildung)
else:
    print("The data is not saved correctly in DB !")
