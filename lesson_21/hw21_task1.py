"""
Task 1

File Context Manager class

Create your own class, which can behave like a built-in function 'open'. Also, you need to extend its functionality with
counter and logging. Pay special attention to the implementation of '__exit__' method, which has to cover all the requirements to context managers mentioned here:

Context Manager Types

The with statement
"""
import logging


class CustomOpen:
    counter = 0

    def __init__(self, fp: str, mode: str = "r", encoding: str = "UTF-8", log: bool = False):
        CustomOpen.counter += 1

        self.fp = fp
        self.mode = mode
        self.encoding = encoding
        self.log = log

        if log:
            datefmt = "%Y-%m-%d %H:%M:%S"
            log_format = "%(asctime)s - %(levelname)s : %(message)s"
            logging.basicConfig(filename="customopen_log.txt", level="INFO", format=log_format, datefmt=datefmt)
            logging.info(f"CustomOpen contextmanager initialized, counter: {CustomOpen.counter}")

    def __enter__(self):
        try:
            self.opened_file = open(file=self.fp, mode=self.mode, encoding=self.encoding)
        except FileNotFoundError:
            if self.log:
                logging.error(f"File {self.fp} not found")
            self.opened_file = None

        except ValueError as e:
            if self.log:
                logging.error(f"{e}")
            self.opened_file = None

        except TypeError as e:
            if self.log:
                logging.error(f"{e}")
            self.opened_file = None

        else:
            if self.log:
                logging.info(f"file {self.fp} has been opened")

        return self.opened_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.opened_file:
            self.opened_file.close()
            if self.log:
                logging.info(f"file {self.fp} has been closed")

                if exc_type:
                    logging.error(f"exception {exc_type} has been occurred\n")

                logging.shutdown()

        return True
