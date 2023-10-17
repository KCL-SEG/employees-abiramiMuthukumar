"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, monthly_salary=-1, hourly_salary=-1, hours_worked=-1,
                 commission='', commission_per_contract=-1, contracts_landed=-1,
                 bonus_commission=-1):
        self.name = name
        self.contract = contract
        self.total_pay = 0
        self.output_string = self.name + ' works on a '
        self.monthly_salary = monthly_salary
        self.hourly_salary = hourly_salary
        self.hours_worked = hours_worked
        self.commission = commission
        self.commission_per_contract = commission_per_contract
        self.contracts_landed = contracts_landed
        self.bonus_commission = bonus_commission

    def get_pay(self):
        self.total_pay = 0
        self.output_string = self.name + ' works on a '

        if self.contract == 'salary':
            self.total_pay += self.get_salary_contract_pay()
        elif self.contract == 'hourly':
            self.total_pay += self.get_hourly_contract_pay()
        else:
            print("contract must be salary or hourly")

        self.total_pay += self.get_commission_pay()

        return self.total_pay

    def get_salary_contract_pay(self):
        self.output_string = self.output_string + 'monthly salary of ' + str(self.monthly_salary) + ''
        return self.monthly_salary

    def get_hourly_contract_pay(self):
        self.output_string = self.output_string + 'contract of ' + str(self.hours_worked) + ' hours at ' + str(self.hourly_salary) + '/hour'
        return self.hourly_salary * self.hours_worked

    def get_commission_pay(self):
        if self.commission:
            if self.commission == 'contract':
                self.output_string = self.output_string + ' and receives a commission for ' + str(
                    self.contracts_landed) + ' contract(s) at ' + str(self.commission_per_contract) + '/contract'
                return self.contracts_landed * self.commission_per_contract
            elif self.commission == 'bonus':
                self.output_string = self.output_string + ' and receives a bonus commission of ' + str(self.bonus_commission)
                return self.bonus_commission
            else:
                print("commission must be contract or bonus")

        return 0

    def __str__(self):
        self.get_pay()
        self.output_string = self.output_string + '. Their total pay is ' + str(self.total_pay) + '.'
        return self.output_string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'salary', monthly_salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'hourly', hourly_salary=25, hours_worked=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'salary', monthly_salary=3000, commission='contract', commission_per_contract=200, contracts_landed=4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'hourly', hourly_salary=25, hours_worked=150, commission='contract', commission_per_contract=220, contracts_landed=3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'salary', monthly_salary=2000, commission='bonus', bonus_commission=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 'hourly', hourly_salary=30, hours_worked=120, commission='bonus', bonus_commission=600)