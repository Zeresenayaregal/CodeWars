class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, activity_rank):
        if activity_rank not in range(-8, 9) or activity_rank == 0:
            raise ValueError("Invalid rank")

        d = self.rank_value(activity_rank) - self.rank_value(self.rank)

        if d == 0:
            self.progress += 3
        elif d == -1:
            self.progress += 1
        elif d > 0:
            self.progress += 10 * d * d

        while self.progress >= 100:
            self.progress -= 100
            self.rank = 1 if self.rank == -1 else self.rank + 1
            if self.rank == 8:
                self.progress = 0
                break

    def rank_value(self, r):
        return r + 8 if r > 0 else r + 7
