# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 

# code starts here
bank=pd.read_csv(path)
df=pd.DataFrame(bank)
categorical_var= df.select_dtypes(include = 'object')
print(categorical_var)

numerical_var= df.select_dtypes(include = 'number')
print(numerical_var)

# code ends here


# --------------
# code starts here

banks= bank.drop(columns='Loan_ID')

# check  all the missing values filled.

print(banks.isnull().sum())

# apply mode 

bank_mode = banks.mode().iloc[0]

# Fill the missing values with 

banks.fillna(bank_mode, inplace=True)

# check again all the missing values filled.

print(banks.isnull().sum())


#code ends here


# --------------
# Code starts here

avg_loan_amount= pd.pivot_table(banks, values ='LoanAmount', index =['Gender', 'Married','Self_Employed'], aggfunc = np.mean)


# code ends here



# --------------
# code starts here
Loan_Status= 614

loan_approved_se = len(banks[(banks['Loan_Status'] == 'Y') & (banks['Self_Employed']== 'Yes')])

loan_approved_nse = len(banks[(banks['Loan_Status'] == 'Y') & (banks['Self_Employed']== 'No')])

# Loan approval for self employed

percentage_se = (loan_approved_se/ Loan_Status)*100
percentage_nse= (loan_approved_nse/ Loan_Status)*100

print(percentage_se)
print(percentage_nse)

# Loan approval for not self employed 




# code ends here


# --------------
# code starts here

loan_term= banks['Loan_Amount_Term'].apply(lambda x: x//12)


print(loan_term)
big_loan_term= len([x for x in loan_term if x >= 25])
print(big_loan_term)



# code ends here


# --------------
# code starts here

loan_groupby= banks.groupby('Loan_Status')[['ApplicantIncome', 'Credit_History']]

mean_values= loan_groupby.mean()


# code ends here


