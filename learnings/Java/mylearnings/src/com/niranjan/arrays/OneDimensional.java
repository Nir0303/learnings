package com.niranjan.arrays;
import java.util.Arrays;
import java.util.*;

/**
 * Created by Niran0303 on 12/29/2016.
 */
public class OneDimensional {
    static void square(int x){
        System.out.println(x*x);
    }
    static void printNames(String k,String v){System.out.println(k+" "+v);}
    public static void main(String args[]){
        int ints[] = {1,2,34,12,12,121,1213,41321,11231,12,134,23};

        Arrays.sort(ints);
        for(int i:ints){
            System.out.println(i);
        }
        String[] s={"Niranjan","Addanki","John"};
        Arrays.sort(s);
        for(String i: s){
            System.out.println(i);
        }
        int[] x = new int[5];
        System.arraycopy(ints,5,x,0,5);
        for(int i:x){
            System.out.println(i);
        }
        List<Integer> list = new ArrayList<>();
        list.add(1);
        list.add(2);
        list.forEach(com.niranjan.arrays.OneDimensional::square);

        //Hash Map
        Map<String,String> map = new HashMap<>();

        map.put("Niranjan","Addanki");
        map.put("John","Jocabs");
        System.out.println(map);

        map.forEach(com.niranjan.arrays.OneDimensional::printNames);
        Set<String> keys = map.keySet();
        for(String t: keys){
            System.out.println("Keys are "+t);
        }

    }
}
