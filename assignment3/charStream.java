package assignment3;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

class charStream{
    static FileReader file;
    static FileWriter output;
    public static void main(String[] args) throws IOException{
        try{
            file = new FileReader(args[0]);
            output = new FileWriter("Output.txt");
            int temp;
            while((temp = file.read())!= -1) output.write((char)temp);
        }
        catch(Exception FileNotFoundException){
            System.out.println("File Not Found!");
        }
        finally{
            if (file != null) file.close();
            if (output != null) output.close();
        }
    }
}