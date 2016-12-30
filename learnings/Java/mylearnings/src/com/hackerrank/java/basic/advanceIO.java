package com.hackerrank.java.basic;

import java.util.Scanner;
/**
 * Input Format

 There are three lines of input:

 The first line contains an integer.
 The second line contains a double.
 The third line contains a String
 */
public class advanceIO {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int i = Integer.parseInt(scan.nextLine());
        double d=Double.parseDouble(scan.nextLine());
        String s=scan.nextLine();
        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}
