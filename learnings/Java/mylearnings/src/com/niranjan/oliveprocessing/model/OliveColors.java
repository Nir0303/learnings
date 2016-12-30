package com.niranjan.oliveprocessing.model;

/**
 * Created by Niran0303 on 12/30/2016.
 */
public enum OliveColors {
    BLUE("blue"),RED("red"),GREEN("purple");

    private String name;
    OliveColors(String name){
        this.name=name;
    }

    @Override
    public String toString(){
        return this.name;
    }

}
