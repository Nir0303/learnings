package com.niranjan.fruits.data;

/**
 * Created by Niran0303 on 1/28/2017.
 */
public enum FruitNames {
    MANGO("Mango"),BANANA("Banana"),BLUEBERRY("Blueberry"),APPLE("Apple");
    private String fruit;
    private FruitNames(String fruit){
        this.fruit = fruit;
    }

    @Override
    public String toString() {
        return fruit;
    }
}
