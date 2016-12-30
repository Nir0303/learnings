package com.niranjan.fileio;

import org.apache.commons.io.FileUtils;

import java.io.*;

import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.Files;


/**
 * Created by Niran0303 on 12/30/2016.
 */
public class FileIO {
    //old implementation
    public static void main(String args[]) throws IOException,FileNotFoundException {
        String ifile="files/test.txt";
        String ofile="files/wtest.txt";
        FileReader fReader = new FileReader(ifile);
        BufferedReader bReader = new BufferedReader(fReader);
        FileWriter wReader = new FileWriter(ofile);
        try {
            while(true){
                String s= bReader.readLine();
                if(s==null) {
                    break;
                }
                else {
                    wReader.write(s+"\n");
                }
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        }
        finally {
            fReader.close();
            wReader.close();
            bReader.close();
        }


        //easy implementation java 7 implementation
        Path ioPath = Paths.get("files/test.txt");
        Path outPath = Paths.get("files/oaptest.txt");
        Files.copy(ioPath,outPath);


        //apache commons implementation

        File iapfile = new File("files/test.txt");
        File oapfile = new File("files/aptest.txt");
        try {
            FileUtils.copyFile(iapfile, oapfile);
        }
        catch(Exception e){
            e.printStackTrace();

        }
    }

}
