
import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) throws IOException{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
	    int t=Integer.parseInt(br.readLine());
		for(int i=0;i<t;i++)
		{
		    int len=Integer.parseInt(br.readLine());
		    String str=br.readLine();
		    
		    int l=0,flag=0;
		    int h=len-1;
		    while(l<=h)
		    {
		        if(str.charAt(l++)!=str.charAt(h--))
		        {
		           flag=-1;
		        }
		    }
		    if(flag==-1)
		        System.out.println("No");
		    else
		        System.out.println("Yes");
		}
	}
}
