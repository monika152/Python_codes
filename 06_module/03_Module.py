#1. Variant: import the whole module
import wbsweiterbildung

wbsweiterbildung.weiterbildung_anmeldung()
wbsweiterbildung.weiterbildung_abbuchung()
print()
###########################
#2. Variante : import the whole module with alias (nickname)
import wbsweiterbildung as wbs

wbsweiterbildung.weiterbildung_anmeldung()
wbsweiterbildung.weiterbildung_abbuchung()
print()
###########################
#3. Variante :import specific function(s)---> we call the function directly
from wbsweiterbildung import weiterbildung_anmeldung
from wbsweiterbildung import weiterbildung_abbuchung , weiterbildung_zertifikat # several with comma

weiterbildung_anmeldung() # without module name
weiterbildung_zertifikat()
print()
##################################
#4. Variant: import speific function(s) with alias (nickname)
from wbsweiterbildung import weiterbildung_abbuchung as abb, weiterbildung_zertifikat as zert

abb() # weiterbildung_abbuchung()
zert() #weiterbildung_zertifikat()
print()
#####################################
#5.Variant: import all functions and call them directly
from wbsweiterbildung import *

weiterbildung_zertifikat()
weiterbildung_abbuchung()
weiterbildung_anmeldung()
