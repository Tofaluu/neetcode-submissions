class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int currentI = 0;
        vector<int> products;
        while (currentI < nums.size()) {
            int product = 1;
            for (int i = 0; i < nums.size(); ++i) {
                if (i != currentI) {
                    product *= nums[i];
                }
            }

            products.emplace_back(product);
            ++currentI;
        }

        return products;
    }
};
