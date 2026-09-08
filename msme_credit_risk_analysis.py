
# Chain Forward - Financial Risk Model

import pandas as pd
import numpy as np
#Lets start by assigning variables we might need when building the financial model, since not all the numbers are given we will create assumptions which can be tweaked.
# 1. BASE CASE ASSUMPTIONS

ACTIVE_BORROWERS = 20_000
INTEREST_INCOME_PER_BORROWER = 8
AVERAGE_EAD = 100
DEFAULT_RATE = 0.06
LGD = 0.50
INITIAL_INVESTMENT = 4_500_000
ANALYSIS_MONTHS = 36

# Calculating the numbers
# 2. BASE CASE FINANCIAL MODEL
#Interest earned per month
monthly_interest_income = (ACTIVE_BORROWERS * INTEREST_INCOME_PER_BORROWER)
# Amount that could be lost incase of default
total_exposure = ACTIVE_BORROWERS * AVERAGE_EAD
# Presumed loss per month
monthly_expected_loss = (DEFAULT_RATE * LGD * total_exposure)
#Difference between interest and loss
monthly_contribution = (monthly_interest_income - monthly_expected_loss)
# Yearly projection
annual_contribution = monthly_contribution * 12
# Contribution after predicted number of years
three_year_contribution = (monthly_contribution * ANALYSIS_MONTHS)
#Difference betwen the total contribution and the initial investment
three_year_net_return = (three_year_contribution - INITIAL_INVESTMENT)
# Return on investment after 3 years
three_year_roi = (three_year_net_return / INITIAL_INVESTMENT)
# Number of months needed to full repay the given initial investment
payback_period_months = (    INITIAL_INVESTMENT / monthly_contribution)


print("BASE CASE")
print(f"Monthly interest income: ${monthly_interest_income:,.2f}")
print(f"Total borrower exposure: ${total_exposure:,.2f}")
print(f"Monthly expected credit loss: ${monthly_expected_loss:,.2f}")
print(f"Monthly contribution after credit losses: ${monthly_contribution:,.2f}")
print(f"Annual contribution: ${annual_contribution:,.2f}")
print(f"3-year contribution: ${three_year_contribution:,.2f}")
print(f"3-year net return: ${three_year_net_return:,.2f}")
print(f"3-year ROI: {three_year_roi:.2%}")
print(f"Estimated payback period: {payback_period_months:.1f} months")


# 3. SCENARIO ANALYSIS
# Lets build the 3 scenarios to map out different interst_incomes,default rate and lgd
scenarios = {
    "Optimistic": {
        "borrowers": 22_000,
        "interest_income": 9,
        "default_rate": 0.04,
        "lgd": 0.40
    },

    "Base": {
        "borrowers": 20_000,
        "interest_income": 8,
        "default_rate": 0.06,
        "lgd": 0.50
    },

    "Pessimistic": {
        "borrowers": 18_000,
        "interest_income": 7,
        "default_rate": 0.10,
        "lgd": 0.60
    }
}


scenario_results = []
# For loop to run every variable from each scenario  and generate results
for scenario, assumptions in scenarios.items():

    borrowers = assumptions["borrowers"]
    interest_income = assumptions["interest_income"]
    default_rate = assumptions["default_rate"]
    lgd = assumptions["lgd"]
#Calculating the numbers from the different scenarios
    revenue = borrowers * interest_income

    exposure = borrowers * AVERAGE_EAD

    expected_loss = (default_rate * lgd * exposure)

    contribution = revenue - expected_loss

    annual_contribution = contribution * 12

    three_year_contribution = ( contribution * ANALYSIS_MONTHS)

    net_return = (three_year_contribution - INITIAL_INVESTMENT)

    roi = net_return / INITIAL_INVESTMENT

    payback_months = (
        INITIAL_INVESTMENT / contribution
        if contribution > 0
        else np.inf
    )
# Addint the new generated numbers to the list
    scenario_results.append({
        "Scenario": scenario,
        "Borrowers": borrowers,
        "Monthly Revenue": revenue,
        "Exposure": exposure,
        "Default Rate": default_rate,
        "LGD": lgd,
        "Expected Loss": expected_loss,
        "Monthly Contribution": contribution,
        "Annual Contribution": annual_contribution,
        "3-Year Contribution": three_year_contribution,
        "3-Year Net Return": net_return,
        "3-Year ROI": roi,
        "Payback Months": payback_months
    })

# Creating a a dataframe with all the new numbers
scenario_df = pd.DataFrame(scenario_results)

print("\nSCENARIO ANALYSIS")
print(scenario_df.round(2))


# 4. DEFAULT RATE SENSITIVITY
#Lets create default rates ranging from 1% to 20% with a step sive of 1
default_rates = np.arange(0.01, 0.201, 0.01)

sensitivity_results = []
#Running the different defualt rate percentages to see the nubers at each given percentage rate
for rate in default_rates:

    expected_loss = (
        rate * LGD * total_exposure
    )

    contribution = (
        monthly_interest_income - expected_loss
    )

    annual_contribution = contribution * 12
#Adding all the numbers to the list
    sensitivity_results.append({
        "Default Rate": rate,
        "Monthly Expected Loss": expected_loss,
        "Monthly Contribution": contribution,
        "Annual Contribution": annual_contribution
    })

#Creating a dataframe to the store the different default rates data
sensitivity_df = pd.DataFrame(sensitivity_results)

print("\nDEFAULT RATE SENSITIVITY")
print("-" * 40)
print(sensitivity_df.round(2))


# 5. CREDIT-LOSS-ONLY BREAK-EVEN DEFAULT RATE
#Getting the number at which the company breaks even,this number might reduce as we havent put into consideration other costs like operating costs
break_even_default_rate = (
    monthly_interest_income /
    (LGD * total_exposure)
)

print("\nBREAK-EVEN ANALYSIS")
print(
    f"Credit-loss-only break-even default rate: "
    f"{break_even_default_rate:.2%}"
)

# The assessment does not provide transaction-level data.
# Synthetic transaction data is generated to demonstrate  customer segmentation .

# 6. CUSTOMER SEGMENTATION

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

np.random.seed(42)

# Generate synthetic MSME transaction data

np.random.seed(42)
#Assigning the number of customers we need generated
n_customers = 1000

transactions_list = []
#Creating a loop to go through all the customers
for customer_id in range(1, n_customers + 1):

    # Different MSMEs have different transaction frequencies
    # Randomly assign a transaction count between 5 and 50 for the current customer
    n_transactions = np.random.randint(5, 51)
   # Generate realistic transaction values using a log-normal distribution
    amounts = np.random.lognormal(
        mean=7,
        sigma=1,
        size=n_transactions
    )
    # Randomly assign transaction categories based on pre-defined probability weights (45% inflows, 45% outflows, 10% loan repayments)
    transaction_types = np.random.choice(
        ["inflow", "outflow", "repayment"],
        size=n_transactions,
        p=[0.45, 0.45, 0.10]
    )
    # Combine the generated data arrays into a temporary DataFrame for this specific customer
    customer_transactions = pd.DataFrame({
        "customer_id": customer_id,
        "transaction_amount": amounts,
        "transaction_type": transaction_types
    })
 # Add the customer data into a list
    transactions_list.append(customer_transactions)

#Combine all the data into one data frame
transactions = pd.concat(
    transactions_list,
    ignore_index=True
)

print("\nSYNTHETIC TRANSACTION DATA")
print(f"Number of customers: {transactions['customer_id'].nunique():,}")
print(f"Number of transactions: {len(transactions):,}")
print(transactions.head())

# Create customer-level behavioral features

# Group the dataset by customer and calculate behavioral financial features
customer_features = transactions.groupby("customer_id").agg(
    transaction_frequency=("transaction_amount", "count"),
    avg_transaction_amount=("transaction_amount", "mean"),
    monthly_transaction_volume=("transaction_amount", "sum"),
    cash_flow_volatility=("transaction_amount", "std")
).reset_index()


# Calculate repayment ratio
# 1. Sum up all credit loan repayments made by each individual customer
repayment_amount = (
    transactions[
        transactions["transaction_type"] == "repayment"
    ]
    .groupby("customer_id")["transaction_amount"]
    .sum()
)

# 2. Sum up all money leaving the account (regular business expenses + debt repayments)
total_outflow = (
    transactions[
        transactions["transaction_type"].isin(
            ["outflow", "repayment"]
        )
    ]
    .groupby("customer_id")["transaction_amount"]
    .sum()
)

# 3. Calculate what percentage of total money leaving the business goes toward paying off debt

customer_features["repayment_ratio"] = (
    customer_features["customer_id"]
    .map(repayment_amount)
    .fillna(0)
    /
    customer_features["customer_id"]
    .map(total_outflow)
    .fillna(1)
)


# Replace any missing volatility values
customer_features["cash_flow_volatility"] = (
    customer_features["cash_flow_volatility"]
    .fillna(0)
)


print("\nCUSTOMER FEATURES")
print(customer_features.head())

# Define the specific list of numerical variables to use for customer segmentation

features_for_clustering = [
    "transaction_frequency",
    "avg_transaction_amount",
    "monthly_transaction_volume",
    "cash_flow_volatility",
    "repayment_ratio"
]
# Initialize the standardizer to scale data to a mean of 0 and variance of 1

scaler = StandardScaler()

# Compute column means/standard deviations, scale the data, and output a clean NumPy array
X_scaled = scaler.fit_transform(
    customer_features[features_for_clustering]
)

# K-Means clustering
#  Initialize K-Means to find 3 distinct groups and running the algorithm 10 times with different starting seeds to find the best fit.


kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Fit the model to the scaled data and immediately assign a cluster label (0, 1, or 2) to each customer.
customer_features["cluster"] = kmeans.fit_predict(X_scaled)

print("\nCLUSTER COUNTS")
print(customer_features["cluster"].value_counts())

# Group the finalized customer profiles by their assigned cluster label

cluster_profile = (
    customer_features
    .groupby("cluster")[features_for_clustering]
    .mean()
    .round(2)
)

print("\nCLUSTER PROFILE")
print(cluster_profile)

#  Calculate a raw behavioral risk score for each customer.

# Risk increases (+) with higher cash flow instability.
# Risk decreases (-) when a business transacts frequently or maintains a high loan repayment ratio.

customer_features["risk_score"] = (
    -customer_features["transaction_frequency"]
    + customer_features["cash_flow_volatility"]
    - customer_features["repayment_ratio"]
)

#  Group the data by cluster to find the average risk score for each segment,
# then sort them in ascending order (from safest/lowest risk to riskiest/highest risk).

cluster_risk = (
    customer_features
    .groupby("cluster")["risk_score"]
    .mean()
    .sort_values()
)

print("\nCLUSTER RISK RANKING")
print("-" * 40)
print(cluster_risk)

# Lowest risk score = lower behavioral risk
# Highest risk score = higher behavioral risk

# Extract the sorted list of cluster IDs from your risk ranking
risk_order = cluster_risk.index.tolist()

#Map the relative positions in the sorted list to meaningful descriptive credit profiles
risk_labels = {
    risk_order[0]: "Lower activity, relatively stable",
    risk_order[1]: "High activity/volume, moderate volatility",
    risk_order[2]: "Higher-value but highly volatile"
}
# Create a final descriptive risk segment column by applying the label dictionary to each customer's cluster ID

customer_features["risk_segment"] = (
    customer_features["cluster"]
    .map(risk_labels)
)

print("\nCUSTOMER SEGMENTS")
print(
    customer_features[
        ["customer_id", "cluster", "risk_segment"]
    ].head(10)
)

# Visualize customer segments


import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))

for cluster in sorted(customer_features["cluster"].unique()):

    cluster_data = customer_features[
        customer_features["cluster"] == cluster
    ]

    plt.scatter(
        cluster_data["monthly_transaction_volume"],
        cluster_data["cash_flow_volatility"],
        label=f"Cluster {cluster}",
        alpha=0.6
    )

plt.xlabel("Monthly Transaction Volume")
plt.ylabel("Cash Flow Volatility")
plt.title("MSME Behavioral Segments")
plt.legend()
plt.tight_layout()
plt.show()

# 7. DEFAULT PREDICTION

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    roc_auc_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


# GENERATE SYNTHETIC DEFAULT OUTCOME

np.random.seed(42)

# Behavioral variables used to generate default risk
default_features = customer_features[features_for_clustering].copy()

default_scaled = StandardScaler().fit_transform(
    default_features
)

default_scaled_df = pd.DataFrame(
    default_scaled,
    columns=features_for_clustering
)

# Behavioral risk score
risk_score = (
    0.8 * default_scaled_df["cash_flow_volatility"]
    + 0.3 * default_scaled_df["avg_transaction_amount"]
    - 0.4 * default_scaled_df["transaction_frequency"]
    - 0.3 * default_scaled_df["monthly_transaction_volume"]
    - 0.4 * default_scaled_df["repayment_ratio"]
)

# Lower baseline probability of default
intercept = -2.8

default_probability = 1 / (
    1 + np.exp(-(intercept + risk_score))
)

# Store probability
customer_features["default_probability"] = default_probability

# Generate default outcome
customer_features["default"] = np.random.binomial(
    1,
    customer_features["default_probability"]
)

print("\nDEFAULT GENERATION")
print(
    f"Average predicted default probability: "
    f"{customer_features['default_probability'].mean():.2%}"
)

print(f"Simulated default rate: "
    f"{customer_features['default'].mean():.2%}"
)

# Default outcomes are synthetically generated because  no labeled customer-level dataset was provided.
# The outcome is probabilistically linked to behavioral risk characteristics

# Prepare model data

X = customer_features[features_for_clustering]

y = customer_features["default"]

#Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)
# Standardize predictors

model_scaler = StandardScaler()

X_train_scaled = model_scaler.fit_transform(X_train)

X_test_scaled = model_scaler.transform(X_test)

# Train Logistic Regression model

logistic_model = LogisticRegression(
    random_state=42
)

logistic_model.fit(
    X_train_scaled,
    y_train
)
# Generate predictions

y_pred = logistic_model.predict(X_test_scaled)

y_probability = logistic_model.predict_proba(
    X_test_scaled
)[:, 1]

# Model evaluation

roc_auc = roc_auc_score( y_test, y_probability)

precision = precision_score( y_test, y_pred)

recall = recall_score( y_test,y_pred)

f1 = f1_score( y_test,y_pred)

print("\nLOGISTIC REGRESSION PERFORMANCE")

print(f"ROC-AUC:  {roc_auc:.3f}")
print(f"Precision: {precision:.3f}")
print(f"Recall:    {recall:.3f}")
print(f"F1 Score:  {f1:.3f}")

print("\nCONFUSION MATRIX")
print(confusion_matrix(y_test, y_pred))

# Model coefficients
coefficients = pd.DataFrame({
    "Feature": features_for_clustering,
    "Coefficient": logistic_model.coef_[0]
}).sort_values(by="Coefficient", ascending=False, key=lambda x: x.abs())
print("\nMODEL RISK DRIVERS\n")
print(coefficients)

from sklearn.metrics import roc_curve

fpr, tpr, thresholds = roc_curve(
    y_test,
    y_probability
)

plt.figure(figsize=(7, 6))

plt.plot(
    fpr,
    tpr,
    label=f"Logistic Regression (AUC = {roc_auc:.3f})"
)

plt.plot(
    [0, 1],
    [0, 1],
    linestyle="--"
)

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - MSME Default Prediction")
plt.legend()
plt.tight_layout()
plt.show()

# ILLUSTRATIVE RISK-BASED PRICING

pricing_scenarios = pd.DataFrame({
    "risk_segment": [
        "Stable / Lower Activity",
        "High Activity",
        "High Value / Volatile"
    ],
    "portfolio_share": [
        0.42,
        0.52,
        0.06
    ],
    "illustrative_monthly_yield": [
        8.00,
        9.50,
        16.00
    ]
})

# Portfolio-weighted monthly yield
weighted_yield = (
    pricing_scenarios["portfolio_share"]
    * pricing_scenarios["illustrative_monthly_yield"]
).sum()

# Base-case required monthly contribution
required_monthly_contribution = 4_500_000 / 36

# Current monthly contribution
current_monthly_contribution = 100_000

# Monthly contribution gap
monthly_gap = (
    required_monthly_contribution
    - current_monthly_contribution
)

# Additional monthly yield required per borrower
additional_yield_per_borrower = (
    monthly_gap / 20_000
)

print("\nILLUSTRATIVE RISK-BASED PRICING")
print("-" * 40)

print(pricing_scenarios)

print(
    f"\nWeighted average monthly yield: "
    f"${weighted_yield:.2f} per borrower"
)

print(
    f"Monthly contribution gap: "
    f"${monthly_gap:,.0f}"
)

print(
    f"Additional yield required per borrower: "
    f"${additional_yield_per_borrower:.2f}"
)

# 8. EXPORT RESULTS TO CSV
import os
os.makedirs("outputs", exist_ok=True)

# Base case summary
base_case_df = pd.DataFrame([{
    "Monthly Interest Income": monthly_interest_income,
    "Total Exposure": total_exposure,
    "Monthly Expected Loss": monthly_expected_loss,
    "Monthly Contribution": monthly_contribution,
    "Annual Contribution": annual_contribution,
    "3-Year Contribution": three_year_contribution,
    "3-Year Net Return": three_year_net_return,
    "3-Year ROI": three_year_roi,
    "Payback Period (months)": payback_period_months,
    "Credit-Loss-Only Breakeven Default Rate": break_even_default_rate,
}])
base_case_df.to_csv("outputs/base_case_summary.csv", index=False)

# Scenario analysis (optimistic / base / pessimistic)
scenario_df.to_csv("outputs/scenario_analysis.csv", index=False)

# Default rate sensitivity (1%-20%)
sensitivity_df.to_csv("outputs/default_rate_sensitivity.csv", index=False)

# Segmentation: cluster-level profile + risk labels + counts
cluster_summary = cluster_profile.copy()
cluster_summary["avg_risk_score"] = cluster_risk
cluster_summary["risk_segment"] = cluster_summary.index.map(risk_labels)
cluster_summary["customer_count"] = customer_features["cluster"].value_counts()
cluster_summary.to_csv("outputs/segmentation_profile.csv")

# Customer-level segment assignments
customer_features[
    ["customer_id", "cluster", "risk_segment", "risk_score"] + features_for_clustering
].to_csv("outputs/customer_segments.csv", index=False)

# Default model performance
model_performance_df = pd.DataFrame([{
    "ROC-AUC": roc_auc,
    "Precision": precision,
    "Recall": recall,
    "F1": f1,
}])
pricing_scenarios.to_csv(
    "illustrative_risk_based_pricing.csv",
    index=False
)
model_performance_df.to_csv("outputs/default_model_performance.csv", index=False)

print("\nAll CSV outputs saved to ./outputs/")

