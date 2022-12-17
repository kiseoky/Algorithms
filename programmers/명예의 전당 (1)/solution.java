// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/138477

import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];

        for(int i=0;i<score.length;i++){
            Integer[] sub = Arrays.copyOf(Arrays.stream(score).boxed().toArray(Integer[]::new), i + 1);
            Arrays.sort(sub, Collections.reverseOrder());
            answer[i] = sub[Math.min(k-1, sub.length-1)];
        }
        return answer;
    }
}