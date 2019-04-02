from Execution.Execution import Execution

class Portfollio:
    def __init__(self,coin_number,principal,data):
        self.coin_number = coin_number
        self.principal = principal
        self.buy_amount = 10000#开单金额
        self.sell_amount = 10000
        self.data = data
        self.trade_sigle = 'None'
        self.position = ( coin_number * self.data.iat[-1,3] ) / ( self.principal + ( coin_number * self.data.iat[-1,3] ))
        self.judge_position = 0.5

    def position_control(self):
        if ((self.data.iat[-1, 10] > 0) and (self.data.iat[-1, 10] > self.data.iat[-1, 11]) and (
                self.judge_position > self.position)):
            self.buy(self.data.iat[-1,3], self.data.iat[-1,1])
        if ((self.data.iat[-1, 11] > 0) and (self.data.iat[-1, 11] > self.data.iat[-1, 10]) and (self.position > 0)):
            self.sell(self.data.iat[-1,3], self.data.iat[-1,1])
        return {'coin_number':self.coin_number,'principal':self.principal,'Price':self.data.iat[-1,3]}

    def buy(self,Price,time):
        sigle = 'buy'
        self.Execution = Execution(sigle,self.buy_amount,self.sell_amount,Price,time,self.principal,self.coin_number)
        result = self.Execution.excu()
        self.coin_number = result['coin_number']
        self.principal = result['principal']
        self.position = (self.coin_number * Price) / (self.principal + (self.coin_number * Price))

    def sell(self,Price,time):
        sigle = 'sell'
        if(self.sell_amount > self.coin_number):
            self.sell_amount = self.coin_number
        self.Execution = Execution(sigle,self.buy_amount,self.sell_amount,Price,time,self.principal,self.coin_number)
        result = self.Execution.excu()
        self.coin_number = result['coin_number']
        self.principal = result['principal']
        self.position = (self.coin_number * Price) / (self.principal + (self.coin_number * Price))