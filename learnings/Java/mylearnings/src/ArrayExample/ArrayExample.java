package ArrayExample;

/**
 * Created by Niran0303 on 12/25/2016.
 */
public class ArrayExample {
    public static void main(String[] args) {
        String friends[];
        friends = new String[5];
        friends[0] = "tom";
        friends[1] = "john";
        friends[2] = "Depp";
        friends[3] = "jake";
        friends[4]="crusie";
        for (String i : friends) {
            System.out.println(i);
        }
    }
}
