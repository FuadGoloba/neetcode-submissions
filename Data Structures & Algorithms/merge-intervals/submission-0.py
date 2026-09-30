class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # sort the intervals by the start so we can capture overlaps
        intervals.sort(key = lambda pair: pair[0])

        # Add the first interval in the output
        output = [intervals[0]]

        # traverse the interval list merging overlaps and appending non-overlaps
        for start, end in intervals[1:]:
            latest_end = output[-1][1]

            if start <= latest_end:
                # merge overlap
                output[-1][1] = max(latest_end, end)
            else:
                # append non-overlap
                output.append([start, end])
        return output
            




