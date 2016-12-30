package com.niranjan.calculator.util;
import java.util.Scanner;
/**
 * Created by Niran0303 on 12/30/2016.
 */
public class InputString {
    public static String getInput(String s){
        System.out.print(s);
        Scanner sc = new Scanner(System.in);
        return sc.nextLine();
    }
}
