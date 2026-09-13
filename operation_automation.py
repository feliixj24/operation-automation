
import json
print("================================")
print("======Operation Automation======")
print("================================")
try:
    with open("tickets.json", "r") as file:
        tickets = json.load(file)
except json.JSONDecodeError:
    tickets = []
def menu_operation():
    while True:
        try:
        
            print("====Select your choice====")
            print("1 - Register Incident")
            print("2 - Search Information")
            print("3 - Find Incident")
            print("4 - Update Incident")
            print("5 - Delete Incident")
            print("6 - General Situation")
            print("7 - Pop out")

            answered = int(input(""))

            if answered == 1:
                register_incidents()
            elif answered == 2:

                file = research_information()
                if not file:
                    print("The file is blank at this moment, and it cannot be found")
                else:
                    print(file)
            elif answered == 3:
                ticket = find_incident()
                if not ticket:
                    print("There is not information releated with this incident number")
                else:
                    print(ticket)
            elif answered == 4:
                result = update_incident()
                if result:
                    print("The incident was found and it was updated succesfully")
                else:
                    print("There is not information releated with this incident number")
            elif answered == 5:
                result = delete_ticket()
                if result:
                    print("The information was sucessfully delete")
                else:
                    print("With this incident number, there is not information related")
            elif answered == 6:
                data_clear = general_information()
                if not data_clear:
                    print("There is not information now")
                else:
                    print(data_clear)
            elif answered == 7:
                break
            else:
                print("This opcion is not in the menu, try again")
        except ValueError:
            print("This informacion is wrong, try again")

def register_incidents():
    last_ticket = None
    for ticket in tickets:
        if last_ticket is None or ticket["id"] > last_ticket:
            last_ticket = ticket["id"]

    if last_ticket == None:
        last_ticket = 1
    else:
        last_ticket = last_ticket + 1

    new_ticket = {"id": last_ticket}
    while True:
        name = input("Type in the name: ")
        name = name.strip().lower()

        if not name:
            print("This field is required: ")
            continue
        if not name.isalpha():
            print("The information entered is invalid, try again")
            continue
        else:
            new_ticket["name"] = name
            break
    while True:
        last_name = input("Type the Last name: ")
        last_name = last_name.strip().lower()

        if not last_name:
            print("This field is required")
            continue
        if not last_name.isalpha():
            print("The information entered is invalid, try again")
            continue
        else:
            new_ticket["lastname"] = last_name
            break
    while True:
        information = input("Please enter a breaf description of the problem: ")
        information = information.strip().lower()

        if not information:
            print("This field is required")
            continue
        else:
            new_ticket["information"] = information
            break
    while True:
        try:
            scope = input("Please type in the amount of users was affected: ")
            scope = scope.strip()

            if not scope:
                print("This field is required")
                continue
            else:
                scope = int(scope)
                new_ticket["scope"] = scope
                break
        except ValueError:
            print("This information is wrong, try again")

    while True:
        priority = input("Please type in the priority: ")
        priority = priority.strip().lower()

        if not priority:
            print("This field is requried")
            continue
        if not priority.isalpha():
            print("The information type in is wrong, try again")
            continue
        else:
            new_ticket["priority"] = priority
            break
    tickets.append(new_ticket)
    with open("tickets.json", "w") as file:
        json.dump(tickets, file, indent=4)

def research_information():
    with open("tickets.json", "r") as file:
        ticket = json.load(file)
        return ticket

def find_incident():

    while True:
        incident_number = input("Please type in the incident number: ")
        incident_number = incident_number.strip().lower()

        if not incident_number:
            print("This file is required")
            continue
        try:
            incident_number = int(incident_number)
        except ValueError:
            print("The information put in is not valid, try again")
            continue
        with open("tickets.json", "r") as file:
            tickets = json.load(file)

        for ticket in tickets:
            if incident_number == ticket["id"]:
                return ticket
        return None
    
def update_incident():
    global tickets
    while True:      

            find_ticket = input("type in the ticket numer you wants to update: ")
            find_ticket = find_ticket.strip().lower()

            if not find_ticket:
                print("This field is required")
                continue
            try:
                find_ticket = int(find_ticket)
            except ValueError:
                print("The information type in is not valid, try again")
                continue
            else:
                
                for ticket in tickets:
                    if find_ticket == ticket["id"]:
                        print(ticket)
                        key_ticket = input("Type in the information you wants to update: ")
                        if key_ticket in ticket:
                            new_information = input("Please type in the new information")
                            ticket[key_ticket] = new_information
                            with open("tickets.json", "w") as file:                                
                               json.dump(tickets, file, indent=4)
                            result = ticket["id"]
                            return result
                return None
        
def delete_ticket():
    global tickets
    while True:
        print("Type in the ID number to delete the informacion: ")
        delete = input("")
        delete = delete.strip().lower()
        
        if not delete:
            print("This field is requeried")
            continue
        try:
            delete = int(delete)
        except ValueError:
            print("The informatio type in is not valid, try again")
            continue
            
        for ticket in tickets:
            if delete == ticket["id"]:
                tickets.remove(ticket)
                with open("tickets.json", "w") as file:
                    json.dump(tickets, file, indent=4)

                result = ticket["id"]
                return result
        return None

def general_information():     
    with open("tickets.json", "r") as archivo:
        tickets = json.load(archivo)
   
    data_clear = sorted(tickets, key=lambda ticket: ticket["scope"])
    return data_clear

menu_operation()


