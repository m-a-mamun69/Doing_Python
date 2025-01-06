# Select a Secure Random Element from a List.
import secrets

participants = ["Mamun", "Rashid", "Jim", "Hasan"]

winner = secrets.choice(participants)
print("Winner: ", winner)