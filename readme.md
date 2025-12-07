# Learning PySpark

A hands-on repository for learning Apache Spark with Python (PySpark) using the MovieLens 100k dataset. This project demonstrates basic PySpark operations including data loading, transformations, and aggregations.

## 📋 Prerequisites

- Python 3.x (Tested with Python 3.12)
- pip (Python package manager)
- Basic understanding of Python
- Terminal/Command line familiarity

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/desininja/LearningPySpark.git
cd LearningPySpark
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
```

### 3. Activate Virtual Environment
**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

You should see `(venv)` appear at the beginning of your terminal prompt.

### 4. Install PySpark
```bash
pip install --upgrade pip
pip install pyspark
```

### 5. Verify Installation
```bash
python -c "import pyspark; print('PySpark version:', pyspark.__version__)"
```

If successful, this will display your PySpark version (e.g., 4.0.1).

## 📊 Dataset Information

This project uses the **MovieLens 100k dataset**, which contains 100,000 ratings from 943 users on 1,682 movies. Each user has rated at least 20 movies.

### Key Dataset Files

#### **u.data**
The full dataset with 100,000 ratings. Tab-separated format:
```
user id | item id | rating | timestamp
```
- Timestamps are Unix seconds since 1/1/1970 UTC
- Data is randomly ordered

#### **u.item**
Information about movies. Tab-separated format:
```
movie id | movie title | release date | video release date | IMDb URL | [19 genre fields]
```
- Last 19 fields are binary genre indicators (1 = movie belongs to genre, 0 = doesn't)
- Movies can belong to multiple genres

#### **u.user**
Demographic information about users. Tab-separated format:
```
user id | age | gender | occupation | zip code
```

#### **u.genre**
List of all available movie genres.

#### **u.occupation**
List of all user occupations.

#### **u.info**
Summary statistics: number of users, items, and ratings.

### Training/Test Splits

**5-Fold Cross Validation (u1-u5):**
- `u1.base` / `u1.test` through `u5.base` / `u5.test`
- 80%/20% splits with disjoint test sets
- Generated from u.data by mku.sh

**User-Based Splits (ua/ub):**
- `ua.base` / `ua.test` and `ub.base` / `ub.test`
- Exactly 10 ratings per user in test sets
- ua.test and ub.test are disjoint

### Utility Scripts
- **allbut.pl** - Generates training/test sets with all but n ratings per user
- **mku.sh** - Shell script to generate all u data sets from u.data
- **ml-data.tar.gz** - Compressed archive (rebuild with: `gunzip ml-data.tar.gz && tar xvf ml-data.tar`)

## 📝 Python Scripts

### 1. ratings-histogram.py

**Purpose:** Analyze the distribution of movie ratings across the dataset.

**What it does:**
- Loads the MovieLens ratings data
- Counts how many times each rating (1-5) appears
- Displays results sorted by rating value

**How to run:**
```bash
source venv/bin/activate
python ratings-histogram.py
```

**Expected Output:**
```
Rating Count
1      6110
2      11370
3      27145
4      34174
5      21201
```

**Key PySpark Concepts Demonstrated:**
- `textFile()` - Loading data from files
- `map()` - Transforming data
- `countByValue()` - Aggregating data
- Working with dictionaries in Python

---

### 2. PopularMovies.py

**Purpose:** Find and rank movies by their popularity (number of ratings received).

**What it does:**
- Loads movie names and ratings data
- Counts how many ratings each movie received
- Sorts movies by popularity (number of ratings)
- Displays all movies from least to most popular

**How to run:**
```bash
source venv/bin/activate
python PopularMovies.py
```

**Expected Output:**
```
('Movie Title 1', 1)
('Movie Title 2', 2)
...
('Star Wars (1977)', 583)
```

**Key PySpark Concepts Demonstrated:**
- `broadcast()` - Broadcasting variables to all nodes
- `map()` - Data transformation
- `reduceByKey()` - Aggregation by key
- `sortByKey()` - Sorting data
- `collect()` - Bringing results to driver

**Note:** The script has a minor bug - it looks for `u.ITEM` (uppercase) but the file is `u.item` (lowercase). This may cause an error on case-sensitive file systems.

---

## 💻 Usage Examples

### Running Scripts

1. **Activate virtual environment:**
   ```bash
   source venv/bin/activate
   ```

2. **Run a script:**
   ```bash
   python ratings-histogram.py
   ```
   or
   ```bash
   python PopularMovies.py
   ```

3. **Deactivate when done:**
   ```bash
   deactivate
   ```

### Common PySpark Patterns Used

**Loading Data:**
```python
lines = sc.textFile("ml-100k/u.data")
```

**Parsing and Transforming:**
```python
ratings = lines.map(lambda x: x.split()[2])
```

**Aggregating:**
```python
result = ratings.countByValue()
movieCounts = movies.reduceByKey(lambda x, y: x + y)
```

**Sorting:**
```python
sortedMovies = flipped.sortByKey()
```

## 🔧 Troubleshooting

### Common Issues

**Issue:** `ModuleNotFoundError: No module named 'pyspark'`
- **Solution:** Make sure virtual environment is activated and PySpark is installed

**Issue:** `FileNotFoundError: [Errno 2] No such file or directory: 'ml-100k/u.data'`
- **Solution:** Ensure you're running scripts from the project root directory

**Issue:** `AttributeError: 'dict' object has no attribute 'take'`
- **Solution:** This was an issue in older versions of ratings-histogram.py - `countByValue()` returns a dict, not an RDD

## 📚 Learning Resources

### Official Documentation
- [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/)
- [PySpark SQL Documentation](https://spark.apache.org/docs/latest/sql-programming-guide.html)

### Key Concepts to Learn
1. **RDD Operations:** Transformations vs Actions
2. **Lazy Evaluation:** How Spark optimizes execution
3. **Key-Value Pairs:** Working with paired RDDs
4. **Broadcasting:** Efficiently sharing read-only data
5. **Avoid `.collect()`:** Use `.take()`, `.show()`, or `.write()` for large datasets

### Alternative Actions to `.collect()`
- `.take(n)` - Get first n rows
- `.show(n)` - Display formatted output
- `.count()` - Count rows only
- `.first()` - Get first row
- `.write.csv()` / `.write.parquet()` - Save to file

## 📄 License

This project includes the MovieLens 100k dataset, which has its own usage terms. Please refer to the LICENSE file for details.

## 🤝 Contributing

Feel free to fork this repository and add your own PySpark learning examples!

---

**Happy Learning! 🚀**