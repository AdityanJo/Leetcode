class Solution:
    def checkMerge(self, interval1, interval2):
        if interval1[-1]>=interval2[0]:
            return [min(interval1[0], interval2[0]),max(interval2[-1], interval1[-1])]
        else:
            return None
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals==[]: return intervals
        intervals.sort()
        merged_intervals=[intervals[0]]
        del(intervals[0])

        while len(intervals)!=0:
            if len(merged_intervals)==0:
                merged_intervals=[intervals[0]]
                del(intervals[0])

            for i, interval in enumerate(merged_intervals):
                merge=self.checkMerge(interval, intervals[0])
                if merge:
                    intervals[0]=merge
                    del(merged_intervals[i])
                    break
            merged_intervals.append(intervals[0])
            del(intervals[0])
        return merged_intervals
