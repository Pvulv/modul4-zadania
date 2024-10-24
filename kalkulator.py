import logging
import sys

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def new_equation(numbers, equation_name, result_equation):
    logging.info(f"{equation_name} {' i '.join(map(str, numbers))}")
    logging.info(f"Wynik to {result_equation}")