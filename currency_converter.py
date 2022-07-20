def usd_to_gbp(bucks):
  gbp_total = bucks * 0.77
  return gbp_total

def usd_to_eur(bucks):
  eur_total = bucks * 0.92
  return eur_total

def usd_to_cny(bucks):
  cny_total = bucks * 6.98
  return cny_total

def main():
  bucks = input("How many bucks pal?")
  bucks = float(bucks)
  type_of_currency = input("What type of currency? gbp(1),eur(2), or cny(3)?")
  type_of_currency= int(type_of_currency)
  gbp=1
  eur=2
  cny=3
  if type_of_currency == gbp:
    print(usd_to_gbp(bucks))

  if type_of_currency == eur:
    print(usd_to_eur(bucks))

  elif type_of_currency == cny:
    print(usd_to_cny(bucks))
if __name__== "__main__":
  main()
