import json

# to add Validation class!!!

class ValidationError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __repr__(self):
        return f"ValidationError: {self.msg}"


class Record:
    PHONE_NUMBER_NOT_VALID_MSG = "Not valid phone number, should include 12 digits only"
    FIELD_NOT_VALID_MSG = "NAME Field can not be empty"
    SUCCESS_MSG = "Operation succeed"

    def __init__(self, first_name: str, last_name: str, phone_number: str, city: str, country: str):
        self.first_name = self.validate_record_field(first_name)
        self.last_name = self.validate_record_field(last_name)
        self.phone_number = self.validate_phone_number(phone_number)
        self.city = city.capitalize()
        self.country = country.capitalize()

    @classmethod
    def validate_phone_number(cls, phone_number: str) -> str:
        if phone_number[0] != "+":
            phone_number = "+" + phone_number

        if len(phone_number) != 13 or not phone_number[1:].isnumeric():
            raise ValidationError(cls.PHONE_NUMBER_NOT_VALID_MSG)

        # validate for existing of such number needed

        return phone_number

    @classmethod
    def validate_record_field(cls, data: str) -> str:
        if data:
            return data.capitalize()
        raise ValidationError(cls.FIELD_NOT_VALID_MSG)

    def record_to_dict(self) -> dict:
        record = {
            "first name": self.first_name,
            "last name": self.last_name,
            "phone number": self.phone_number,
            "city": self.city,
            "country": self.country
        }
        return record

    def load_records(self, fb: "PhoneBook") -> list:
        try:
            with open(fb.fp) as db:
                record_list = json.load(db)
        except FileNotFoundError:
            record_list = []

        return record_list

    def save_record(self, fb: "PhoneBook"):
        records = self.load_records(fb)
        record = self.record_to_dict()
        records.append(record)

        with open(fb.fp, "w") as db:
            json.dump(records, db)

        print(self.SUCCESS_MSG)


class PhoneBook:
    EXT = ".json"
    DATA_FILE = "data.json"
    FP_NOT_VALID_MSG = "Name of phonebook couldn't be empty or DATA"

    def __init__(self, fp: str):
        self.fp = self.validate_fp(fp)

    @classmethod
    def validate_fp(cls, fp) -> str:
        if fp and fp != cls.DATA_FILE:
            return fp.lower + cls.EXT

        raise ValidationError(cls.FP_NOT_VALID_MSG)

    def create_record(self, first_name, last_name, phone_number, city, country):
        new_record = Record(first_name, last_name, phone_number, city, country)
        new_record.save_record(self)
