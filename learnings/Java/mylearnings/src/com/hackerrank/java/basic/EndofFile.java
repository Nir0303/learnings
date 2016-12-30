package com.hackerrank.java.basic;

import java.util.Scanner;
/**
 * Run until end of file
 */
public class EndofFile {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cnt=1;
        while(true){
            String s = sc.nextLine();
            System.out.println(cnt+ " "+s);
            if(sc.hasNext()==false) break;
            cnt++;
        }
    }
}
