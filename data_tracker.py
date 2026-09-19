import datetime
import os
import pandas as pd
from calculate import Income_traker



class Data:
  def __init__(self, filename='income_tracker.csv'):
    self.filename = filename
    self.columns =['date',
        'monthly_income',
        'rent',
        'utilities',
        'food',
        'transport',
        'clothes_skincare',
        'investment',
        'entertainment',]

    if not os.path.exists(self.filename):
      df = pd.DataFrame(columns=self.columns)
      df.to_csv(self.filename,index=False)

  def save_data(self, date_t):
    date_t['date'] = datetime.date.today().strftime('%Y-%m-%d')

    new_df = pd.DataFrame([date_t], columns=self.columns)

    new_df.to_csv(self.filename, mode='a', header=False, index=False)

  def get_history(self):
    return pd.read_csv(self.filename)







#test
if __name__ == '__main__':
      from calculate import Income_traker
      
calc= Income_traker(
      monthly_income=12000,
      rent=2500,
      utilities=600,
      food=2500,
      clothes_skincare=1500,
      transport=1000,)
storage = Data()
storage.save_data(calc.all_data())

print('---  CSV ---')
print(storage.get_history())