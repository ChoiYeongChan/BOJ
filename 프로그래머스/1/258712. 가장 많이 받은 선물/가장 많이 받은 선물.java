import java.util.HashMap;
class Solution {
    public int solution(String[] friends, String[] gifts) {
        int answer = 0;
        int friendsLength=friends.length;
        HashMap<String, Integer> dic=new HashMap<>();
        int[] giftDegree=new int[friendsLength];
        int[][] giftGraph= new int[friendsLength][friendsLength];
        for (int i=0;i<friendsLength;i++) {
            dic.put(friends[i],i);
        }
        for (String gift : gifts) {
            String[] split=gift.split(" ");
            String x=split[0];
            String y=split[1];
            giftDegree[dic.get(x)]++;
            giftDegree[dic.get(y)]--;
            giftGraph[dic.get(x)][dic.get(y)]++;
        }
        for (int i=0;i<friendsLength;i++) {
            int n=0;
            for (int j=0; j<friendsLength; j++) {
                if (i==j) {
                    continue;
                }
                if (giftGraph[i][j]>giftGraph[j][i] || (giftGraph[i][j]==giftGraph[j][i] && giftDegree[i]>giftDegree[j])) {
                    n++;
                }
            }
            if (answer<n) {
                answer=n;
            }
        }
        return answer;
    }
}