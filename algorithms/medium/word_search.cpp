class Solution {
private:
    int COLS;
    int ROWS;

    bool dfs(vector<vector<char>>& board, const string& word, int r, int c, int i){
        if (i == word.size()){
            return true;
        }

        if (r < 0 || c < 0 || c >= COLS || r >= ROWS || word[i] != board[r][c] || board[r][c] == '#'){
            return false;
        }

        board[r][c] = '#';
        bool res = (dfs(board,word,r+1,c,i+1) || dfs(board,word,r-1,c,i+1) || dfs(board,word,r,c+1,i+1) || dfs(board,word,r,c-1,i+1));
        board[r][c] = word[i];
        return res;
    }
public:
    bool exist(vector<vector<char>>& board, string word) {
        COLS = board[0].size();
        ROWS = board.size();

        for (int r = 0; r < ROWS; ++r){
            for (int c = 0; c < COLS; ++c){
                if (dfs(board,word,r,c,0)){
                    return true;
                }
            }
        }
        return false;
    }
};
