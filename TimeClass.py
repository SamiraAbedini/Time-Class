#===================================================================
#--------------------------------E12--------------------------------
#===================================================================

class Time:
#-------------------------------------------------------------------
#initial value method
    def __init__(self, hour, minute, second):
        self.hour     =   hour
        self.minute   =   minute
        self.second   =   second
        assert hour>=0 , "Hour can't be smaller than 0"
        assert 0<=minute<60 , "Minute can't be smaller than 0 or bigger than 60"
        assert 0<=second<60 , "Second can't be smaller than 0 or bigger than 60"

#-------------------------------------------------------------------
#show_time method
    def show_time(self):
        return str(self.hour) + ':' + str(self.minute) + ':' + str(self.second)


#-------------------------------------------------------------------
#jam method
    def jam(self, other):
        H = self.hour + other.hour
        M = self.minute + other.minute
        S = self.second + other.second
        if S >= 60:
            S -= 60
            M += 1
        if M >= 60:
            M-= 60
            H += 1
        return Time(H,M,S)


#-------------------------------------------------------------------
# str method
    def __str__(self):
        return str(self.hour) + ':' + str(self.minute) + ':' + str(self.second)


#-------------------------------------------------------------------
# represent method
    def __repr__(self):
        return str(self.hour) + ':' + str(self.minute) + ':' + str(self.second)



    

#-------------------------------------------------------------------
#add method
    def __add__(self, other):
        H = self.hour + other.hour
        M = self.minute + other.minute
        S = self.second + other.second
        if S >= 60:
            S -= 60
            M += 1
        if M >= 60:
            M-= 60
            H += 1
        return Time(H,M,S)



#-------------------------------------------------------------------
#sub method
    def __sub__(self,other):
        H = self.hour - other.hour
        M = self.minute - other.minute
        S = self.second - other.second
        if S<0:
            S+=60
            M-=1
        if M<0:
            M+=60
            H-=1
        return Time(H,M,S)




#-------------------------------------------------------------------
# less than (<) 
    def __lt__(self,other):
        H1=self.hour
        H2=other.hour
        M1=self.minute
        M2=other.minute
        S1=self.second
        S2=other.second
        return (H1 < H2) or ((H1==H2) and (M1<M2)) or ((H1==H2)and (M1==M2)and (S1 < S2))
        
        


           
#-------------------------------------------------------------------
#greater than (>)
    def __gt__(self,other):
        H1=self.hour
        H2=other.hour
        M1=self.minute
        M2=other.minute
        S1=self.second
        S2=other.second
        return (H1 > H2) or ((H1==H2) and (M1>M2)) or ((H1==H2)and (M1==M2)and (S1 > S2))



#-------------------------------------------------------------------
#less than or equal to (<=)
    def __le__(self,other):
        H1=self.hour
        H2=other.hour
        M1=self.minute
        M2=other.minute
        S1=self.second
        S2=other.second
        return (H1 <= H2) or ((H1==H2) and (M1<=M2)) or ((H1==H2)and (M1==M2)and (S1 <= S2))



#-------------------------------------------------------------------
#greater than or equal to (>=)
    def __ge__(self,other):
        H1=self.hour
        H2=other.hour
        M1=self.minute
        M2=other.minute
        S1=self.second
        S2=other.second
        return (H1 >= H2) or ((H1==H2) and (M1>=M2)) or ((H1==H2)and (M1==M2)and (S1 >= S2))


        



#-------------------------------------------------------------------
#equality
    def __eq__(self,other):
        return (self.hour)==(other.hour) and (self.minute)==(other.minute) and (self.second) == (other.second)
       



#-------------------------------------------------------------------
#not equal
    def __ne__(self,other):
        return (self.hour)!=(other.hour) and (self.minute)!=(other.minute) and (self.second) != (other.second)
     
        

    
        
        
    
   
        
