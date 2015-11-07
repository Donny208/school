import java.util.Random;

/**
 * lets you add a value
 * @author Cameron Wright
 *
 */
public class Index {
	private int firstInt;
	private int secondInt;
	private int TotalInt;
	
	/**
	 * Creates the Index object
	 * @param first int 
	 * @param second int 
	 */
	public Index(int first,int second){
		firstInt = first;
		secondInt = second;
		TotalInt = 0;
	}
	/**
	 * Adds the first and second value together
	 * @returns the totalInt
	 */
	public int addValues(){
		return TotalInt = firstInt + secondInt;
	}
	
	public int getfirstInt(){
		return firstInt;
	}
	
	public int getsecondInt(){
		return secondInt;
	}
	
	public int getTotalInt(){
		return TotalInt;
	}
	
	public String toString(){
		return getfirstInt() + " + " + getsecondInt() + " = " + getTotalInt();
	}
	
	public static void main(String [] args) {
		Random rdm = new Random();
		
		Index text = new Index(rdm.nextInt(100)+1,rdm.nextInt(100)+1);
		text.addValues();
		System.out.println(text);
	}
}
