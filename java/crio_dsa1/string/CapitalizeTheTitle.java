package java.crio_dsa1.string;

public class CapitalizeTheTitle {
    public String capitalizeTitle(String title) {
      
      //whenever modification convert string to char array
      char[] chars = title.toCharArray();
      int first = 0;
	 //right pointer for curr char
      for(int i=0; i<=chars.length-1; i++){
        //move right till space within length
        while(i<=chars.length-1 && chars[i]!=' '){    //recheck because you are incrementing inside a loop
            //if capital char, make it small
            if(chars[i]>=65 && chars[i]<=90){
                chars[i] = (char) (chars[i] + 32);
            }
            i++;
        }
	   
	   //if length>2 and letter at first is small letter, make it capital
        int length = i-first;
        if(length>2 && chars[first]>=97 && chars[first]<=122){
            chars[first] = (char) (chars[first] - 32);
        }

        //first becomes first letter of next word
        first = i+1;
      }
        //return as string
        return new String(chars);
    }
}
