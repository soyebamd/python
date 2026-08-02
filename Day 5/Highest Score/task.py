student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# Start with 0 as the largest number found so far.
default_num = 0

# Loop through every score in the list.
for score in student_scores:

    # Compare the current largest number with the current score.
    if default_num < score:

        # If the current score is larger,
        # replace the old largest number with the new one.
        default_num = score

        # ---------- Example of how the loop works ----------
        # 1st loop:
        # default_num = 0
        # score = 150
        # 0 < 150  -> True
        # Update default_num to 150

        # 2nd loop:
        # default_num = 150
        # score = 142
        # 150 < 142 -> False
        # No update, default_num stays 150

        # 3rd loop:
        # default_num = 150
        # score = 185
        # 150 < 185 -> True
        # Update default_num to 185

        # 4th loop:
        # default_num = 185
        # score = 120
        # 185 < 120 -> False
        # No update

        # This process continues for every score.
        # Whenever a larger number is found,
        # default_num is updated.

        # Later:
        # default_num = 185
        # score = 199
        # 185 < 199 -> True
        # Update default_num to 199

        # After 199, no larger number exists,
        # so default_num remains 199 until the loop ends.

print("The largest number in student scores is:", default_num)

#opposite find min num ---




minNumber = 1000

for score in student_scores:

    if minNumber > score:

        minNumber = score

print("The smallest number in student scores is:", minNumber)

