package com.niranjan.menuoptions;

/**
 * Created by Niran0303 on 12/25/2016.
 */
public class Menuoptions {
    public static void main(String[] args) throws java.io.IOException{
        char choice;
        do {
            System.out.println("Help on: ");
            System.out.println(" 1. if");
            System.out.println(" 2. switch");
            System.out.println(" 3. while");
            System.out.println(" 4. do-while");
            System.out.println(" 5. for\n");
            System.out.println("Choose one:");
            choice=(char) System.in.read();
        } while(choice<'1' || choice >'5');
        switch(choice){
            case '1': System.out.println("If Statement");break;
            case '2':System.out.println("Switch statement");break;
            case '3':System.out.println("While Statement");break;
            case '4':System.out.println("do-while Statement");break;
            case '5':System.out.println("For statement");break;
            default: System.out.println("Invalid Statement");
        }
    }
}
