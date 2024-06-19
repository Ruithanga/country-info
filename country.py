from countryinfo import CountryInfo
country=input("Enter your country : ")
country = CountryInfo(country)
print("Capital is : ", country.capital())
print("Currency is : ", country.currencies())
print("language is : ", country.languages())
print("Borders are : ", country.borders())
print("Sub-region is : ", country.subregion())
print("Other names : ", country.alt_spellings())
