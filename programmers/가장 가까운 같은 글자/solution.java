// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/142086

import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        Arrays.fill(answer, -1);

        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        for(int i=0;i<s.length();i++){

            if(map.get(s.charAt(i)) == null){
                map.put(s.charAt(i), i);
                continue;
            }
            answer[i] = i-map.get(s.charAt(i));
            map.put(s.charAt(i), i);

        }
        return answer;
    }
}