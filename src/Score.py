class Game_Score:
    
    def __init__(self, scorecard):
        self.scorecard = list(scorecard)
        self.contador_tiradas = 0
        self.strike = 'X'
        self.spare = '/'
        self.pin_null = '-'
        self.total_pins = 10
        self.frame = 0
        self.total_points = 0

    def strike_score(self):
        suma = 0
        if self.scorecard[self.contador_tiradas+1] == self.pin_null:
            suma += 0
        elif self.scorecard[self.contador_tiradas+2] == self.pin_null:
            suma += 0
        elif self.scorecard[self.contador_tiradas+1] == self.strike:
            suma += self.total_pins * 2 + int(self.scorecard[self.contador_tiradas+2])
        elif self.scorecard[self.contador_tiradas+2] == self.spare:
            suma += self.total_pins * 2
        else:
            suma += self.total_pins + int(self.scorecard[self.contador_tiradas+1]) + int(self.scorecard[self.contador_tiradas+2])
        self.total_points += suma

    def spare_score(self):
        suma = 0
        if self.scorecard[self.contador_tiradas+1] == self.pin_null:
            suma += 0
        elif self.scorecard[self.contador_tiradas+1] == self.strike:
            self.total_pins * 2 - int(self.scorecard[self.contador_tiradas-1])
        else:
            suma += (self.total_pins - int(self.scorecard[self.contador_tiradas-1])) + int(self.scorecard[self.contador_tiradas+1])
        self.total_points += suma

    def tenth_score(self):
        suma = 0
        last_frame = self.scorecard[self.contador_tiradas: ]
        for throw in last_frame:
            if throw == self.pin_null:
                suma += 0
            elif len(last_frame) == 2:
                suma += int(throw)
            else:
                if throw == self.strike:
                    suma += self.total_pins
                elif throw == self.spare:
                    suma += self.total_pins - last_frame[last_frame.find(self.spare)-1]        
        self.total_points += suma

    def Total_Score(self):
        for throw in self.scorecard:
            if self.frame != 9:
                if throw == self.pin_null:
                    self.contador_tiradas += 1
                    self.frame += 0.5
                elif throw.isdigit():
                    self.total_points += int(throw)
                    self.contador_tiradas += 1
                    self.frame += 0.5
                elif throw == self.strike:
                    self.strike_score()
                    self.contador_tiradas += 1
                    self.frame += 1
                elif throw == self.spare:
                    self.spare_score()
                    self.frame += 0.5
            else: 
                self.tenth_score()
                break
        return self.total_points
    
## assert 60 == Game_Score('12345123451234512345').Total_Score()
# #assert 300 == Game_Score('XXXXXXXXXXXX').Total_Score()
##assert 90 == Game_Score('9-9-9-9-9-9-9-9-9-9-').Total_Score()
# assert 150 == Game_Score('5/5/5/5/5/5/5/5/5/5/5').Total_Score()
# assert 133 == Game_Score('8/9-44729-XX8-359/7').Total_Score()
# assert 20 == Game_Score('11111111111111111111').Total_Score()
# assert 122 == Game_Score('8-7-539/9/X8-513/9-').Total_Score()
# assert 175 == Game_Score('X5/X5/XX5/--5/X5/').Total_Score()
# assert 149 == Game_Score('8/549-XX5/53639/9/X').Total_Score()