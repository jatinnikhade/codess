import matplotlib.pyplot as plt

#sample data for demonstration
categories = ['0-10','10-20','20-30','30-40','40-50']
values = [55,48,25,68,90]
plt.bar(categories,values,color='red')
plt.xlabel('overs')
plt.ylabel('runs')
plt.title('bar plot showing runs scored in odi match')
plt.show()           
        
