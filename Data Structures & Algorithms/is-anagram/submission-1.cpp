class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        int length = s.length();

        std::vector<int> s_count(26, 0);
        std::vector<int> t_count(26, 0);

        for (int i = 0; i < length; ++i) {
            ++s_count[s[i] - 'a'];
            ++t_count[t[i] - 'a'];
        }

        for (int i = 0; i < 26; ++i) {
            if (s_count[i] != t_count[i]) {
                return false;
            }
        }
        return true;
    }
};
