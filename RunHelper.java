import java.io.*;
import java.util.Scanner;


public class RunHelper 
{ 
   public static void main(String[] args) throws IOException
   {
        
        try {
System.out.println("Starting search");
                Runtime rt = Runtime.getRuntime();
                Process pr = rt.exec("python3 search.py L");

                BufferedReader input = new BufferedReader(new InputStreamReader(pr.getInputStream()));
 
                String line=null;
 
                while((line=input.readLine()) != null) {
                    System.out.println(line);
                } 
            } catch(Exception e) {
                System.out.println(e.toString());
                e.printStackTrace();
            }

	Scanner infile = new Scanner(new File("save.txt"));
      
      String first = infile.nextLine().split("!")[0];

	while(!first.equals("1000")){

try {
System.out.println("Starting search");
                Runtime rt = Runtime.getRuntime();
                Process pr = rt.exec("python3 search.py L");
                
                BufferedReader input = new BufferedReader(new InputStreamReader(pr.getInputStream()));
 
                String line=null;
 
                while((line=input.readLine()) != null) {
                    System.out.println(line);
                }
            } catch(Exception e) {
                System.out.println(e.toString());
                e.printStackTrace();
            }


        infile = new Scanner(new File("save.txt"));
    
      first = infile.nextLine().split("!")[0];

}

   }
}
