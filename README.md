# Credit-Risk
Goal is to create a probability of Default models using various methods and comparing the results

#### Data set introduction : 
| Feature Name | Description |
| ----- | ----- |
| `SeriousDlqin2yrs` | Person experienced 90 days past due delinquency or worse. |
| `RevolvingUtilizationOfUnsecuredLines` | Total balance on credit cards and personal lines of credit (except real estate and no installment debt like car loans) divided by the sum of credit limits. |
| `age` | Age of borrower in years. |
| `NumberOfTime30-59DaysPastDueNotWorse` | Number of times borrower has been 30-59 days past due but no worse in the last 2 years. |
| `DebtRatio` | Monthly debt payments, alimony, living costs divided by monthly gross income. |
| `MonthlyIncome` | Monthly income. |
| `NumberOfOpenCreditLinesAndLoans` | Number of Open loans (installment like car loan or mortgage) and Lines of credit (e.g., credit cards). |
| `NumberOfTimes90DaysLate` | Number of times borrower has been 90 days or more past due. |
| `NumberRealEstateLoansOrLines` | Number of mortgage and real estate loans, including home equity lines of credit. |
| `NumberOfTime60-89DaysPastDueNotWorse` | Number of times borrower has been 60-89 days past due but no worse in the last 2 years. |
| `NumberOfDependents` | Number of dependents in family excluding themselves (spouse, children, etc.). |

In the main.ipynb notebook, a simple EDA was performed, after which I chose to treat the task as a classification problem to estimate the probability of default (where 0 means the client will repay, and 1 means the client will default).