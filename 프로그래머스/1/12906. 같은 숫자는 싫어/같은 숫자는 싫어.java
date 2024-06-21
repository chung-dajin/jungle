import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        
		Stack<Integer> stack = new Stack<>();		
        
		for (int i : arr) {			
			if(stack.size() == 0 || i != stack.peek()) {
				stack.push(i);
			}
		}
        
        int []answer = new int[stack.size()];
		for (int i = 0; i < stack.size(); i++) {
            answer[i] = stack.get(i);
        }

        

        return answer;
    }
}