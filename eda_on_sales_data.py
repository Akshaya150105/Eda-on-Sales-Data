from matplotlib.pyplot import title, xlabel, ylabel, show, figure, xticks, legend, pie, grid, axis,axvline
from pandas import read_csv, DataFrame, to_datetime
from seaborn import heatmap, countplot, barplot, color_palette, scatterplot
from pandas import read_excel, DataFrame,concat,DatetimeIndex


def describe_data(df: DataFrame):
    print(df.describe())


def correlation_matrix(df: DataFrame):

    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    figure(figsize=(10, 8))
    heatmap(numeric_df.corr(), annot=True,
            cmap='coolwarm', fmt=".2f", linewidths=0.5)
    title('Correlation Matrix')
    show()


def gender_byquantity(df: DataFrame):
    gender_quantity = df.groupby('Gender')['Quantity'].sum().reset_index()
    print(gender_quantity)
    


def productline_by_gender(df: DataFrame):
    
    figure(figsize=(12, 6))
    based_on_quantity=df.groupby(['Gender','Product line'])['Quantity'].sum().reset_index()
    barplot(x='Product line',y='Quantity',hue='Gender',data=based_on_quantity,palette='viridis')
    title('Number of Each Gender by Product line')
    xlabel('Product line')
    show()
    
   

def payment_type(df: DataFrame):
    figure(figsize=(10, 6))
    Payment_df = DataFrame(df['Payment'].value_counts())
    print(Payment_df)
    barplot(x=Payment_df.index, y=Payment_df['count'], palette='viridis')
    xlabel('Payment Type')
    show()


def product_line_by_gross_income(df: DataFrame):
    figure(figsize=(12, 6))
    barplot(x=df['Product line'], y=df['gross income'])
    title('Gross Income by Product Line')
    xlabel('Product Line')
    ylabel('Gross Income')
    show()


def avg_rating(df: DataFrame):
    avg_rating = df.groupby('Product line')['Rating'].mean().reset_index()
    avg_rating = avg_rating.sort_values(by='Rating', ascending=False)
    print(avg_rating)
    figure(figsize=(10, 6))
    barplot(data=avg_rating, x='Rating', y='Product line', palette='viridis')
    title('Average Rating by Product Line')
    xlabel('Average Rating')
    ylabel('Product Line')
    show()


def sales_highest_by_which_city(df: DataFrame):
    total_sales_by_city = df.groupby('City')['Total'].sum().reset_index()
    figure(figsize=(10, 6))
    barplot(x='City', y='Total', data=total_sales_by_city, palette='viridis')
    title('Total Sales by City')
    xlabel('City')
    ylabel('Total Sales')
    xticks(rotation=45)
    show()


def product_sales(df: DataFrame):
    sales_by_product = df.groupby(['City', 'Product line'])[
        'Total'].sum().reset_index()
    figure(figsize=(12, 8))
    barplot(x='City', y='Total', hue='Product line',
            data=sales_by_product, palette='viridis')
    title('Sales of Each Product for Each City')
    xlabel('City')
    ylabel('Total Sales')
    xticks(rotation=45)
    legend(title='Product line', bbox_to_anchor=(1.05, 1), loc='upper left')
    show()


def pie_chart(df: DataFrame):
    total_sales_by_city = df.groupby('City')['Total'].sum()
    figure(figsize=(8, 8))
    pie(total_sales_by_city, labels=total_sales_by_city.index,
        autopct='%1.1f%%', colors=color_palette('mako', len(total_sales_by_city)))
    title('Total Sales Distribution by City')
    show()


def time_period(df: DataFrame):
    df['Date'] = to_datetime(df['Date'])
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    start_date = to_datetime(start_date)
    end_date = to_datetime(end_date)
    period_sales = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    total_sales_period = period_sales['Total'].sum()
    print(total_sales_period)
    print("Total sales for the specified period:", total_sales_period)


def sales_by_customer_type(df: DataFrame):
    avg_sales = df.groupby(['Customer type', 'Gender'])['Total'].mean().reset_index()
    figure(figsize=(10, 6))
    barplot(x='Customer type', y='Total', hue='Gender', data=avg_sales, palette='viridis')
    title('Average Sales for Normal and Member Customers by Gender')
    xlabel('Customer Type')
    ylabel('Average Total Sales')
    show()
def month_insights(df: DataFrame):
    df['Date'] = to_datetime(df['Date'])
    df['month'] = DatetimeIndex(df['Date']).month
    print(df['month'])
    sales_month=df.groupby('month')['Total'].sum().reset_index()
    figure(figsize=(8, 8))
    barplot(x='month',y='Total',data=sales_month,color='pink')
    show()
def day_insights(df):
    
    df['Date'] = to_datetime(df['Date'])
    
  
    df['Day'] = df['Date'].dt.day_name()
    
    
    weekly_sales = df.groupby('Day')['Total'].sum().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    figure(figsize=(12, 6))
    barplot(x=weekly_sales.index, y=weekly_sales.values, color='lightblue')
    title('Total Sales by Day of the Week')
    xlabel('Day of the Week')
    ylabel('Total Sales')
    show()

def highest_sales_hour(df):
        df['Hour'] = to_datetime(df['Time'], format='%H:%M').dt.hour
        
        # Group by hour and sum the 'Total' sales
        sales_by_hour = df.groupby('Hour')['Total'].sum().reset_index()
        
        # Identify the hour with the highest sales
        max_sales_hour = sales_by_hour.loc[sales_by_hour['Total'].idxmax()]
        
        # Plot the sales for each hour
        figure(figsize=(10, 6))
        barplot(x='Hour', y='Total', data=sales_by_hour, palette='viridis')
        axvline(x=max_sales_hour['Hour'], color='red', linestyle='--', label=f'Highest Sales Hour: {max_sales_hour["Hour"]}')
        title('Total Sales by Hour of the Day')
        xlabel('Hour of the Day')
        ylabel('Total Sales')
        legend()
        show()

    
def highest_cogs(df):
   
    cogs_by_product_line = df.groupby('Product line')['cogs'].sum().reset_index()
    figure(figsize=(12, 6))
    barplot(x='Product line', y='cogs', data=cogs_by_product_line, palette='viridis')
    title('Total COGS by Product Line')
    xlabel('Product Line')
    ylabel('Total COGS')
    xticks(rotation=45)
    show()
df = read_csv('sales.csv')

print(df.dtypes)

correlation_matrix(df)
gender_byquantity(df)
productline_by_gender(df)
payment_type(df)
product_line_by_gross_income(df)
avg_rating(df)
sales_highest_by_which_city(df)
product_sales(df)
pie_chart(df)
sales_by_customer_type(df)
time_period(df)
month_insights(df)
day_insights(df)
sales_by_customer_type(df)
highest_cogs(df)
highest_sales_hour(df)