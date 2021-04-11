class Budget:
    def __init__(self, food, clothing,transport, entertainment):
        self.food= food
        self.clothing= clothing
        self.transport= transport
        self.entertainment= entertainment
        self.database={'food':food, 'clothing':clothing, 'transport': transport, 'entertainment': entertainment}
    # database={'food':self.food, 'clothing':self.clothing, 'transport':self.transport,'entertainment': self.entertainment}
        
    def deposit(self, fund_for_food, fund_for_clothing, fund_for_transport, fund_for_entertainment):
        # database={'food':self.food, 'clothing':self.clothing, 'transport':self.transport,'entertainment': self.entertainment}
        
        if fund_for_food:
            self.database['food']+= fund_for_food
            print(self.database['food'])
        if fund_for_clothing:
            self.database['clothing']+=fund_for_clothing
            print(self.database['clothing'])
        if fund_for_transport:
            self.database['transport']+=fund_for_transport
            print(self.database['transport'])
        if fund_for_entertainment:
            self.database['entertainment']+=fund_for_entertainment
            print(self.database['entertainment'])
        else:
            pass
        print(self.database)
    def withdraw(self, fund_for_food, fund_for_clothing,fund_for_transport,fund_for_entertainment):
        if fund_for_food:
            print(f"You\'ve just withdrawn {fund_for_food} for food.")
        if fund_for_clothing:
            print(f"You\'ve just withdrawn {fund_for_clothing} for clothing.")
        if fund_for_transport:
           print(f"You\'ve just withdrawn {fund_for_transport} for transport.")
        if fund_for_entertainment:
            print(f"You\'ve just withdrawn {fund_for_entertainment} for entertainment.")
        else:
            pass
    
    def check_balance(self, request):
        for request in self.database.items()
        # if fund_for_food:
        #     self.database['food']-= fund_for_food
        #     print(self.database['food'])
        # if fund_for_clothing:
        #     self.database['clothing']-=fund_for_clothing
        #     print(self.database['clothing'])
        # if fund_for_transport:
        #     self.database['transport']-=fund_for_transport
        #     print(self.database['transport'])
        # if fund_for_entertainment:
        #     self.database['entertainment']-=fund_for_entertainment
        #     print(self.database['entertainment'])
        # else:
        #     pass
        

budget1= Budget(0,0,0,0)


budget1.deposit(2000, 3000,4000, 6000)
budget1.withdraw(3000,4000,670,6900)
budget1.check_balance()

