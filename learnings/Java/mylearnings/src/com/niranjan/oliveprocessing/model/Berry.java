package com.niranjan.oliveprocessing.model;

/**
 * Created by Niran0303 on 12/30/2016.
 */
public class Berry extends Olive {
    public Berry(){
        super(OliveNames.BERRY,OliveColors.GREEN,3.6);
    }
    public String getOrigin(){
        return "India";
    }
}
