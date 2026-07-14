


public class Predefined_Classes {
    public static void main(String[] args) {
        String name = "Tamizh";
        String email = "tamizhsk@gmail.com";
        System.out.println("Length : " + name.length());
        System.out.println("Length : " + email.length());

        int indexOfAt = email.indexOf('@'); 
        String username = email.substring(0, indexOfAt);
        //last index of the domain
        int lastindexOf = email.lastIndexOf('m');
        String domain = email.substring(indexOfAt + 1, lastindexOf + 1);

        System.out.println("Index of @ in " + email + " " + indexOfAt );
        System.out.println("Username : " + username);
        System.out.println("Domain : " + domain.toUpperCase());

        String password = "tamizhsk1234";
        String confirmPassword = "tamizhsk1234";

        System.out.println("Password Match : " + password.equals(confirmPassword));



        



    }

}



/*

Predefined classes in Java

String
StringBuffer
Wrapper Classes - Integer, Double, Float, Character, Long, Short and more.
there are corresponding wrapper classes for all the primitive datatypes.

String: it creates immutable objects. (cannot be modified)

useful methods: concat(), length(), equals(), equalsIgnoreCase(), chartAt(), indexOf(), lastIndexOf(), toUpperCase(), toLowerCase(), split(),.....



StringBuffer / StringBuilder:
----------------

these create mutable strings, both has same methods, they have difference w.r.t their characters






*/