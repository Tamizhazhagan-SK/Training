import java.sql.*;
import java.util.Scanner;
 
public class jdbc {
  public static void main(String args[]) {
    try {
        Scanner scan = new Scanner(System.in);
        int id = 0;
        String name = null;
        float salary = 0;
        // Step 1
        Connection connection = DriverManager.getConnection("jdbc:h2:mem:test", "ben", "stokes");
        System.out.println("Connected to in-memory DB!!!");
        // Step 2
        Statement statement = connection.createStatement();
        // Step 3
        statement.execute("Create table emp(id int, name varchar(20), sal float)");
        /*
        // insert few records
        id = scan.nextInt();
        name = scan.next();
        salary = scan.nextFloat();
        statement.execute("insert into emp values("+id+", '"+name+"', "+salary+")");
        // insert few records
        id = scan.nextInt();
        name = scan.next();
        salary = scan.nextFloat();
        statement.execute("insert into emp values("+id+", '"+name+"', "+salary+")");
        // insert few records
        id = scan.nextInt();
        name = scan.next();
        salary = scan.nextFloat();
        statement.execute("insert into emp values("+id+", '"+name+"', "+salary+")");
        */
        //Creating prepared statements
        PreparedStatement pstatement = connection.prepareStatement("insert into emp values(?,?,?)");
        pstatement.setInt(1, scan.nextInt());
        pstatement.setString(2, scan.next());
        pstatement.setFloat(3, scan.nextFloat());
        // to execute call executeUpdate() without arguments
        pstatement.executeUpdate();
        // Setting values for 2nd record
        pstatement.setInt(1, scan.nextInt());
        pstatement.setString(2, scan.next());
        pstatement.setFloat(3, scan.nextFloat());
        // to execute call executeUpdate() without arguments
        pstatement.executeUpdate();
 
        
        // retrieve the records
        ResultSet result = statement.executeQuery("select * from emp");
        // iterate using next() method - it takes care of iterating until there's a next record
        while(result.next()) {
            //ResultSet has getter methods for every datatype - getInt(index), getFloat(index)
            // you must pass column numbers to these getters to get the value of a particular row
            System.out.println(result.getInt(1)+"=>"+result.getString(2)+"=>"+result.getFloat(3));
            System.out.println("---------------------------------------------------------------");
        } 
        // close all the resourses
        result.close(); statement.close(); connection.close();
 
    } catch(Exception e) {
        e.printStackTrace();
    }
  }
}
 