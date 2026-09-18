class Income_traker :
  def __init__(self ,monthly_income,rent,utilities,food,
               clothes_skincare,transport):
    self.income = monthly_income
    self.rent = rent 
    self.utilities = utilities
    self.food = food 
    self.clothes_skincare = clothes_skincare 
    self.transport = transport 
    
  def calculate_investment(self):
      return self.income *0.20
  
  def calculate_entertainment(self):
      total = (self.rent + self.utilities+ self.food+ 
               self.clothes_skincare+self.transport+
               self.calculate_investment() )
      entertainment = self.income - total
      return entertainment
      
  def all_data(self):
      return{ "monthly_income":self.income,
             "rent":self.rent ,
             "utilities":self.utilities,
             "food":self.food,
             "transport":self.transport,
             "clothes_skincare":self.clothes_skincare,
             "investment":self.calculate_investment(),
             "entertainment":self.calculate_entertainment(),}
             
# test
if __name__ == '__main__':
  test_tracker = Income_traker(
      monthly_income=10000,
      rent=2000,
      utilities=500,
      food=2000,
      clothes_skincare=1000,
      transport=1000,
  )
  print("-----results-----")
  print(test_tracker.all_data())
 