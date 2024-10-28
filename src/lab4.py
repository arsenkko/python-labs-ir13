class Hotel:
    def __init__(self, name, visitors_per_year, number_of_rooms):
        self.name = name 
        self.visitors_per_year = visitors_per_year 
        self.number_of_rooms = number_of_rooms 

    def __str__(self):
        return f"Готель: {self.name}, Відвідувачі протягом року: {self.visitors_per_year}, Номери: {self.number_of_rooms}"

hotel_1 = Hotel("Deputat", 23175, 330)

print(hotel_1)

