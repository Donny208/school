/**
* lets you add a value
* @author Cameron Wright
*
*/
public class Index {
  private int firstInt;
  private int secondInt;
  
  /**
  * Creates the Index object
  * @param first int 
  * @param second int 
  */
  public Index(int first,int second){
    firstInt = first;
    secondInt = second;
  }
  /**
  * Adds the first and second value together
  * @returns the total
  */
  public int addValues(){
    return firstInt + secondInt;
  }
  
  public static void main(String [] argu){
    Index text = new Index(1,2);
    int total = text.addValues();
    System.out.println(total);
  }
}
