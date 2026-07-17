import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Scanner;

public class ContactManagementSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        HashMap<Long, Contact> contacts = new HashMap<>();
        ContactManager manager = new ContactManager(scanner);

        System.out.println("Enter size: ");
        int size = Integer.parseInt(scanner.nextLine().trim());
        manager.addContacts(contacts, size);

        while (true) {
            System.out.println("\nSelect an operation:");
            System.out.println("1. Add contact");
            System.out.println("2. Remove contact by name");
            System.out.println("3. Edit contact");
            System.out.println("4. Display contacts by age range");
            System.out.println("5. Display contacts by name filter");
            System.out.println("6. Display all contacts");
            System.out.println("7. Exit");

            int choice;
            try {
                choice = Integer.parseInt(scanner.nextLine().trim());
            } catch (NumberFormatException ex) {
                System.out.println("Invalid choice. Please enter a number.");
                continue;
            }

            switch (choice) {
                case 1:
                    System.out.println("Enter details for the new contact:");
                    System.out.println("Format: number name email age");
                    long newNumber = Long.parseLong(scanner.nextLine().trim());
                    String newName = scanner.nextLine();
                    String newEmail = scanner.nextLine();
                    int newAge = Integer.parseInt(scanner.nextLine().trim());
                    try {
                        Contact newContact = new Contact(newNumber, newName, newEmail, newAge);
                        manager.addSingleContact(contacts, newContact);
                    } catch (AgeInvalidException | InvalidEmailException ex) {
                        System.out.println(ex.getMessage());
                    }
                    break;
                case 2:
                    System.out.println("Enter name");
                    String nameToRemove = scanner.nextLine();
                    manager.removeContactsByName(contacts, nameToRemove);
                    break;
                case 3:
                    System.out.println("Enter number, name, email, age");
                    long editNumber = Long.parseLong(scanner.nextLine().trim());
                    String editName = scanner.nextLine();
                    String editEmail = scanner.nextLine();
                    int editAge = Integer.parseInt(scanner.nextLine().trim());
                    try {
                        Contact c = new Contact(editNumber, editName, editEmail, editAge);
                        manager.editContact(contacts, editNumber, c);
                    } catch (AgeInvalidException | InvalidEmailException ex) {
                        System.out.println(ex.getMessage());
                        System.out.println("Contact number not found. Update failed.");
                    }
                    break;
                case 4:
                    System.out.println("Enter ageThreshold");
                    int ageThreshold = Integer.parseInt(scanner.nextLine().trim());
                    manager.displayContactThreshold(contacts, 20, ageThreshold);
                    break;
                case 5:
                    System.out.println("Enter nameFilter");
                    String nameFilter = scanner.nextLine();
                    manager.displayContactThreshold(contacts, nameFilter);
                    break;
                case 6:
                    System.out.println("All contacts:");
                    manager.displayAllContacts(contacts);
                    break;
                case 7:
                    System.out.println("Exiting program...");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }
}

class Contact {
    private long number;
    private String name;
    private String email;
    private int age;

    public Contact(long number, String name, String email, int age) {
        this.number = number;
        this.name = name;
        setEmail(email);
        setAge(age);
    }

    public Contact() {}

    public long getNumber() {
        return number;
    }

    public void setNumber(long number) {
        this.number = number;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        if (email == null || !email.contains("@") || !email.endsWith(".com")) {
            throw new InvalidEmailException("Invalid email: must contain '@' and end with '.com'");
        }
        this.email = email;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        if (age < 0) {
            throw new AgeInvalidException("Age cannot be negative: " + age);
        }
        this.age = age;
    }

    @Override
    public String toString() {
        return "Contact [number=" + number + ", name=" + name + ", email=" + email + ", age=" + age + "]";
    }
}

class InvalidEmailException extends RuntimeException {
    public InvalidEmailException() {
        super();
    }

    public InvalidEmailException(String message) {
        super(message);
    }

    public InvalidEmailException(String message, Throwable cause) {
        super(message, cause);
    }
}

class AgeInvalidException extends RuntimeException {
    public AgeInvalidException() {
        super();
    }

    public AgeInvalidException(String message) {
        super(message);
    }

    public AgeInvalidException(String message, Throwable cause) {
        super(message, cause);
    }
}

class ContactManager {
    private Scanner scanner;

    ContactManager(Scanner scanner) {
        this.scanner = scanner;
    }

    void addContacts(HashMap<Long, Contact> contacts, int n) {
        for (int i = 0; i < n; i++) {
            System.out.println("Enter details for contact " + (i + 1) + ":");
            System.out.println("Format: number name email age");

            long number = Long.parseLong(scanner.nextLine().trim());
            String name = scanner.nextLine();
            String email = scanner.nextLine();
            int age = Integer.parseInt(scanner.nextLine().trim());

            addSingleContact(contacts, new Contact(number, name, email, age));
        }
    }

    void addSingleContact(HashMap<Long, Contact> contacts, Contact contact) {
        if (contacts.containsKey(contact.getNumber())) {
            System.out.println("Contact number already exists. Skipping contact.");
            return;
        }

        contacts.put(contact.getNumber(), contact);
        System.out.println("Contact added successfully");
    }

    void removeContactsByName(HashMap<Long, Contact> contacts, String name) {
        if (contacts.isEmpty()) {
            System.out.println("No contacts found with name: " + name);
            return;
        }

        Iterator<Map.Entry<Long, Contact>> it = contacts.entrySet().iterator();
        boolean removed = false;
        while (it.hasNext()) {
            Map.Entry<Long, Contact> entry = it.next();
            if (entry.getValue().getName().equals(name)) {
                it.remove();
                removed = true;
            }
        }

        if (removed) {
            System.out.println("Contacts removed successfully for name: " + name);
        } else {
            System.out.println("No contacts found with name: " + name);
        }
    }

    void editContact(HashMap<Long, Contact> contacts, long number, Contact contact) {
        if (contacts.containsKey(number)) {
            contacts.put(number, contact);
            System.out.println("Contact updated successfully");
        } else {
            System.out.println("Contact number not found. Update failed.");
        }
    }

    void displayContactThreshold(HashMap<Long, Contact> contacts, int startAge, int endAge) {
        if (contacts.isEmpty()) {
            System.out.println("No contacts available");
            return;
        }

        boolean found = false;
        String header = "Contacts with age between " + startAge + " and " + endAge + ":";
        StringBuilder sb = new StringBuilder();
        for (Contact c : contacts.values()) {
            if (c.getAge() >= startAge && c.getAge() <= endAge) {
                if (!found) {
                    sb.append(header).append("\n");
                }
                sb.append(c.toString()).append("\n");
                found = true;
            }
        }

        if (found) {
            System.out.print(sb.toString());
        } else {
            System.out.println("No contacts found in the age range " + startAge + " to " + endAge);
        }
    }

    void displayContactThreshold(HashMap<Long, Contact> contacts, String nameFilter) {
        if (contacts.isEmpty()) {
            System.out.println("No contacts available");
            return;
        }

        boolean found = false;
        String header = "Contacts starting with '" + nameFilter + "':";
        StringBuilder sb = new StringBuilder();
        for (Contact c : contacts.values()) {
            if (c.getName().startsWith(nameFilter)) {
                if (!found) {
                    sb.append(header).append("\n");
                }
                sb.append(c.toString()).append("\n");
                found = true;
            }
        }

        if (found) {
            System.out.print(sb.toString());
        } else {
            System.out.println("No contacts found starting with '" + nameFilter + "'");
        }
    }

    void displayAllContacts(HashMap<Long, Contact> contacts) {
        if (contacts.isEmpty()) {
            System.out.println("No contacts available");
            return;
        }

        System.out.println("All contacts:");
        for (Contact c : contacts.values()) {
            System.out.println(c.toString());
        }
    }
}


