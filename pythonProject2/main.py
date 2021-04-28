class Tech:
    WorkTime = "3"
    users = "1" \
            ""
    def get_WorkTime(self):
        print(self.WorkTime)

    def get_users(self):
        print(self.users)

class TV(Tech):
    condition = "work"
    price = "50000"
    model = "Sony"

    def start(self):
        print("Телевизор включен")

    def get_condition(self):
        print(self.condition)

    def get_price(self):
        print(self.price)

    def get_model(self):
        print(self.model)

class laptop(Tech):
    CPU = "intel"
    price = "70000"
    model = "Lenovo"

    def get_CPU(self):
        print(self.CPU)

    def get_price(self):
        print(self.price)

    def get_model(self):
        print(self.model)

class monitor(Tech):
    display = "24"
    price = "70000"
    model = "LG"

    def get_display(self):
        print(self.display)

    def get_price(self):
        print(self.price)

    def get_model(self):
        print(self.model)

class microwave(Tech):
    watt = "700"
    price = "5000"
    model = "Hansa"

    def get_watt(self):
        print(self.watt)

    def get_price(self):
        print(self.price)

    def get_model(self):
        print(self.model)

class printer(Tech):
    size = "100"
    price = "20000"
    model = "endever"

    def get_size(self):
        print(self.size)

    def get_price(self):
        print(self.price)

    def get_model(self):
        print(self.model)


class Rabotnik:
    WorkTime = "9"
    name = "Marek"
    salary = "100000"

    def get_salary(self):
        print(self.salary)

    def get_name(self):
        print(self.name)

    def get_WorkTime(self):
        print(self.WorkTime)


class Manager(Rabotnik):
    salary = "50000"
    name = "Abraham"
    age = "27"

    def get_salary(self):
        print(self.salary)

    def get_name(self):
        print(self.name)

    def get_age(self):
        print(self.age)

class Kassir(Rabotnik):
    name = "Alex"
    age = "27"
    salary = "30000"

    def get_salary(self):
        print(self.salary)

    def get_name(self):
        print(self.name)

    def get_age(self):
        print(self.age)
