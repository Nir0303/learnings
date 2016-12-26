package com.niranjan.loopiteration;

/**
 * Created by Niran0303 on 12/25/2016.
 */
public class Loopiterators {
    public static void main(String[] args){
        int n=10;
        while(n>0){
            System.out.println(n);
            n--;
        }
        int i=100;
        int j=230;
        while(++i<--j);
        System.out.println("Mid point is"+i);
        do{
            System.out.println("Value is "+i );
            n++;
        }while(i<10);
        String[][] test = {{"Hi there","How are you"},{"Hi there","How are you"}};
        for(String[] k:test)
            for (String t : k) {
                System.out.println(t);

            }



    }
}
