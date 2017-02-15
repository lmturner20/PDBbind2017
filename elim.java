import java.io.*;
import java.util.*;
public class elim
{
	public static void main( String[] args )throws Exception
	{
		BufferedReader elimfile = new BufferedReader( new FileReader( args[0] ) );//files to be eliminated
		BufferedReader fullfile = new BufferedReader( new FileReader( args[1] ) );
		HashSet<String> elimLigands = new HashSet<String>();

		elimfile.readLine();
		while( elimfile.ready() )
		{
			String elimLig = elimfile.readLine();
			elimLigands.add(elimLig);
		}
		elimfile.close();

		fullfile.readLine();
		while( fullfile.ready() )
		{
			String line = fullfile.readLine();
			String lig = line.substring( 0,4 );
			if( elimLigands.add(lig) == true )
				System.out.println( lig );
		}
		fullfile.close();
	}//end main
}//end program
