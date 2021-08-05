import pandas as pd
import statistics

df = pd.read_csv("data.csv")

math_score_list = df["math score"].to_list()

math_mean = statistics.mean(math_score_list)
print("The mean of this data set is :" , math_mean)

math_median = statistics.median(math_score_list)
print("The median of this data set is :" , math_median)

math_mode = statistics.mode(math_score_list)
print("The mode of this data set is :" , math_mode)

math_stdev = statistics.stdev(math_score_list)
print("The standard deviation of this data set is :" , math_stdev)

math_1st_std_dev_start = (math_mean - math_stdev)

math_1st_std_dev_end = (math_mean + math_stdev)

math_2nd_std_dev_start = (math_mean - (math_stdev*2))

math_2nd_std_dev_end = (math_mean + (math_stdev*2))

math_3rd_std_dev_start = (math_mean - (math_stdev*3))

math_3rd_std_dev_end = (math_mean + (math_stdev*3))

math_score_listOfData_within_1st_stdev = [result for result in math_score_list if result > math_1st_std_dev_start and result < math_1st_std_dev_end]

math_score_listOfData_within_2nd_stdev = [result for result in math_score_list if result > math_2nd_std_dev_start and result < math_2nd_std_dev_end]

math_score_listOfData_within_3rd_stdev = [result for result in math_score_list if result > math_3rd_std_dev_start and result < math_3rd_std_dev_end]

math_percentageOfData_within_1st_stdev = len(math_score_listOfData_within_1st_stdev)*100 / len(math_score_list)
print(math_percentageOfData_within_1st_stdev ,"%")

math_percentageOfData_within_2nd_stdev = len(math_score_listOfData_within_2nd_stdev)*100 / len(math_score_list)
print(math_percentageOfData_within_2nd_stdev ,"%")

math_percentageOfData_within_3rd_stdev = len(math_score_listOfData_within_3rd_stdev)*100 / len(math_score_list)
print(math_percentageOfData_within_3rd_stdev ,"%")