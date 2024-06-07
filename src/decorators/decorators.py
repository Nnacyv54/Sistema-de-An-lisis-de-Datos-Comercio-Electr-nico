import time 
import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(menssaje)s")




def timeit(func):
    #decorador para medir el tiempo de ejecución
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        elapsed_time=end_time - start_time
        logging.info(f"{func._name_} ejecutada en {elapsed_time:.4f} seconds")
        
        return result
    return wrapper


def logit(func):
    def wrapper(*args,**kwargs):
        logging.info(f"Corriendo {func._name_}")
        result=func(*args,**kwargs)
        logging.info(f"Completado")
        
    return wrapper
                     