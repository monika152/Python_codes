# import all function(s) and variables(s) locally
import wbsweiterbildung

wbsweiterbildung.weiterbildung_anmeldung()

print(wbsweiterbildung.first_name) # Thomas
print(wbsweiterbildung.last_name) # Meier

wbsweiterbildung.weiterbildung_zertifikat()



print(wbsweiterbildung.first_name) # Thomas

# Local variables (new variables)
first_name = "Sara"
last_name = "Möller"
print(first_name)
print(last_name)

print(wbsweiterbildung.last_name) #Meier

wbsweiterbildung.last_name = "Meyer"

print(wbsweiterbildung.last_name) # Mayer