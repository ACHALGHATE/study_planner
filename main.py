import pickle
import numpy as np
import pandas as pd

with open("model/model.pkl", "rb") as file:
    model = pickle.load(file)

print("=" * 45)
print("        AI SMART STUDY PLANNER")
print("=" * 45)

while True:
    try:
        print("\nEnter your details:\n")

        study_hours = int(input("Study hours      : "))
        sleep_hours = int(input("Sleep hours      : "))
        screen_time = int(input("Screen time      : "))
        difficulty = int(input("Difficulty (1-10) : "))

        data = pd.DataFrame(
            [[study_hours, sleep_hours, screen_time, difficulty]],
            columns=["study_hours", "sleep_hours", "screen_time", "difficulty"]
        )

        prediction = model.predict(data)[0]

        print("\n" + "-" * 45)
        print("Result\n")

        if prediction == 0:
            print("Stress Level : Low")
            print("Suggestion   : You can increase study time and stay consistent.")

        elif prediction == 1:
            print("Stress Level : Medium")
            print("Suggestion   : Try to balance study and breaks.")

        else:
            print("Stress Level : High")
            print("Suggestion   : Reduce workload and take proper rest.")

        print("-" * 45)

        again = input("\nDo you want to check again? (yes/no): ").strip().lower()

        if again != "yes":
            print("\nThank you for using the planner.\n")
            break

    except:
        print("\nInvalid input. Please enter numbers only.\n")