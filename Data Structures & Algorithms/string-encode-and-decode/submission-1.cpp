class Solution {
public:

    string encode(vector<string>& strs) {
        string newString = "";
        for (const string str : strs) {
            newString += str + "/";
        }

        return newString;
    }

    vector<string> decode(string s) {
        vector<string> decodedString;
        int currentStartingPosition = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == '/') {
                string word = "";
                for (int j = currentStartingPosition; j < i; ++j) {
                    word += s[j];
                }

                decodedString.emplace_back(word);
                currentStartingPosition = i + 1;
            }
        }

        return decodedString;
    }
};
