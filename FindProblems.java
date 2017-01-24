import java.io.*;
public class FindProblems
{
	public static void main( String[] args ) throws Exception
	{
		//int nameLength = 18;//length of filename + space after it
		//int energyLength = 23;//length of "TOTAL ENERGY = " + " kJ/mol"

		BufferedReader infile = new BufferedReader( new FileReader("Total Energies-GenSet") );
		while( infile.ready() )
		{
			String string = infile.readLine();
			int i =0;
			while(true)
			{
				if( string.length() > (59+18*i) ) 
				{
					if( string.startsWith(".sdf", 31+18*i) )
						System.out.println( string.substring( (0+18*i),(17+18*i) ) );
					i++;
				}
				else
					break;
			}//end while loop
		}//end while loop
	}//end main
}//end program
