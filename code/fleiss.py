import pandas as pd

# read the csv file into df
df = pd.read_csv('input.csv')

# dictionary to store the code counts
code_counts = {
    'N': [],
    'C': [],
    'S': [],
    'H': [],
    'P': [],
    'F': [],
    'B': [],
    'X': []
}

print("\n")

# CHANGE THESE PATHS DEPENDING ON WHICH RATER
# print("Claude Runs")
print("Bing Runs")
#print("Human Runs")

print(
    f"{'Code':<12}{'N':<6}{'C':<6}{'S':<6}{'H':<6}{'P':<6}{'F':<6}{'B':<6}{'X':<6}"
)
print("\n")

# iterate through all rows
for i in range(len(df)):

  # COMMENT IN AND OUT DEPENDING ON WHICH RATER
  #row = df.iloc[i, 1:4]  # HUMAN 3
  #row = df.iloc[i, 5:12]  # CLAUDE 7
  row = df.iloc[i, 12:19]  # BING 7
  
  code_count = {code: row.tolist().count(code) for code in code_counts.keys()}
  total = sum(code_count.values())
  for code in code_counts.keys():
    code_counts[code].append(code_count[code])

  # print only the first 4 and last 4 rows
  if i < 4 or i >= len(df) - 4:
    print(
        f"{i + 1:<12}{code_count['N']:<6}{code_count['C']:<6}{code_count['S']:<6}{code_count['H']:<6}{code_count['P']:<6}{code_count['F']:<6}{code_count['B']:<6}{code_count['X']:<6}"
    )

# calculate totals for each code for all rows
total_counts = {code: sum(code_counts[code]) for code in code_counts.keys()}

# print the totals
print(
    f"{'Total':<12}{total_counts['N']:<6}{total_counts['C']:<6}{total_counts['S']:<6}{total_counts['H']:<6}{total_counts['P']:<6}{total_counts['F']:<6}{total_counts['B']:<6}{total_counts['X']:<6}"
)
print("\n")