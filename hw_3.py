def handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "KeyError"
        except ValueError:
            return "ValueError"
        except IndexError:
            return "IndexError"
    return wrapper


@handler
def add(arg, contacts):
    try:
        return arg + contacts
    except ValueError:
        print('Error')









# def parse_input(user_input):
#     cmd, *args = user_input.split()
#     cmd = cmd.strip().lower()
#     return cmd, *args
#
#
# def add_contact(args, contacts):
#     name, phone = args
#     contacts[name] = phone
#     return "Contact added."
#
#
# def change_contact(args, contacts):
#     name, phone = args
#     if name in contacts:
#         raise ValueError("Contact")
#     contacts[name] = phone
#     return "Contact updated successfully"
#
#
# def show_contact(args, contacts):
#     name, _ = args
#     return contacts[name]
#
#
# def main():
#     contacts = {}
#     print("Welcome to the assistant bot!")
#
#     while True:
#         user_input = input("Enter a command: ")
#         command, *args = parse_input(user_input)
#
#         if command in ["close", "exit"]:
#             print("Good bye!")
#             break
#         elif command == "hello":
#             print("How can I help you?")
#         elif command == "add":
#             print(add_contact(args, contacts))
#         elif command == "change":
#             print(change_contact(args, contacts))
#         elif command == "show":
#             print(show_contact(args, contacts))
#         else:
#             print("Invalid command.")
#
#
# if __name__ == "__main__":
#     main()
#
