# print_letters function taken from https://gist.github.com/python4d

letters = {"a": ["####", "#  #", "####", "#  #", "#  #"], "b": ["###", "# #", "###", "# #", "###"],
           "c": ["###", "#", "#", "#", "###"], "d": ["##", "# #", "# #", "# #", "##"],
           "e": ["###", "#", "###", "#", "###"], "f": ["###", "#", "###", "#", "#"],
           "g": ["###", "# #", "###", "  #", "###"], "h": ["# #", "# #", "###", "# #", "# #"],
           "i": ["###", " #", " #", " #", "###"], "j": ["###", " #", " #", " #", "##"],
           "k": ["# #", "##", "#", "##", "# #"], "l": ["#", "#", "#", "#", "###"],
           "m": ["# #", "###", "###", "# #", "# #"], "n": ["###", "# #", "# #", "# #", "# #"],
           "o": ["###", "# #", "# #", "# #", "###"], "p": ["###", "# #", "###", "#", "#"],
           "q": ["###", "# #", "###", "  #", "  #"], "r": ["###", "# #", "##", "# #", "# #"],
           "s": ["###", "#", "###", "  #", "###"], "t": ["###", " #", " #", " #", " #"],
           "u": ["# #", "# #", "# #", "# #", "###"], "v": ["# #", "# #", "# #", "# #", " #"],
           "w": ["# #", "# #", "# #", "###", "###"], "x": ["# #", " #", " #", " #", "# #"],
           "y": ["# #", "# #", "###", "  #", "###"], "z": ["###", "  #", " #", "#", "###"], " ": [" "],
           "1": [" #", "##", " #", " #", "###"], "2": ["###", "  #", "###", "#", "###"],
           "3": ["###", "  #", "###", "  #", "###"], "4": ["#", "#", "# #", "###", "  #"],
           "5": ["###", "#", "###", "  #", "###"], "6": ["###", "#", "###", "# #", "###"],
           "7": ["###", "  # ", " #", " #", "#"], "8": ["###", "# #", "###", "# #", "###"],
           "9": ["###", "# #", "###", "  #", "###"], "0": ["###", "# #", "# #", "# #", "###"],
           "!": [" # ", " # ", " # ", "   ", " # "], "?": ["###", "  #", " ##", "   ", " # "],
           ".": ["   ", "   ", "   ", "   ", " # "], "]": ["   ", "   ", "   ", "  #", " # "],
           "/": ["  #", "  #", " # ", "# ", "# "], ":": ["   ", " # ", "   ", " # ", "   "],
           "@": ["###", "# #", "## ", "#  ", "###"], "'": [" # ", " # ", "   ", "   ", "   "],
           "#": [" # ", "###", " # ", "###", " # "]}
def print_letters(text, scale=1, espace=2):
    bigletters = []
    for i in text:
        bigletters.append(letters.get(i.lower(), letters[' ']))
    output = [''] * (5 * scale)  # nb de ligne
    for i in range(5):
        for ind, j in enumerate(bigletters):
            temp = ' '
            try:
                temp = j[i]
            except:
                pass
            line = ''
            for z in temp:
                line += z * scale
            line += ' ' * (3 * scale + espace - len(line))
            line = line.replace('#', text[ind].upper())
            output[i * scale] += line
        for bold in range(scale - 1):
            output[i * scale + bold + 1] = output[i * scale]

    return '\n'.join(output)
# hat image taken from https://www.villagehatshop.com/product/top-hats/451139-443902/head-n-home-the-butcher-leather-st
# ove-pipe-top-hat.html
# Want to have a cool ascii image like that top-hat? I recommend using https://www.text-image.com/convert/ascii.html.
# Put the name of your game/program where "NAME" is. Change "3" for scale and "4" for spacing
intro = print_letters('  NAME', 3, 4) + '''

                                            `````.........--::::::::::::///////:-.                      
                             `..-::://++++ooooooooooooooooooooooooosssyyyyyyyyhdmNdo-                   
                      `.::/+syhhhhyyyyyyyyyyyyyyyyhhhhhhhddddddmmmmmmNNNNNNNNmmddmmdy:                  
                   `oydmmdmmmmNNNmmmmNNNNNNNNNNNNNNNNmmNNNNNNNNNNNNNmmNNNNNNNNNmmmmdh:                  
                   -dmmNNNNNNNNNNNmmmmmmmmNNNNNNNmmNNNNNmmmmmmmNmmmmmNNNNNNNNNNNNNmmh`                  
                    ymNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmms                   
                    /mNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmo                   
                    `dNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmmmNNNNNNNNNNNNNNNmdo                   
                     hNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmmmNNNNNNNNNNNNNNNmmo                   
                     smNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmmNNNNNNNNNNNNNNNNmd+                   
                     +mNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmmNNNNNNNNNNNNNNNNmd+                   
                     :mmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmNmmmmmmmmNNNNNNNNNNNNNNNNmd/                   
                     .mmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmmNNNNNNNNNNNNNNNNmmd:                   
                     `dmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmmNNNNNNNNNNNNNNNmmh:                   
                      hmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmNNNNNNNNNNNNNNNNmdh-                   
                      smNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmmNNNNNNNNNNNNNNNNmdh.                   
                      +mNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmNNNNNNNNNNNNNNNNNmdh`                   
                      :mmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmNNNNNNNNNNNNNNmmmmdy                    
                      .dmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmmmmNNNNNNNNNNNNNNmmmds                    
                      .dmNNNNNNNNNNNNNNNNNNNNNNmNNNNNNNNmmmmmmmmmNNNNNNNNNNNNNNNmmds                    
                      `dmNNmNNNNNNNNNNNNNmmmNNmmNNNNNNNNmmmmmmmNNNNNNNNNNNNNNNNNmmds                    
                      `dmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmNNNNNNNNNNNNNNNNNNNNNmmdy                    
                       smNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmdy`                   
                       +mNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmdh`                   
                       -mNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmddh`                   
                     `./mNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmdy                    
                 -ohmNNNmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmNNNNNNNNNNNNNNNNmd+                    
               :hNMMNNNmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmNNNNNNNNNNNNNNNmd:          ..        
             `sNMMNNNmmdNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmmmmmmNNNNNNNNNNNNNNNNNNm-       `/sys.       
            `yNNNNNNmdddNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMMNNNNNN/     -ohddy:        
            yNNNmmmmmmmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMNm/`.+hmmmdy:         
           +NNNmmmmNNNNNMMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMMMNmhmmmmmdy/          
           dMNmmmNNNMMMMMMMMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMMMNNNNNmmdds-           
          .mMNmmNNNMMMMMMMMMMMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMMMNNNNNNmmdy/`            
          .NMNNNNNMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMMMNNNNNNmmdh+.              
          `mMNNNNNMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMMMNNNNNmmds/`                
           yNMNNNNMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMMMNNNNNmmyo-`                  
           :NMMMNMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMNNNNmmds:`                     
            hNMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMNNNNmdy/.                        
            :mMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMNNNmdy+-                           
             +NMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMNNmmh+-`                             
              oNNMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNMMMMMMMMMMNmho-`                                
               +mNMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNMMMMMMMMMMMMNds:`                                   
                :hNNNMMMMMMMMMMMMMMMNNNNNNNNNMMMMMMMMMMMMMMMMNmd+.                                      
                 `odNNNNNNNNNNNNMNNNNNNNNNMMMMMMMMMMMMMMMMNNmy:`                                        
                   .+hmmNNNNNNNNNNNNNNNNNNNMMMMMMMMMNNNNNmdo-                                           
                      -+hmmmNNNNNNNNNNNNNNNNNNNNNNNNmmdy+-                                              
                         `:+ydmmmmmmNNmNmNmmmmmmmdyo/-                                                  
                              `-:/+oosssssso+/:-`                                                       

    /////////////////////////////////////////////////////////////////////////////////////////////////////////////
    ----------------------------------------------Yourname-------------------------------------------------------
    /////////////////////////////////////////////////////////////////////////////////////////////////////////////
     Input 'b' to begin, 'c' for credits, 'r' to return to this menu and 'q' to exit. '''
# You can put your name in the ---- if you want
'''
Want to have another menu option? Just copy this script onto the while loop, only before the "if b" command.
    if response == "o":
        print("o stands for other menu option")        
        response = input("> ")
        if response == "r":
            print("")
        if response == "q":
            a = False
            exit()
        else:
            while response != 'r':
                print("Invalid input")
                response = input("> ")
'''
menu_options = ["b", "c", "r", "q"] # Also, put your new menu option in this list, you'll see why later.
num_of_inputs = 0
a = True
while a:
    print(intro)
    response = input("> ")
    while response == 'r':
        print("You are already in the main menu!")
        response = input("> ")
    if response not in menu_options:
        while response not in menu_options:
            print("Invalid input")
            response = input("> ")
    if response == "c":
        print("\nEnter 'r' to return")# Enter your name, date of publication and stuff like that in the first line
        response = input("> ")
        if response == "r":
            print("")
        if response == "q":
            a = False
            exit()
        else:
            while response != 'r':
                print("Invalid input")
                response = input("> ")

    if response == "q":
        a = False
        exit()
    if response == "b":
            response = input("> ")
            if response == "r":
                print("")
            if response == "q":
                a = False
                exit()
            # Put your program after else:. You can change it to elif or if and delete the stuff I've written there
            else:
                fun_factor = True
                while fun_factor:
                    print(response)
                    response = input("> ")
                    if response == "r":
                        fun_factor = False
                    if response == "q":
                        fun_factor = False
                        exit()
