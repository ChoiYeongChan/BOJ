import java.util.*;
class Solution {
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        
        HashMap<String, Integer> dic=new HashMap<>();
        dic.put("code",0);
        dic.put("date",1);
        dic.put("maximum",2);
        dic.put("remain",3);
        int n=dic.get(ext);
        int s=dic.get(sort_by);
        ArrayList<int[]> list=new ArrayList<>();
        for (int[] d : data) {
            if (d[n]<val_ext) {
                list.add(d);
            }
        }
        Collections.sort(list, (o1,o2)->o1[s]-o2[s]);
        int[][] answer = new int[list.size()][];
        for (int i=0;i<list.size();i++) {
            answer[i]=list.get(i);
        }
        return answer;
    }
}