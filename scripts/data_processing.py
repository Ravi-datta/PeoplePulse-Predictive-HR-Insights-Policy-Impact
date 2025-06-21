import pandas as pd

def load_and_clean():
    emp = pd.read_csv('data/employee_master.csv')
    reviews = pd.read_csv('data/performance_reviews.csv')
    # merge and clean...
    return emp, reviews

if __name__ == '__main__':
    emp, reviews = load_and_clean()
    print(emp.head(), reviews.head())
