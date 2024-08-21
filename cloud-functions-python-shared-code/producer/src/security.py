class Security:
  
  def __init__(self, isin, name):
    # international security identification number
    self.isin = isin
    # name of the security
    self.name = name

  @staticmethod
  def from_dict(input_dict):
    return Security(input_dict['isin'], input_dict['name'])     
  
  def to_dict(self):
    return { 'isin': self.isin, 'name': self.name }
