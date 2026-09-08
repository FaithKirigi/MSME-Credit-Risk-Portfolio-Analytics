# MSME-Credit-Risk-Portfolio-Analytics
MSME credit risk analytics using financial modeling, K-Means segmentation, logistic regression, and portfolio scenario analysis.

## Overview

This project evaluates the financial viability and credit risk of a hypothetical short-term MSME lending product using financial modeling, customer segmentation, machine learning, and scenario analysis.

The objective is to demonstrate how transaction behavior and portfolio-level risk metrics can be used to support lending decisions for micro, small, and medium enterprises with limited formal financial histories.

The analysis combines:

- Expected credit loss and profitability modeling
- MSME behavioral segmentation using K-Means clustering
- Default prediction using Logistic Regression
- Optimistic, base, and pessimistic portfolio scenario analysis
- Early-warning indicators and risk-based pricing concepts

> **Note:** Customer transaction and default data used in the modeling sections are synthetic and were generated solely to demonstrate the analytical methodology. Results should not be interpreted as estimates from a real lending portfolio.

---

## Business Problem

MSME lending presents several challenges, particularly when borrowers have:

- Limited formal financial histories
- Irregular or seasonal cash flows
- Short-term and high-frequency borrowing needs
- Strong dependence on suppliers, distributors, and other value-chain participants

The analysis explores how behavioral transaction data can support credit-risk assessment while ensuring that the lending product remains financially sustainable.

The key questions addressed are:

1. Is the lending product financially viable?
2. Which MSME behavioral segments appear more or less risky?
3. Which transaction characteristics are associated with default risk?
4. How sensitive is portfolio profitability to changes in default rates?
5. What risk controls and early-warning indicators should be implemented?

---

## Analytical Approach

### 1. Financial Risk Modeling

The financial model estimates:

- Monthly interest income
- Exposure at Default (EAD)
- Expected credit loss
- Monthly and annual contribution
- Three-year investment return
- Payback period
- Credit-loss break-even default rate

Expected loss is calculated using:

**Expected Loss = Probability of Default × Loss Given Default × Exposure at Default**

### Base Case Results

| Metric | Result |
|---|---:|
| Monthly interest income | $160,000 |
| Total borrower exposure | $2.0M |
| Monthly expected credit loss | $60,000 |
| Monthly contribution after credit losses | $100,000 |
| Annual contribution | $1.20M |
| 3-year contribution | $3.60M |
| 3-year net return | -$900,000 |
| 3-year ROI | -20% |
| Payback period | 45 months |

The base case does not recover the initial investment within the targeted 36-month period.

---

## 2. Scenario Analysis

Portfolio performance was evaluated under three scenarios:

| Scenario | Default Rate | LGD | Monthly Contribution | 3-Year ROI | Payback |
|---|---:|---:|---:|---:|---:|
| Optimistic | 4% | 40% | $162.8K | 30% | 27.6 months |
| Base | 6% | 50% | $100K | -20% | 45 months |
| Pessimistic | 10% | 60% | $18K | -86% | 250 months |

The results show that portfolio profitability is highly sensitive to deterioration in credit performance.

---

## 3. MSME Customer Segmentation

Synthetic transaction data was aggregated at customer level and used to create behavioral features including:

- Transaction frequency
- Average transaction amount
- Monthly transaction volume
- Cash-flow volatility
- Repayment ratio

The features were standardized and segmented using **K-Means clustering with three clusters**.

### Cluster Profiles

| Segment | Frequency | Avg Transaction | Monthly Volume | Volatility |
|---|---:|---:|---:|---:|
| Stable / Lower Activity | 16.9 | $1,593 | $26.6K | $1,511 |
| High Activity | 38.9 | $1,829 | $70.5K | $2,077 |
| High Value / Volatile | 18.7 | $3,158 | $55.6K | $4,915 |

The High Value / Volatile segment warrants closer monitoring because its higher transaction values are accompanied by significantly greater cash-flow volatility.

---

## 4. Default Prediction

A Logistic Regression model was trained to estimate MSME default probability using behavioral transaction features.

### Model Performance

| Metric | Result |
|---|---:|
| ROC-AUC | 0.837 |
| Precision | 0.727 |
| Recall | 0.308 |
| F1 Score | 0.432 |

The model demonstrates good rank-ordering ability, although recall at the default classification threshold is relatively low.

In a production lending environment, the classification threshold should therefore be optimized based on the relative cost of missed defaults versus false-positive declines.

### Key Risk Drivers

| Feature | Relationship with Default Risk |
|---|---|
| Cash-flow volatility | Higher risk |
| Transaction frequency | Lower risk |
| Repayment ratio | Lower risk |
| Monthly transaction volume | Mildly higher risk |
| Average transaction amount | Lower risk |

Cash-flow volatility was the strongest positive risk signal in the model.

---

## 5. Early-Warning Framework

The analysis recommends monitoring behavioral, credit, and portfolio-level indicators such as:

- Rising cash-flow volatility
- Declining transaction frequency
- Falling repayment ratios
- Missed or late repayments
- Increasing loan utilization
- Frequent repeat borrowing
- Default rates by customer segment
- Vintage and cohort performance
- Value-chain concentration
- Geographic concentration

These indicators can be used to trigger account reviews, credit-limit adjustments, or changes in pricing.

---

## 6. Illustrative Risk-Based Pricing

A simple pricing scenario was developed to demonstrate how differentiated pricing could help improve portfolio economics.

| Segment | Portfolio Share | Illustrative Monthly Yield |
|---|---:|---:|
| Stable | 42% | $8.00 |
| Active | 52% | $9.50 |
| Volatile | 6% | $16.00 |

The weighted average yield is approximately **$9.26 per borrower per month**, compared with the $8.00 base-case assumption.

This pricing framework is illustrative only. A production pricing model would require calibrated estimates of Probability of Default, Loss Given Default, funding costs, operating costs, expected recoveries, and borrower price sensitivity.

---

## Recommendations

The analysis supports a **controlled pilot rather than an immediate full-scale rollout**.

The base case does not achieve the targeted 36-month payback period, while the pessimistic scenario demonstrates significant downside risk.

Recommended actions include:

- Apply behavioral and transaction-based underwriting
- Use exposure limits for volatile borrowers
- Monitor value-chain and geographic concentration
- Implement early-warning triggers
- Optimize the default classification threshold
- Recalibrate the model using real repayment data
- Validate EAD and LGD assumptions using actual portfolio performance
- Scale only when observed credit losses and portfolio returns demonstrate a credible path to the investment target

---

## Tools & Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Microsoft Excel

### Machine Learning

- K-Means Clustering
- Logistic Regression
- StandardScaler
- Train/Test Split
- ROC-AUC
- Precision
- Recall
- F1 Score

---

## Repository Structure

```text
msme-credit-risk-analytics/
│
├── README.md
│
├──msme_credit_risk_analysis.py
│
├── outputs/
│   ├── financial_model_results.csv
│   ├── scenario_analysis.csv
│   ├── customer_segments.csv
│   ├── cluster_profile.csv
│   ├── default_model_metrics.csv
│   ├── model_risk_drivers.csv
│   └── illustrative_risk_based_pricing.csv
│
├──  MSME_Credit_Risk_Assessment.pdf
│
├──  Executive_Summary.pdf

