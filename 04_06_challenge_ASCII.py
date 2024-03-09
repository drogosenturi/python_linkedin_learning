def encodeString(stringVal):
    tuplelist = [] # blank list
    lengthchar = 0 # start with 0 length
    prevchar = None # establish prevchar variable
    # at each position of input string, add one to length
    ## as long as the prevchar is the same, keep looping and adding length
    # once a new character is prevchar, split the string at position i
    ## append the tuple list with prevchar and length
    ## reset length to 0
    ## set prevchar to new char at position i
    ## return the tuple list
    for i in stringVal:
        lengthchar = lengthchar + 1
        if i != prevchar and prevchar != None:
            stringVal.split(i)
            tuplelist.append((prevchar,lengthchar))
            lengthchar = 0
        prevchar = i
    return tuplelist


def decodeString(encodedList):
    decoded = ''
    ## unpack the tuples at each position of input into a and b
    ## multiply a by b and add to end of 'decoded' string
    for i in encodedList:
        a, b = i
        decoded = decoded + (a * b)
    # return the final decoded string
    return decoded

art = '''

                                                                                
                                                                                
                               %%%%%%%%%%%%%%%%%%%                              
                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                       
                    %%%%%%%%                         %%%%%%%%                   
                %%%%%%%                                   %%%%%%                
              %%%%%%                                         %%%%%%             
           %%%%%%                                               %%%%%           
          %%%%%                                                   %%%%%         
        %%%%%                                                       %%%%%       
       %%%%                 %%%%%              %%%%%                  %%%%      
      %%%%                 %%%%%%%            %%%%%%%                  %%%%     
     %%%%                  %%%%%%%            %%%%%%%                   %%%%    
    %%%%                   %%%%%%%            %%%%%%%                    %%%%   
    %%%%                    %%%%%              %%%%%                     %%%%   
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                      %%%%        %%%%   
    %%%%       %%%%%%                                        %%%%%       %%%%   
    %%%%         %%%%                                       %%%%        %%%%    
     %%%%         %%%%                                     %%%%         %%%%    
      %%%%         %%%%%                                  %%%%         %%%%     
       %%%%%         %%%%%                             %%%%%         %%%%%      
        %%%%%          %%%%%%                        %%%%%          %%%%        
          %%%%%           %%%%%%%               %%%%%%%           %%%%%         
            %%%%%             %%%%%%%%%%%%%%%%%%%%%             %%%%%           
              %%%%%%%                                        %%%%%              
                 %%%%%%%                                 %%%%%%%                
                     %%%%%%%%%                     %%%%%%%%%                    
                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%                         
                                   %%%%%%%%%%%%                                 
                                                                                
                                                                                 

'''

encodedString = encodeString(art)
encodedString

decodeString(encodedString)
decoded = decodeString(encodedString)
decoded
print(decoded)
## TESTING
len(decoded)
a,b = decodeList(encodedString[0])
a
b
c,d = decodeList(encodedString[6])
c
d
c*d
e = c*d
f = a*b
print(e)
print(f)

encodeString(art)