class Solution():
    def insert(self, intervals, newInterval):
        START, END = 0, 1
        s, e = newInterval[START], newInterval[END]
        left, right = [], []

        for curr_interval in intervals:
            if curr_interval[1] < s:            # 如果現在的結尾 < 插入的interval開頭
                left.append(curr_interval)      # 就加到 左邊
            elif curr_interval[0] > e:          # 如果現在的開頭 > 插入的interval結尾
                right.append(curr_interval)     # 就加入到右邊 
            else:   # 這裡處理重疊的數值
                s = min(curr_interval[START],s)
                e = max(curr_interval[END],e)
        return left + [[s,e]] + right


        # res, n = [], newInterval
        # for index, i in enumerate(intervals):
            
        #     if i.end < n.start:
        #         res.append(i)
        #     elif n.end < i.start:
        #         res.append(n)
        #         return res+intervals[index:]  # can return earlier
        #     else:  # overlap case
        #         n.start = min(n.start, i.start)
        #         n.end = max(n.end, i.end)
        # res.append(n)
        # return 

if __name__ == "__main__":
    ans = Solution()
    result= ans.insert([[1,5],[9,10],[12,23]],[4,11])
    print(result)