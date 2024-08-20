class Security:
  
  def __init__(self, isin, name):
    # international security identification number
    self.isin = isin
    # name of the security
    self.name = name

  def to_dict(self):
    return { 'isin': self.isin, 'name': self.name }
