class Twitter:

    def __init__(self):
        self.followMap, self.tweetMap, self.counter = defaultdict(set), defaultdict(list), 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.counter += 1
        indx = len(self.tweetMap[userId])
        self.tweetMap[userId].append([-self.counter, tweetId, indx, userId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []

        maxHeap = []

        if self.tweetMap[userId]:
            maxHeap.append(self.tweetMap[userId][-1])

        for uId in self.followMap[userId]: 
            if self.tweetMap[uId]:
                maxHeap.append(self.tweetMap[uId][-1])
        
        heapq.heapify(maxHeap)

        while maxHeap and len(res) < 10:
            recent_twt = heapq.heappop(maxHeap)
            res.append(recent_twt[1])
            if recent_twt[2] > 0:
                u_id, indx = recent_twt[3], recent_twt[2]
                heapq.heappush(maxHeap, self.tweetMap[u_id][indx-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
