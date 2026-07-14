

public class TestStringBuffer {

    public static void main(String[] args) {
        StringBuffer buffer1 = new StringBuffer("hello");
        
        //it reflects to the same object - mutable
        System.out.println("Buffer1 = " + buffer1);
        buffer1.append("123");
        System.out.println("Buffer1 after changes = " + buffer1); //hello123
        buffer1.reverse();
        System.out.println("Buffer1 after reverse = " + buffer1); //321olleh
        buffer1.delete(0, 3);
        System.out.println("Buffer1 after delete = " + buffer1);  //olleh


        //String buffer are thread safe (they are synced)
        //String builder are not thread safe because they are not synced

        //thread-safe : during concurrent modifications, no unexpected results

    }
}
