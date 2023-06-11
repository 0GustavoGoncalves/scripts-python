class Category:
    ledger = list()
    balance = 0
    category = ''
    def __init__(self, category):
        self.category = category
        self.ledger = list()
    def __repr__(self):
        return_string = ''
        for x in range((30-len(self.category))//2):
            return_string += '*'
        return_string += self.category
        for x in range((30-len(self.category))//2):
            return_string += '*'
        return_string += '\n'
        for item in self.ledger:
            amount = f'{item["amount"]:.2f}'
            if len(item['description']) <= 23: 
                description = item['description']
            else:
                description = item['description'][0:23]
            spaces = ' '* (30-len(description)-len(str(amount)))
            return_string += f'{description}{spaces}{amount}\n'
        return_string += f'Total: {self.balance}'
        return return_string
    def deposit(self, amount, description = ''):
        self.ledger.append({'amount':amount,'description':description})
        self.balance += amount     
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount':-amount,'description':description})
            self.balance -= amount
            return True
        else:
            return False
    def get_balance(self):
        return self.balance
    def transfer (self, amount, budget):
        if self.check_funds(amount):
            local_description = f'Transfer to {budget.category}'
            destination_description = f'Transfer from {self.category}'
            self.withdraw(amount, local_description)
            budget.deposit(amount, destination_description)
            return True
        else: return False
    def check_funds(self, amount):
        return True if amount <= self.balance else False

def create_spend_chart(categories):
    records = dict()
    total = 0
    for each in categories:
        for item in each.ledger:
            if item['amount'] < 0:
                records[each.category] = records.get(each.category, 0) + item['amount']
                total += item['amount']
    for key, value in records.items():
        records[key] = value/total * 100 
    return_string = 'Percentage spent by category\n'
    for x in range(100, -1, -10):
        return_string += f'{x:>3}|'
        for value in records.values():
            return_string += ' '
            if value >= x:
                return_string += 'o'
            else:
                return_string += ' '
            return_string += ' '
        return_string += ' \n'
    labels = records.keys()
    return_string += (4 * ' ')+('-' * ((len(labels))*3+1)) + '\n'
    greater_len = 0
    for item in labels:
        if len(item) > greater_len:
            greater_len = len(item)
    count = 0
    while (greater_len)  > count:
        return_string += 4 * ' '
        for key in labels:
            return_string += ' '
            try:
                return_string += key[count]
            except:
                return_string += ' '
            return_string += ' '
        count +=1 
        return_string += ' \n' if ((greater_len)  > count) else ' '
    return return_string