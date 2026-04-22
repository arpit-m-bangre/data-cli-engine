<img width="1536" height="1024" alt="flow" src="https://github.com/user-attachments/assets/ffe79c63-ca87-49e3-b163-a5def0657ec4" />
<img width="1920" height="1100" alt="1" src="https://github.com/user-attachments/assets/5ce10d43-50e2-41bf-8439-9691f500bf6a" />
<img width="1920" height="1100" alt="2" src="https://github.com/user-attachments/assets/e9e74ee1-8c75-4d53-adf7-0fbbd33a98aa" />
<img width="1920" height="1100" alt="3" src="https://github.com/user-attachments/assets/1789e9d6-fd5c-4ca0-8255-a27601b28f02" />
<img width="1920" height="1100" alt="4" src="https://github.com/user-attachments/assets/6a9dbfc1-26f8-4e29-ab79-c7d24820bed7" />

🚀 DataCLI — Mini SQL Engine in Python
A command-line data processing tool built using pure Python (no external libraries).
This project simulates basic SQL-like operations such as filtering, sorting, grouping, and querying CSV data.

💡 Features
Load CSV data
Filter data (filter column=value)
Group data (groupby column)
Sort data (sort column asc/desc)
SQL-like queries:
SELECT * WHERE column=value
SELECT * WHERE column=value SORT BY column DESC
Save processed data to CSV
Reset dataset
Interactive CLI interface
Clean tabular output UI

🧠 Why this project?
Most data projects rely on libraries like pandas.
This project was built to understand:
How data processing works internally
How query systems like SQL are implemented
How CLI tools are designed

🛠 Tech Stack
Python (core only)
File handling
Lists & dictionaries
CLI input/output

▶️ How to Run
python main.py


🧪 Example Usage
>> load data.csv
>> summary
>> filter region=West
>> groupby category
>> sort sales desc
>> SELECT * WHERE region=West SORT BY sales DESC
>> save output.csv


📂 Project Structure
main.py → CLI interface
data_loader.py → CSV loader
operations.py → data operations
sql_parser.py → query parsing & execution

🚀 Future Improvements
AND conditions in SQL
Select specific columns
Better query language
Web UI version

🙌 Author
Built by Arpit




