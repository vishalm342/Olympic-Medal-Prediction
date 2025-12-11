# 🏅 Olympic Medal Prediction

A machine learning project that predicts the number of Olympic medals a country will win based on historical data and team characteristics.

## 📊 Project Overview

This project uses historical Olympic data to predict medal counts for participating countries. By analyzing factors such as the number of athletes, average age of the team, and previous medal performance, we build a predictive model using linear regression. 

## 🎯 Hypothesis

**We can predict how many medals a country will win at the Olympics by using historical data.**

This prediction is based on analyzing key factors that correlate with medal success across different Olympic games. 

## 📁 Dataset

The project uses the `teams. csv` dataset containing historical Olympic team data with the following features: 

- **team**:  Country code (e.g., USA, CHN, GBR)
- **country**: Full country name
- **year**: Olympic year
- **athletes**: Number of athletes on the team
- **age**: Average age of athletes
- **medals**: Total medals won (target variable)
- **prev_medals**:  Medals won in previous Olympics

**Dataset size**:  2,144 rows covering multiple Olympic games from 1964 to 2016

## 🔍 Exploratory Data Analysis

### Key Findings

1. **Strong correlations identified:**
   - **athletes ↔ medals**: 0.84 (strong positive correlation)
   - **prev_medals ↔ medals**:  0.92 (very strong positive correlation)
   - **age ↔ medals**: 0.025 (weak correlation)
   - **year ↔ medals**: -0.022 (negligible correlation)

2. **Distribution insights:**
   - Medal distribution is heavily right-skewed (most teams win 0-5 medals)
   - The number of athletes and previous medals are the best predictors

### Visualizations Included

- Scatter plots with regression lines for athletes, previous medals, and age vs.  medals
- Medal distribution histogram showing frequency patterns

## 🛠️ Data Preprocessing

1. **Feature selection**:  Kept only relevant columns (team, country, year, athletes, age, medals, prev_medals)
2. **Handling missing values**: Removed 130 rows containing NaN values (countries with no previous Olympic data)
3. **Train-test split**: 
   - Training set: Years < 2012 (1,609 rows)
   - Test set: Years ≥ 2012 (405 rows)

## 🤖 Machine Learning Model

### Model Selection
**Linear Regression** - chosen due to the linear relationships identified in the correlation analysis

### Features Used for Prediction
- `athletes`: Number of athletes on the team
- `prev_medals`: Medals won in previous Olympics

### Model Performance
- **Mean Absolute Error (MAE)**: 3.30 medals
- **Model successfully captured the relationship** between team characteristics and medal outcomes

### Key Insights
- Previous medal success is the strongest predictor (coefficient:  ~0.87)
- Team size also contributes significantly to predictions
- The model performs reasonably well given the complexity of Olympic competition

## 📈 Results

The model achieved a Mean Absolute Error of 3.30 medals, meaning on average, predictions are within ±3.3 medals of the actual count.  This is a reasonable error margin considering: 
- Unpredictable factors (injuries, unexpected performances)
- variability in Olympic competitions
- Different sports mix for each country

## 📝 Requirements

```
pandas
numpy
scikit-learn
matplotlib
seaborn
jupyter
```

## 🚀 Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/visually342/Olympic-Medal-Prediction. git
   cd Olympic-medal-prediction
   ```

2. **Install dependencies**
   ```bash
   pip install pandas numpy scikit-learn matplotlib seabokrn jupyter
   ```

3. **Run the notebook**
   ```bash
   jupyter notebook Athletes. ipynb
   ```

4. **view the project documentation**
   ```bash
   python notebook_viewer.py
   ```
   Then open your browser to `http://localhost:8000`

## 📂 Project Structure

```
Olympic-Medal-Prediction/
├── README. md                 # Project documentation
├── Athletes.ipynb            # Main Jupyter notebook with analysis
├── teams.csv                 # Olympic teams historical data
└── notebook_viewer.py        # HTML viewer for notebook (optional)
```

## 🎓 Key Learnings

1. **Feature engineering matters**: Previous performance is highly predictive
2. **Data quality is crucial**:  Handling missing values appropriately improves model reliability
3. **domain knowledge helps**: Understanding Olympic competition dynamics aids in feature selection
4. **simple models can be effective**: Linear regression provided good results despite its simplicity

## 🔮 Future Improvements

- [ ] Include more features (GDP, population, sports budget)
- [ ] Try advanced models (Random Forest, Gradient Boosting)
- [ ] Analyze individual sport categories
- [ ] Incorporate home advantage factor
- [ ] Add country-specific trends over time

## 📄 License

This project is open source and available for educational purposes.

## 👤 Author

**vishalm342**
- GitHub: [@vishalm342](https://github.com/vishalm342)

---

⭐ If you found this project helpful, please give it a star! 
```
