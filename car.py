class car:
    def __init__(self, engine, year, company, no):
        self.no = no
        self.gear = 'P'
        self.engine = engine
        self.kiloo = 0
        self.brake_pad_health = 100

        if year>=1970:
            self.year = year
        else:
            print('The inputed year is wrong')

        if company == 'Toyota':
            self.company = company
            self.name = 'camry'
            self.speed = 150
            self.initial_speed = 150
        elif company == 'BMW':
            self.name = 'M5'
            self.company = company
            self.speed = 200
            self.initial_speed = 200
        elif company == 'saipa':
            self.name = 'quick'
            self.company = company
            self.speed = 50
            self.initial_speed = 50
        elif company == 'kia':
            self.name='serato'
            self.company = company
            self.speed = 100
            self.initial_speed = 100
        else:
            print('There is not such company')

    def set_kiloo_meter(self, kiloo):
        self.kiloo = kiloo
        self.speed = self.initial_speed - (kiloo/10)
        self.brake_pad_health = 100 - (kiloo/10)
    def set_gear(self, gear):
        if gear == 'P':
            self.gear= 'P'
        elif gear == 'D':
            self.gear = 'D'
        elif gear == 'N':
            self.gear = 'N'
        elif gear == 'R':
            self.gear = 'R'
        else:
            print('Your input is wrong')
    def output(self):
        print('name:' + self.name+ "\ncompany:" + self.company)





