import java.util.*;
class Solution {
    public String[] solution(String[] players, String[] callings) {
        //String[] answer = {};
        HashMap<String, Integer> dic=new HashMap<>();
        int n=players.length;
        int i=0;
        for (String s:players) {
            dic.put(s,i);
            i++;
        }
        for (String c:callings) {
            int p=dic.get(c);
            String frontPlayer=players[p-1];
            dic.replace(c,p-1);
            dic.replace(frontPlayer,p);
            players[p-1]=c;
            players[p]=frontPlayer;
        }
        return players;
    }
}