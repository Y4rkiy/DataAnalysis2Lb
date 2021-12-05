if __name__ == "__main__":
    res_list = []
    w1, w2, w3, w4 = 0.5, 0.2, 0.3, 0.1
    with open("austin_weather.txt", "r") as file:
        fl = True
        for line in file:
            split_line = line.split(",")
            if fl:
                fl = False
                continue
            daily_income = w1 * float(split_line[1].replace("-", "72")) + w2 * float(
                split_line[2].replace("-", "54")) + w3 * float(split_line[3].replace("-", "10")) \
                           + w4 * float(split_line[4].replace("-", "49"))
            res_list.append((split_line[0], split_line[1], split_line[2], split_line[3], split_line[4].replace("\n", "")
                             , daily_income))

    with open("austin_income.txt", "w") as file:
        print("Date TempAvgFHumidity AvgPercent VisibilityAvgMiles WindAvgMPH DailyIncome", file=file)
        for t in res_list:
            print(f"{t[0]},{t[1]},{t[2]},{t[3]},{t[4]},{t[5]:.1f}", file=file)

    with open("austin_best_income.txt", "w") as file:
        print("Date TempAvgFHumidity AvgPercent VisibilityAvgMiles WindAvgMPH DailyIncome", file=file)
        filtered_list_best = filter(lambda x: x[5] > 61, res_list)
        for t in filtered_list_best:
            print(f"{t[0]},{t[1]},{t[2]},{t[3]},{t[4]},{t[5]:.1f}", file=file)

    with open("austin_worst_income.txt", "w") as file:
        print("Date TempAvgFHumidity AvgPercent VisibilityAvgMiles WindAvgMPH DailyIncome", file=file)
        filtered_list_worst = filter(lambda x: x[5] < 31, res_list)
        for t in filtered_list_worst:
            print(f"{t[0]},{t[1]},{t[2]},{t[3]},{t[4]},{t[5]:.1f}", file=file)
