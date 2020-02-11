

def main(action_type,input_string):
#   if isinstance(action_type, int) is False:
#     raise('invalid action type')
#   elif action_type != 1 or 2:
#     raise('action out of range')
  if action_type == 1 and check(input_string)[0] == True:
    print(check(input_string)[1])

  else:
	  return ""
	  
def check(string):
  statue = False
  l = len(string) 
  for i in range(l-1):
    for j in range(l):
      if destroy(string[i], string[i+j]) == True:
        string = string.replace(string[i], '')
        string = string.replace(string[i+j], '')
        statue = True

  return [statue, string]

def destroy(char1, char2):
  if ( char1.isupper() == True and char2.islower() == True ) or (char1.isupper() == False and char2.islower() == False):
    if char1.lower() == char2.lower():
        return True
  else:
    return False

main(1, "FADdfs")
      
  


