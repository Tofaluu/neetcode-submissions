class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> numberCount;
        vector<int> frequentList;

        for (int num: nums) {
            if (numberCount.find(num) == numberCount.end()) {
                numberCount[num] = 1;
            } else {
                auto it = numberCount.find(num);
                ++it->second;
            }
        }

        int highestFirst = numberCount.begin()->first;
        int highestSecond = numberCount.begin()->second;
        while (k > 0) {
            for (const auto &pair: numberCount) {
                bool alreadyInList = false;
                for (int i = 0; i < frequentList.size(); ++i) {
                    if (pair.first == frequentList[i]) {
                        alreadyInList = true;
                    }
                }

                if (!alreadyInList && (pair.second > highestSecond)) {
                    highestFirst = pair.first;
                    highestSecond = pair.second;
                }
            }

            frequentList.emplace_back(highestFirst);
            highestSecond = -1001;

            --k;
        }

        return frequentList;


    }

};
