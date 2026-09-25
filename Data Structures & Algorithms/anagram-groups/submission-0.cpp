class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> anagrams;
        for (string word: strs) {
            bool foundWord = false;

            for (int i = 0; i < anagrams.size(); ++i) {
                if (anagramCalculator(word, anagrams[i][0])) {
                    anagrams[i].push_back(word);
                    foundWord = true;
                }
            }

            if (!foundWord) {
                vector<string> newWord = {word};
                anagrams.push_back(newWord);
            }
        }

        return anagrams;
    }

    bool anagramCalculator(string &str1, string &str2) {
        if (str1.length() != str2.length()) {
            return false;
        } 
        vector<int> alphabet(25, 0);

        for (int i = 0; i < str1.length(); ++i) {
            ++alphabet[str1[i] - 'a'];
            --alphabet[str2[i] - 'a'];
        }

        for (int j = 0; j < alphabet.size(); ++j) {
            if (alphabet[j] != 0) {
                return false;
            }
        }

        return true;

    }
};
