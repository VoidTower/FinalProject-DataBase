import matplotlib.pyplot as plt
from connect_database import session

session.set_keyspace("netflix_keyspace")

# 1. Top 10 countries
rows = session.execute("SELECT * FROM top_countries")
countries = []
counts = []
for row in rows:
    countries.append(row.country)
    counts.append(row.count)

plt.figure(figsize=(10, 6))
plt.barh(countries, counts, color='skyblue')
plt.title("Top 10 Countries by Number of Developers")
plt.xlabel("Number of Developers")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("output/top_countries.png")
plt.show()

# 2. Education distribution
rows = session.execute("SELECT * FROM education_distribution")
education = []
counts = []
for row in rows:
    education.append(row.education[:30])  # truncate for readability
    counts.append(row.count)

plt.figure(figsize=(10, 6))
plt.barh(education, counts, color='orange')
plt.title("Education Level Distribution")
plt.xlabel("Number of Developers")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("output/education_distribution.png")
plt.show()

# 3. Open Source by Company Size
rows = session.execute("SELECT * FROM opensource_by_company")
sizes = []
counts = []
for row in rows:
    sizes.append(row.companysize)
    counts.append(row.count)

plt.figure(figsize=(10, 6))
plt.pie(counts, labels=sizes, autopct='%1.1f%%', startangle=140)
plt.title("Open Source Contributors by Company Size")
plt.tight_layout()
plt.savefig("output/opensource_by_company.png")
plt.show()