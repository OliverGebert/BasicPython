from dataclasses import dataclass


@dataclass
class Purse:
    euro: int
    funfzig: int
    zwanzig: int
    zehn: int

    def total_value(self):
        coins = [self.euro, self.funfzig, self.zwanzig, self.zehn]
        values = [100, 50, 20, 10]
        value = 0
        for index in range(4):
            value += coins[index]*values[index]
        return value

    def showCoins(self):
        return [self.euro, self.funfzig, self.zwanzig, self.zehn]

    def checkCoins(self, coins):
        return self.euro >= int(coins[0]) and self.funfzig >= int(coins[1]) and self.zwanzig >= int(coins[2]) and self.zehn >= int(coins[3])
    
    def addCoins(self, coins):
        self.euro += int(coins[0])
        self.funfzig += int(coins[1])
        self.zwanzig += int(coins[2])
        self.zehn += int(coins[3])
        return True
    
    def useCoins(self,coins):
        self.euro -= int(coins[0])
        self.funfzig -= int(coins[1])
        self.zwanzig -= int(coins[2])
        self.zehn -= int(coins[3])
        return True

    def provideCoinsForValue(self, value):
        coins = [self.euro, self.funfzig, self.zwanzig, self.zehn]
        values = [100, 50, 20, 10]
        change = [0, 0, 0, 0]

        def subsum(index):
            """ provide sum value of all minor coins """
            value = 0
            for i in range(index,4):
                value += coins[i] * values[i]
            # print(f"+ the minor coins have a value of : {value}")
            return value
        
        if self.total_value() >= value:
            remainingValue = value
            for index in range(4):
                while (remainingValue >= values[index] and coins[index] > 0) or (subsum(index+1) < remainingValue and coins[index] > 0):
                    # print(f"coins: {coins[index]}, values: {values[index]}")
                    remainingValue -= values[index]
                    coins[index] -= 1      
                    change[index] += 1      # add coin to change return list
            return change
        else:
            return False

