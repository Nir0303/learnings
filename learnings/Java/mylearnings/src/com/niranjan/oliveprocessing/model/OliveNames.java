package com.niranjan.oliveprocessing.model;

/**
 * Created by Niran0303 on 12/30/2016.
 */
public enum OliveNames {
    KALAMATA("kalamata"),ROSE("rose"),BERRY("berry");

    private String name;
    OliveNames(String name){
        this.name=name;
    }

    public String toString(){
        return this.name;

    }

}
