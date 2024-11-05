class Hotel:
    def __init__(self, name="", visitors_per_year=0, rooms=0, money=0):
        self.__name = name
        self.__visitors_per_year = visitors_per_year
        self.__rooms = rooms
        self.__money = money  

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_visitors_per_year(self):
        return self.__visitors_per_year

    def set_visitors_per_year(self, visitors):
        self.__visitors_per_year = visitors

    def get_money(self):
        return self.__money

    def set_money(self, amount):
        if amount > 0:
            self.__money += amount
        else:
            print("Прибуток має бути плюсовим")

    def __str__(self):
        return f"Hotel '{self.__name}', Visitors: {self.__visitors_per_year}, Rooms: {self.__rooms}, Money: ${self.__money}"

    def __repr__(self):
        return f"Hotel(name='{self.__name}', visitors={self.__visitors_per_year}, rooms={self.__rooms}, money={self.__money})"

    def __del__(self):
        print(f"Hotel '{self.__name}' is being deleted")

def find_least_profitable(hotels):
    return min(hotels, key=lambda hotel: hotel.get_money())

if __name__ == "__main__":
    hotel1 = Hotel("Grand Plaza", 5000, 120, 10000)
    hotel2 = Hotel("Sea View", 3000, 80, 7000)
    hotel3 = Hotel("Mountain Retreat", 1500, 50, 4000)

    hotel1.set_money(5000)
    hotel2.set_money(3000)
    hotel3.set_money(2000)

    print(hotel1)
    print(hotel2)
    print(hotel3)

    least_profitable = find_least_profitable([hotel1, hotel2, hotel3])
    print(f"Найбільший лох по прибутку: {least_profitable}")


