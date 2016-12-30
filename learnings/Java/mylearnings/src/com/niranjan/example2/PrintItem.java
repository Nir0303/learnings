package com.niranjan.example2;

/**
 * Created by Niran0303 on 12/29/2016.
 */
public class PrintItem {
    public String item;
    public static void main(String args[]){
        PrintItem p = new PrintItem();
        p.item="Niranjan";
        p.printstring();
        char[] chars={'n','i','r','a','n','j','a','n'};
        String s2=new String(chars);
        System.out.println(s2);
    }
    private void printstring(){
        System.out.println("Print Name "+this.item);
    }
}
