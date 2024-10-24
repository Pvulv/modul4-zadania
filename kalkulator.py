import logging
import sys

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def new_equation(numbers, equation_name, result_equation):
    logging.info(f"{equation_name} {' i '.join(map(str, numbers))}")
    logging.info(f"Wynik to {result_equation}")

if __name__ == "__main__":
    name_text = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    
    numbers = []
    
    if name_text in ["1", "3"]:
        while True:
            number_text = input("Podaj liczbe (lub wpisz 'koniec', aby zakończyć): ")
            if number_text.lower() == 'koniec':
                break
            try:
                number = float(number_text)
                numbers.append(number)
            except ValueError:
                logging.error("jeden z podanych składników nie był liczbą!")
                sys.exit(1)
    
        if len(numbers) < 2:
            logging.error("Musisz podać przynajmniej dwie liczby!")
            sys.exit(1)
    
        if name_text == "1":
            equation_name = "Dodaję"
            result_equation = sum(numbers)
        elif name_text == "3":
            equation_name = "Mnożę"
            result_equation = 1
            for number in numbers:
                result_equation *= number
    elif name_text in ["2", "4"]:
        number_1_text = input("Podaj pierwszy składnik ")
        number_2_text = input("Podaj drugi składnik ")

        try:
            number_1 = float(number_1_text)
            number_2 = float(number_2_text)
        except ValueError:
            logging.error("Jeden ze składników nie jest liczbą!")
            sys.exit(1)
    
        if name_text == "2":
            equation_name = "Odejmuję"
            result_equation = number_1 - number_2
        elif name_text == "3":
            equation_name = "Mnożę"
            result_equation = number_1 * number_2
        elif name_text == "4":
            equation_name = "Dzielę"
            if number_2 != 0:
                result_equation = number_1 / number_2
            else:
                result_equation = "Nie można dzielić przez 0!"
        numbers = [number_1, number_2]
    else:
        equation_name = "Nieznane działanie"
        result_equation = "Błąd"
        numbers = []
        
new_equation(numbers, equation_name, result_equation)