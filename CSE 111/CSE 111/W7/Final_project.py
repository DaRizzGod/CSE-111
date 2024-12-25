import csv

year_index = 0
avg_close_index = 1
open_index = 2
high_index = 3
low_index = 4
close_index = 5
ann_change_index = 6

print('Welcome to the stock market, where the fun happens!')

    
def read_compund_list(filename):
        
        compound_list = []
        
        with open(filename, 'rt') as csv_file:
            
            reader = csv.reader(csv_file)
            
            next(reader)
            
            for row in reader:
                
                compound_list.append(row)
                
            return compound_list
        
# def predict_next_10_years(stock):
   
#         print(f"Predicting the next 10 years for {stock[year_index]} stock...")
        
def main():
        stock_list = read_compund_list('stock_market.csv')
        get_year = lambda stock: stock[year_index]
        stock_list.sort(key=get_year)
        
        get_avg = lambda stock: stock[avg_close_index]
        stock_list.sort(key=get_avg)
        get_open = lambda stock: stock[open_index]
        stock_list.sort(key=get_open)
        get_high = lambda stock: stock[high_index]
        stock_list.sort(key=get_high)
        get_low = lambda stock: stock[low_index]
        stock_list.sort(key=get_low)
        get_close = lambda stock: stock[close_index]
        stock_list.sort(key=get_close)
        get_ann = lambda stock: stock[ann_change_index]
        stock_list.sort(key=get_ann)
        
    
            
        print('In the time of {year_index} that the {open_index} from the ranges of {high_index} to {low_index} that the market decided to {close_index} but annually its going to be {ann_change_index}')


main()