from datastore import Datastore 
from mainmenu import Mainmenu

datastore = Datastore()
main_menu=Mainmenu()

main_menu.display_main_menu(datastore)
