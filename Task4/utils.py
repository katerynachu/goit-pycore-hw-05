from decorators import input_error

def parse_input(user_input):
    if not user_input.strip():
        return "", []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} updated"
    raise KeyError

@input_error
def show_phone(args,contacts):
    name = args[0]
    if name in contacts:
        phone_number = contacts[name]
        return phone_number
    else:
        raise KeyError
    
@input_error
def show_all(contacts):
    if not contacts:
        return "Your contact list is empty"
    result = "All contacts:\n"
    for name,phone in contacts.items():
        result+=f"{name}:{phone}\n"
    return result.strip()    




def main():
    pass
if __name__ == '__main__':
    main() 
