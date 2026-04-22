def load_csv(filename):
    data = []

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        # check empty file
        if not lines:
            print("❌ File is empty")
            return []

        # get headers
        headers = [h.strip() for h in lines[0].split(",")]

        # process rows
        for line in lines[1:]:
            line = line.strip()

            # skip empty lines
            if not line:
                continue

            values = [v.strip() for v in line.split(",")]

            # skip invalid rows
            if len(values) != len(headers):
                print(f"⚠️ Skipping invalid row: {line}")
                continue

            row = {}
            for i in range(len(headers)):
                row[headers[i]] = values[i]

            data.append(row)

        return data

    except FileNotFoundError:
        print("❌ File not found")
        return []

    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return []