import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class TestIterator {
    public static void main(String[] args) {
        List<String> strings = new ArrayList<>();
        strings.add("Tamizh");
        strings.add("Gowtham");
        strings.add("Aaron");
        strings.add("Aadhi");
        strings.add("Shreejith");
        strings.add("Harris");
        strings.add("Murph");
        strings.add("LakshmiAmmal");
        strings.add("Zendaya");

        // since for loop doesn't allow the modification; we must use Iterator here
        Iterator<String> iterate = strings.iterator();
        while(iterate.hasNext()){
            String name = iterate.next();
            if(name.contains("ar")){
                iterate.remove();
            }
        }

        // for(String name : strings){
        //     if(name.startsWith("A")){
        //         strings.remove(name);
        //     }
        // }

        System.out.println(strings);

        /*
        remove(element) : Collection
        remove(index) : List
        remove() : Iterator
        */

    }


}


/*

Iterator<I>

used to iterate elements in the collection,
works similar to 'for loop'; 
but it can perform remove while iterating, where for loop can't remove while iterating, trying to remove from collection


it has 3 methods:

hasNext() --  to verify if the next element is present
next()    --  to iterate the next element & also returns the next arguments
remove()  --  to remove the elements



*/