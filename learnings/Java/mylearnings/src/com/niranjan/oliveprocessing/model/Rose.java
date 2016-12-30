package com.niranjan.oliveprocessing.model;

/**
 * Created by Niran0303 on 12/30/2016.
 */
public class Rose extends Olive {
    public Rose(){
        super(OliveNames.ROSE,OliveColors.RED,2.6);
    }

    public String getOrigin(){
        return "Spain";
    }
}
