from random import randint
import numpy as np



possible_responses = [
    "Hi, how are you?",
    "You are amazing",
    "I'm sure you will be fine, you are so intelligent!",
    "I love you",
    "Can we get married?"
]

how_many = 4
top_k_robots = 2
how_many_responses = len(possible_responses)

def generate_new() -> np.ndarray:
    robots = np.random.randint(0, how_many_responses, size=(how_many, how_many_responses))
    return robots


def mutate(robot):
    idx = randint(0, how_many_responses - 1)
    robot[idx] = randint(0, how_many_responses - 1)
    return robot


def repopulate(best_robots):
    robots = np.zeros((how_many, how_many_responses))
    # copy best performers
    for i in range(top_k_robots):
        robots[i] = best_robots[i][0]

    for i in range(how_many - top_k_robots):
        robots[top_k_robots + i] = mutate(best_robots[i % top_k_robots][0])

    return robots

def test(robots):
    scores = []
    for i in range(how_many):
        robot = robots[i]
        print("Next converstation")
        for index in robot:
            my_text = input("You say: ")
            if my_text == "x":
                break
            print(possible_responses[index])
        rating = int(input("Rate: "))
        scores.append([robot, rating])

    return scores

def main():
    print("Super Advanced ChatBot")
    robots = generate_new()
    while True:
        print("New generation")
        print(robots)

        # test
        scores = test(robots)
        
        # sort and get top robots
        scores = sorted(scores, key=lambda pair:pair[1], reverse=True)

        # stop if satisfactory
        if scores[0][1] == 100:
            print("Your dream waifu robot is:")
            print(scores[0][0])
            return

        # generate new population
        robots = repopulate(scores[0:top_k_robots])

if __name__ == "__main__":
    main()

