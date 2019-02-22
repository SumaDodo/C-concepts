class Solution:    
    def numberToWords(self, num: 'int') -> 'str':
        if num==0:
            return "Zero"
        
        mapping = {
            0 : "",
            1 : "Thousand ",
            2 : "Million ",
            3 : "Billion "
        }
        decade = {
                0 : "",
                2 : "Twenty ",
                3 : "Thirty ",
                4 : "Forty ",
                5 : "Fifty ",
                6 : "Sixty ",
                7 : "Seventy ",
                8 : "Eighty ",
                9 : "Ninety "
            }


        l20 = {
              0 : "",
            1 : "One ",
            2 : "Two ",
            3 : "Three ",
            4 : "Four ",
            5 : "Five ",
            6 : "Six ",
            7 : "Seven ",
            8 : "Eight ",
            9 : "Nine ",
            10 : "Ten ",
            11 : "Eleven ",
            12 : "Twelve ",
            13 : "Thirteen ",
            14 : "Fourteen ",
            15 : "Fifteen ",
            16 : "Sixteen ",
            17 : "Seventeen ",
            18 : "Eighteen ",
            19 : "Nineteen "
        }
        
        self.res = ""
        self.cnt = 0
        
        def helper(num):
            if num:
                hund = int(num/100)
                last2 = num%100

                if last2>=20:
                    # print(last2/10," ", last2%10)
                    self.res = decade[int(last2/10)] + l20[last2%10] + mapping[self.cnt] + self.res
                else:
                    self.res = l20[last2] + mapping[self.cnt] + self.res

                if hund:
                    self.res = l20[hund]+"Hundred " + self.res
            
   
        while num:
            temp=num%1000
            helper(temp)
            num=int(num/1000)
            self.cnt+=1
        
        return self.res[:-1]
