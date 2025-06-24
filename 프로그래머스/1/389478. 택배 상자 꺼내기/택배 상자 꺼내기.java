class Solution {
    public int solution(int n, int w, int num) {
        int answer = 0;
        int m=n/w+1;
        int[][] boxes=new int[m][w];
        int numx=0;
        int numy=0;
        int x=0;
        int y=0;
        boolean left=true;
        for(int i=1;i<=n;i++) {
            if (i==num) {
                numx=x;
                numy=y;
            }
            if (left) {
                boxes[y][x]=i;
                if(x==w-1) {
                    y++;
                    left=false;
                }
                else {
                    x++;
                }
            }
            else {
                boxes[y][x]=i;
                if (x==0) {
                    y++;
                    left=true;
                }
                else {
                    x--;
                }
            }
        }
        while(numy<m) {
            if(boxes[numy][numx]!=0) {
                answer++;
            }
            numy++;
        }
        return answer;
    }
}