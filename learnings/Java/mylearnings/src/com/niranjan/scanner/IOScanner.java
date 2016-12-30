package com.niranjan.scanner;
import java.util.Scanner;

/**
 * Created by Niran0303 on 12/29/2016.
 */
public class IOScanner {
    public static void main(String args[]){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Type some message");
        String s=scanner.nextLine();
        System.out.println(s);
    }
}
