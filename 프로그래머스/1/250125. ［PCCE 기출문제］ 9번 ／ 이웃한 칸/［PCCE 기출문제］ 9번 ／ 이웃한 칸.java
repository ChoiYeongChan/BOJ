class Solution {
    public int solution(String[][] board, int h, int w) {
        int answer = 0;
        int[] dx={0,0,1,-1};
        int[] dy={1,-1,0,0};
        int n=board.length;
        for (int i=0;i<4;i++) {
            int dh=h+dx[i];
            int dw=w+dy[i];
            if (dh>=0&&dh<n&&dw>=0&&dw<n) {
                if (board[h][w].equals(board[dh][dw])) {
                    answer++;
                }
            }
        }
        return answer;
    }
}