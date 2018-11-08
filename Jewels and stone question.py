You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  

Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".




def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        #J = list(dict(J).value)
        count = 0
        if(len(J)<= 50 and len(S)<=50):
            for characters in S:
                if characters.isalpha():
                    if characters in J:
                        count += 1
        return count




###### this second method is more efficient than the first becauses it uses dictionary for look up

def numJewelsInStones(self, J, S):
	summy = 0
       
	count = collections.Counter()
        
	if(J.isalpha() and S.isalpha()):
            
		for x in S:
                
		count[x] += 1
           
	S = dict(count)
           
	if(len(J)<= 50 and len(S)<=50):
                
		for x in S:
                    
			if x in J:
                        
				summy += S.get(x)
                
	return summy