from faker import Faker
import json

faker = Faker()

def generate_basic_data():
    return {
        "name": faker.name(),
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "address": faker.address(),
        "email": faker.email(),
        "phone_number": faker.phone_number(),
        "date_of_birth": str(faker.date_of_birth()),
    }

def generate_business_data():
    return {
        "company": faker.company(),
        "job": faker.job(),
        "catch_phrase": faker.catch_phrase(),
        "credit_card": faker.credit_card_number(),
        "currency": faker.currency_code(),
        "price": faker.pricetag(),
    }

def generate_internet_data():
    return {
        "url": faker.url(),
        "domain_name": faker.domain_name(),
        "ipv4": faker.ipv4(),
        "mac_address": faker.mac_address(),
        "email": faker.free_email(),
        "user_name": faker.user_name(),
    }

def generate_profile_data():
    return faker.profile()

def generate_date_time_data():
    return {
        "date": str(faker.date()),
        "time": str(faker.time()),
        "unix_time": faker.unix_time(),
        "iso8601": faker.iso8601(),
    }

def generate_misc_data():
    return {                
        "hex_color": faker.hex_color(),
        "random_bool": faker.pybool(),
        "random_int": faker.random_int(min=10, max=100),
        "color": faker.color_name(),
        "language": faker.language_name(),
        "currency": faker.currency_name(),
        "uuid": faker.uuid4()
    }

def main():
    print("=== Basic Data ===")
    print(json.dumps(generate_basic_data(), indent=2))

    print("\n=== Business Data ===")
    print(json.dumps(generate_business_data(), indent=2))

    print("\n=== Internet Data ===")
    print(json.dumps(generate_internet_data(), indent=2))

    print("\n=== Full Profile Data ===")
    print(json.dumps(generate_profile_data(), indent=2, default=str))

    print("\n=== Date/Time Data ===")
    print(json.dumps(generate_date_time_data(), indent=2))

    print("\n=== Miscellaneous Data ===")
    print(json.dumps(generate_misc_data(), indent=2))

if __name__ == "__main__":
    main()
