import pandas as pd

# Data to write
data = {
    "Username": [
        "standard_user",
        "locked_out_user",
        "problem_user",
        "performance_glitch_user",
        "error_user",
        "visual_user",
        "Hello"
    ],
    "Password": ["secret_sauce"] * 7
}

# Create DataFrame
df = pd.DataFrame(data)

# Write to Excel
df.to_excel("users.xlsx", index=False)
