class Solution {
public:
    string minWindow(string s, string t) {
        if (s.size() < t.size()) return "";
        unordered_map<char, int> win;
        unordered_map<char, int> count;

        for (auto& c : t){
            count[c]++;
        }

        int have = 0;
        int need = count.size();

        int resL = INT_MAX;
        int res[2] = {-1,-1};

        int l = 0;

        for (int r = 0; r < s.size(); ++r){
            char c = s[r];
            win[c]++;

            if (win[c] == count[c]) have++;

            while (have == need){
                if (r-l+1 < resL){
                    res[0] = l;
                    res[1] = r;
                    resL = r - l + 1;
                }
                win[s[l]]--;
                if (win[s[l]] < count[s[l]]) have--;
                l++;
            }
        }

        return resL != INT_MAX ? s.substr(res[0], resL) : "";
    }
};
