import pandas as pd 
import numpy as np
import matplotlib.pyplot  as plt

customer=pd.read_csv("C:\pythonproject\Customer.csv")
# print(customer)
prod_cat_info=pd.read_csv("C:\pythonproject\prod_cat_info.csv")
# print(prod_cat_info)
transaction=pd.read_csv("C:\pythonproject\Transactions.csv")
# print(transaction)

cust_trans=pd.merge(left=customer,
                    right=transaction,
                    left_on='customer_Id',
                    right_on='cust_id',
                    how='inner',
                    indicator=True)
# print(cust_trans)

Customer_Final=pd.merge(left=cust_trans,
                        right=prod_cat_info,
                        left_on='prod_cat_code',
                        right_on='prod_cat_code',
                        how='inner')
print(Customer_Final)
# print(Customer_Final.dtypes)

tot_male=Customer_Final['Gender'].value_counts()['M']
# print("total male customers:",tot_male)
tot_female=Customer_Final['Gender'].value_counts()['F']
# print("total female customers:",tot_female)


''' 1: Get the column names and their corresponding data types'''
# print(Customer_Final)
# print(Customer_Final.dtypes)

'''2:Top/Bottom 10 observations'''
# print(Customer_Final.tail(10))

'''c: "Five-number summary” for continuous variables (min, Q1, median, Q3 and max)'''
Data_min=Customer_Final['total_amt'].min()
# print(Data_min)
Data_max=Customer_Final['total_amt'].max()
# print("max in total amount",Data_max)
Q1=np.percentile(Customer_Final['total_amt'],25)
# print(Q1)
median=np.percentile(Customer_Final['total_amt'],50)
# print(median)
Q3=np.percentile(Customer_Final['total_amt'],75)
# print(Q3)

'''d:Frequency tables for all the categorical variables'''
# f=pd.crosstab(index = Customer_Final['Gender'],
#                          columns = Customer_Final['Store_type'])
# f.columns = ['TeleShop','MBR','e-shop','Flagshipstore']
# f.index = ['Male','Female']
# print(f)
# p=pd.crosstab(index=Customer_Final['Gender'],columns=Customer_Final['city_code'])
# p.index=['male','female']
# print(p)
# freq_table = pd.crosstab(index = Customer_Final['Gender'],
#                          columns = Customer_Final['prod_subcat'])
# freq_table.columns = ['Men','Women','Kid','Mobile','Computer','Personal Appliances','Cameras','Audio and video',
#                       'Fiction','Academic','Non-fiction','Children','Comics','DIY','Furnishing','Kitchen',
#                       'Bath','Tools']
# freq_table.index = ['Male','Female']
# print(freq_table)

'''3:generate histogram for all continous  variables  and frequency bars for categorical variables'''
# city=Customer_Final['city_code']
# plt.hist(city,width=0.4,edgecolor='r')
# plt.xlabel("city_code")
# plt.ylabel("Store_type")
# plt.show()

# Total_amt=Customer_Final['total_amt']
# plt.hist(Total_amt,color='Blue')
# plt.xlabel("total amount")
# plt.ylabel("Frequency")
# plt.show()




'''4].Calculate the following information using the merged dataset :
a. Time period of the available transaction data'''

# d=Customer_Final['tran_date'].groupby()           doubt
# print(d)                                              


'''b. Count of transactions where the total amount of transaction was negative'''
# df=Customer_Final['total_amt']
# count1=Customer_Final.loc[(df<0),['total_amt']].count()
# print(count1) 


'''5].which product category more poopulr among male and females'''
# popular among males
# m=Customer_Final.loc[Customer_Final['Gender']=='M']
# group_prod=m.groupby(['prod_cat'])['total_amt'].count()
# print(group_prod.nlargest(1))

# popular among females
# f=Customer_Final.loc[Customer_Final['Gender']=='F']
# group_prodd=f.groupby(['prod_cat'])['total_amt'].count()
# print(group_prodd.nlargest(1))

'''6].which city code has the maximum customers and what was the percentage of customers from that city'''
# maxcust = Customer_Final['city_code'].value_counts()
# t=(maxcust.nlargest(1))
# print("city code which has maximum customers:",t)


'''7].Which store type sells the maximum products by value and by quantity'''
# sort_list=Customer_Final.sort_values(['total_amt','Qty'],ascending=True)
# print(sort_list)
# print(sort_list.tail(1)['Store_type'])

'''8].What was the total amount earned from the "Electronics" and "Clothing" categories from Flagship Stores'''
# pc=Customer_Final[Customer_Final.prod_cat.isin(['Electronics','Clothing']) & (Customer_Final.Store_type == 'Flagship store')]
# s=pc.total_amt.sum()
# print(s)


'''9].what was total amount earned from male customers under electronics category'''
# t_male=Customer_Final[(Customer_Final.Gender == 'M') & (Customer_Final.prod_cat == 'Electronics')]
# earn_male=t_male.total_amt.sum()
# print("total amount earned:",earn_male)

'''10].. How many customers have more than 10 unique transactions, after removing all transactions 
which have any negative amounts?'''
# t=Customer_Final[(Customer_Final.total_amt > 0)]
# ts=t.transaction_id.nunique()
# print("total customers having more than 10 unique =",ts)


'''11].11. For all customers aged between 25 - 35, find out:
a. What was the total amount spent for “Electronics” and “Books” product categories?'''
# t=Customer_Final[Customer_Final.prod_cat.isin( ['Electronics','Books'])]
# ta=t.total_amt.sum()
# print("total amount spent on electronics and books:",ta)

