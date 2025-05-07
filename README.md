# FinalProject-DataBase 

A data engineering and analytics project using **Apache Cassandra (DataStax Astra)** to store, clean, analyze, and visualize developer survey data.

---

## Project Structure
.
├── Big_Data/
│ ├── initial_analysis.ipynb
│ ├── adjust_data.ipynb
│ └── survey_results_public_100k.csv
├── cleaned_stackoverflow.csv
├── survey_results_public.csv
├── create_table.py
├── load_data.py
├── clean_data.py
├── connect_database.py
├── aggregate_data.py
├── visualize.py
├── output/
│ ├── education_distribution.png
│ ├── opensource_by_company.png
│ └── top_countries.png


---

## Features

- Clean raw Stack Overflow survey data
- Load cleaned data into **Cassandra** using batch inserts
- Create Bronze (raw), Silver (cleaned), and Gold (aggregated) data layers
- Generate visualizations for quick insights
- Use **DataStax Astra DB** as scalable NoSQL backend

---

##  Data Layers

| Layer | Contents | Example |
|-------|----------|---------|
| 🥉 Bronze | Raw CSV files | `survey_results_public.csv` |
| 🥈 Silver | Cleaned tables in Cassandra | `developer_survey` |
| 🥇 Gold | Aggregated tables & charts | `top_countries`, `education_distribution`, `opensource_by_company` |

---

## How to Run
### 1. Install Dependencies

```bash
pip install -r requirements.txt
Make sure you have Python 3.8+ and a virtual environment set up.

2.  Clean the Data
bash

Copy
python clean_data.py
This creates cleaned_stackoverflow.csv from the raw dataset.

3. Connect to Astra DB
Ensure your Secure Connect Bundle is placed under secure-connect-netflix-project/.

bash

Copy
python connect_database.py
4. 🗄️ Create Tables
bash

Copy
python create_table.py
5. 📥 Load Data into Cassandra
bash

Copy
python load_data.py
This loads 100k+ cleaned records into the developer_survey table.

6. 📊 Generate Aggregates (Gold Layer)
bash

Copy
python aggregate_data.py
7. 📈 Run Visualizations
bash

Copy
python visualize.py
Visualizations are saved in the output/ folder.

Sample Visualizations
- output/top_countries.png
- output/opensource_by_company.png
- output/education_distribution.png


Technologies Used:
Python 
Apache Cassandra (Astra DB) 
Pandas / Matplotlib / Seaborn 
Git + GitHub 
Author
Tanjil Hossain (VoidTower)
GitHub: @VoidTower

📄 License
This project is open source under the MIT License.

