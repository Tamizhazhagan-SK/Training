import java.sql.*;
import java.util.Scanner;

public class BookManagementSystem {

    public static void main(String[] args) {

        try {
            Scanner sc = new Scanner(System.in);
            Connection con = DriverManager.getConnection("jdbc:h2:mem:test", "user", "user@123");
            Statement stmt = con.createStatement();

            stmt.execute("CREATE TABLE Book(bookId INT PRIMARY KEY, title VARCHAR(100), copiesAvailable INT, publicationYear INT)");

            processMenu(con, sc);

            stmt.close();
            con.close();
            sc.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    static void processMenu(Connection con, Scanner sc) {

        int choice;
        do {
            System.out.println("\n1. Insert Book");
            System.out.println("2. Display Books Sorted by Publication Year and Title");
            System.out.println("3. Display Books by Title Pattern");
            System.out.println("4. Display All Books");
            System.out.println("5. Update Copies Available");
            System.out.println("6. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            switch (choice) {

                // insert books
                case 1:
                    insertBook(con, sc);
                    break;
                // sorting the books
                case 2:
                    displayBooksSorted(con);
                    break;
                //showing in title patter
                case 3:
                    displayBooksByTitlePattern(con, sc);
                    break;
                // show all books
                case 4:
                    displayAllBooks(con);
                    break;
                // update the copies
                case 5:
                    updateCopies(con, sc);
                    break;
                // close
                case 6:
                    System.out.println("\nApplication terminated");
                    break;

                default:
                    System.out.println("Invalid Choice");
            }

        } while (choice != 6);
    }

    static void insertBook(Connection con, Scanner sc) {

        try {
            int bookId = sc.nextInt();
            sc.nextLine();
            String title = sc.nextLine();
            int copies = sc.nextInt();
            int year = sc.nextInt();

            PreparedStatement ps = con.prepareStatement("INSERT INTO Book VALUES(?,?,?,?)");

            ps.setInt(1, bookId);
            ps.setString(2, title);
            ps.setInt(3, copies);
            ps.setInt(4, year);
            ps.executeUpdate();

            System.out.println("\nBook inserted successfully");
            displayAllBooks(con);
            ps.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    static void displayBooksSorted(Connection con) {

        try {
            Statement st = con.createStatement();
            ResultSet rs = st.executeQuery("SELECT * FROM Book ORDER BY publicationYear ASC, title DESC");
            System.out.println("\nBooks sorted by publication year and title:");

            while (rs.next()) {
                System.out.println("Book Id = " + rs.getInt("bookId") + ", Title = " + rs.getString("title") + ", Copies = " + rs.getInt("copiesAvailable") + ", Year of publication = " + rs.getInt("publicationYear"));
            }
            rs.close();
            st.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    static void displayBooksByTitlePattern(Connection con, Scanner sc) {

        try {
            String pattern = sc.next();
            PreparedStatement ps =con.prepareStatement("SELECT * FROM Book WHERE title LIKE ?");
            ps.setString(1, pattern + "%");
            ResultSet rs = ps.executeQuery();
            System.out.println("\nBooks with title starting with " + pattern + ":");

            while (rs.next()) {
                System.out.println("Book Id = " + rs.getInt("bookId") + ", Title = " + rs.getString("title") + ", Copies = " + rs.getInt("copiesAvailable") + ", Year of publication = " + rs.getInt("publicationYear"));
            }
            rs.close();
            ps.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    static void displayAllBooks(Connection con) {

        try {
            Statement st = con.createStatement();
            ResultSet rs = st.executeQuery("SELECT * FROM Book");
            System.out.println("All Books:");

            while (rs.next()) {
                System.out.println("Book Id = " + rs.getInt("bookId") + ", Title = " + rs.getString("title") + ", Copies = " + rs.getInt("copiesAvailable") + ", Year of publication = " + rs.getInt("publicationYear"));
            }
            rs.close();
            st.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    static void updateCopies(Connection con, Scanner sc) {

        try {
            int bookId = sc.nextInt();
            int newCopies = sc.nextInt();

            PreparedStatement ps = con.prepareStatement("UPDATE Book SET copiesAvailable=? WHERE bookId=?");

            ps.setInt(1, newCopies);
            ps.setInt(2, bookId);
            ps.executeUpdate();
            System.out.println("\nBook updated successfully");
            displayAllBooks(con);
            ps.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}