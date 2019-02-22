class Solution:    
    
    def numberToWords(self, num: 'int') -> 'str':
        self.count = 0
        self.string = ""
        
        if num == 0:
            return "Zero"
        
        mapping = {
            0 : "",
            1 : "Thousand ",
            2 : "Million ",
            3 : "Billion "
        }
        
        tens = {
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
        
        tenth = {
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
        
        
        def helper(num):
            if num:
                hundred = int(num/100)
                remaining = num%100
                if remaining>=20:
                    self.string = tens[int(remaining/10)] + tenth[remaining%10] + mapping[self.count] + self.string
                    # self.string = tens[remaining/10] + tenth[remaining%10] + mapping[self.count] + self.string
                else:
                    self.string = tenth[remaining] + mapping[self.count] + self.string
        
        
                if hundred:
                    self.string = tenth[hundred]+"Hundred "+self.string
        
        while(num):
            temp = num%1000
            helper(temp)
            num = int(num/1000)
            self.count += 1
            
        return self.string[:-1]
