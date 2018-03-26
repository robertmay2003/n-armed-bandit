import numpy as np

class Bandit:
    def __init__(self, arms):
        self.arms = arms
    def reward(self, arm):
        return(np.random.rand() < self.arms[arm])

class Fella:
    def __init__(self, arms_count):
        self.estimates = [0.5 for arm in range(arms_count)]
    def policy(self, bandit):
        # This is how you will make your guess
        choice = np.random.randint(0, len(bandit.arms))
        reward = bandit.reward(choice)
        self.update_estimates(choice, reward)
        return(reward)
    def update_estimates(self, choice, reward):
        self.estimates = self.estimates
        # This is how you will update your estimates

class Session:
    def __init__(self, rounds, pulls, arms):
        self.rounds = rounds
        self.pulls  = pulls
        self.bandits = arms
        self.wins = 0
    def play(self):
        for arms in self.bandits:
            bandit = Bandit(arms)
            fella = Fella(len(arms))
            for pull in range(self.pulls):
                reward = fella.policy(bandit)
                if reward:
                    self.wins += 1
        return(self.wins / self.pulls)

def avg_arms(arms):
    avg1 = 0
    avg2 = 0
    for arm in arms:
        avg1 += arm[0]
        avg2 += arm[1]
    avg1 /= 500
    avg2 /= 500
    print(avg1, avg2)

def main():
    arms = np.random.rand(500, 2)
    avg_arms(arms)
    session = Session(100, 500, arms)
    results = session.play()
    print(results)

if __name__ == "__main__":
    main()
