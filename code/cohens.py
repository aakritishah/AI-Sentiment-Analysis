# imports
import pandas as pd
import numpy as np
from sklearn.metrics import cohen_kappa_score

# defining
codes = ["N", "C", "S", "H", "P", "F", "B", "X"]

# CHANGE THESE PATHS DEPENDING ON MATRIX
groundTruth = "Myers"
ai = "Bing Modal"


# creating matrix
def create_matrix(input_file):
  # read csv
  df = pd.read_csv(input_file)

  # create empty matrix
  matrix = np.zeros((len(codes), len(codes)), dtype=int)

  # create lists to store the ground truth and AI predictions
  ground_truth_values = []
  ai_values = []

  # iterate through rows
  for _, row in df.iterrows():
    groundTruth_code = row[groundTruth]
    ai_code = row[ai]

    if groundTruth_code in codes and ai_code in codes:
      # insert into corresponding position in matrix
      col_index = codes.index(groundTruth_code)  # groundTruth codes are x-axis
      row_index = codes.index(ai_code)  # AI codes are y-axis

      matrix[row_index][col_index] += 1

      # Store the values for Cohen's Kappa calculation
      ground_truth_values.append(groundTruth_code)
      ai_values.append(ai_code)

  kappa = cohen_kappa_score(ground_truth_values, ai_values, labels=codes)
  return matrix, kappa


if __name__ == "__main__":
  input_file = "input.csv"
  matrix, kappa = create_matrix(input_file)
  cell_width = 4

  # print name of matrix
  print("\n" + " " * (cell_width * 3) + groundTruth + " vs " + ai + "\n")

  # print codes
  print(" " * cell_width, end="")
  for code in codes:
    print("%*s" % (cell_width, code), end="")
  print()
  print()

  # print values and calculate row sums
  row_sums = []
  # main diagonal
  main_diagonal_sum = 0
  for i, (row, code) in enumerate(zip(matrix, codes)):
    row_sums.append(sum(row))
    print("%-*s" % (cell_width, code), end="")
    main_diagonal_sum += matrix[i][i]
    for value in row:
      print("%*s" % (cell_width, value), end="")
    print("%*s" % (cell_width, sum(row)))

  print()

  # print main diagonal and matching percentage
  print(f"Matching codes: {main_diagonal_sum}")
  total_codes = sum(row_sums)
  print(
      f"Percentage of matching codes: {main_diagonal_sum / total_codes * 100:.2f}%"
  )

  # print Cohen's Kappa
  print(f"Cohen's Kappa: {kappa:.4f}\n")
