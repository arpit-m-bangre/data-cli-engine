# ---------------------------
# SUMMARY
# ---------------------------
def summary(data):
    if not data:
        print("❌ No data available")
        return

    total = 0

    for row in data:
        try:
            total += int(row["sales"])
        except:
            print("⚠️ Skipping invalid sales value")
            continue

    count = len(data)
    avg = total / count if count > 0 else 0

    print("\n📊 SUMMARY")
    print("--------------------")
    print(f"Total Sales     : {total}")
    print(f"Average Sales   : {round(avg, 2)}")
    print(f"Records         : {count}")
    print("--------------------\n")


# ---------------------------
# FILTER
# ---------------------------
def filter_data(data, key, value):
    if not data:
        print("❌ No data available")
        return []

    if key not in data[0]:
        print("❌ Invalid column")
        return []

    result = []

    for row in data:
        if row[key].lower() == value.lower():
            result.append(row)

    return result


# ---------------------------
# GROUP BY
# ---------------------------
def group_by(data, key):
    if not data:
        print("❌ No data available")
        return {}

    if key not in data[0]:
        print("❌ Invalid column")
        return {}

    result = {}

    for row in data:
        group_value = row[key]

        if group_value not in result:
            result[group_value] = 0

        try:
            result[group_value] += int(row["sales"])
        except:
            print("⚠️ Skipping invalid sales value")

    return result


# ---------------------------
# SORT
# ---------------------------
def sort_data(data, key, reverse=False):
    if not data:
        print("❌ No data available")
        return None

    if key not in data[0]:
        print("❌ Invalid column")
        return None

    try:
        return sorted(data, key=lambda row: int(row[key]), reverse=reverse)
    except:
        print("❌ Cannot sort this column (not numeric)")
        return None


# ---------------------------
# SAVE CSV
# ---------------------------
def save_csv(data, filename):
    if not data:
        print("❌ No data to save")
        return

    try:
        with open(filename, "w") as f:
            headers = list(data[0].keys())
            f.write(",".join(headers) + "\n")

            for row in data:
                values = []
                for h in headers:
                    values.append(row[h])
                f.write(",".join(values) + "\n")

        print(f"✅ Data saved to '{filename}' successfully!")

    except:
        print("❌ Error saving file")