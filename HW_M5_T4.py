def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "There is no contact with this name."
        except ValueError:
            return "Give me name and phone, please."
        except IndexError:
            return "Enter name, please."
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added with phone {phone}."

@input_error
def change_user_phone(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name}'s updated to {phone}."

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{name}'s phone: {contacts[name]}"


def show_all(contacts):
    return contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_user_phone(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
