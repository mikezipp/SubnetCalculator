import time

#Checks how many hosts can exist for a given subnet mask

#Init some lists
KEY_LIST = []
VALUE_LIST = []

#Calculate subnet masks
def create_keys():
   key = 1
   while key <= 32:
      KEY_LIST.append(key)
      key = key + 1
   KEY_LIST.reverse()
create_keys()

#Calculate hosts
def create_values():
   bits = 1
   while bits < 3000000000:
      VALUE_LIST.append(bits)
      bits = bits * 2
create_values()

#Zip list into dictionary
DYNAMIC_DICT = dict(zip(KEY_LIST, VALUE_LIST))


#Searches dictionary, prints user options
def search_dictionary(keyvar):
   for key, value in DYNAMIC_DICT.items():
      if int(keyvar) == key:
         print "\nThere are %s bits on a CIDR of /%s" % (value, keyvar)
         if keyvar < 31:
            hosts_on_subnet = value - 2
            print "You can use %s hosts on this subnet" % (hosts_on_subnet)
         elif keyvar == 31:
            hosts_on_subnet = value
            print "You can use %s hosts on this subnet if this is a point to point network" % (hosts_on_subnet)
         elif keyvar == 32:
            print "There is no room for hosts on this subnet"

#User interface
def main():
   keyvar = int(raw_input("What is the CIDR netmask?\n> /"))
   if type(keyvar) == int and int(keyvar) <= 32:
      print "You have selected /%s" % (keyvar)
      print "\nCalculating results"
      time.sleep(1)
      search_dictionary(keyvar)

   else:
      print "Invalid input, please try again"
        

main()


