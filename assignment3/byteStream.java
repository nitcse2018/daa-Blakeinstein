package assignment3;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class byteStream {
    static FileInputStream file;
    static FileOutputStream output;
    public static void main(String[] args) throws IOException{
        try{
            file = new FileInputStream(args[0]);
            output = new FileOutputStream("Output.txt");
            int temp;
            while((temp=file.read()) != -1) output.write((byte)temp);
        }
        catch(Exception fileNotFoundException){
            System.out.println("File not Found!");
        }
        finally{
            if (file != null) file.close();
            if (output != null) output.close();
        }
    }
}