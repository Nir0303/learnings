package com.niranjan.fruits;

/**
 * Created by Niran0303 on 1/28/2017.
 */

import com.niranjan.fruits.data.*;

import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;

public class MyFruits {

    public static void main(String args[]){
        FruitMarket myfruits = new FruitMarket();
        myfruits.addCart(FruitNames.APPLE,"Green");
        myfruits.addCart(FruitNames.MANGO,"Yellow");
        myfruits.addCart(FruitNames.BLUEBERRY,"Blue");
        myfruits.printCart();

        Class <?> o = myfruits.getClass();

        System.out.println(o);
        System.out.println(o.getName());
        System.out.println(o.getSimpleName());

        Package p = o.getPackage();
        System.out.println("Package Name is "+p.getName());





    }
}
