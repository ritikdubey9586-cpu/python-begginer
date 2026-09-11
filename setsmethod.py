city1={"surat","kim","vadodara","rajkot","ahmedabad"}
city2={"mumbai","delhi","bangalore","chennai","kolkata"}
print(city1.union(city2))


# union is used to combine differenet different sets to make single sets.


city1={"surat","kim","vadodara","rajkot","ahmedabad"}
city2={"mumbai","delhi","bangalore","chennai","kolkata"}
cities=city1.intersection(city2)
print(cities)

# intersection is used to make sets without same value either in two sets or more than two sets means it is used to find the common elements from sets.


city1={"surat","kim","vadodara","rajkot","ahmedabad"}
city2={"mumbai","delhi","bangalore","chennai","kolkata"}
cities=city1.intersection_update(city2)
print(cities)


city1={"surat","kim","vadodara","rajkot","ahmedabad"}
city2={"mumbai","delhi","bangalore","chennai","kolkata"}
cities=city1.difference(city2)
print(cities)



city1={"surat","kim","vadodara","rajkot","ahmedabad"}
city2={"mumbai","delhi","bangalore","chennai","kolkata"}
cities=city1.isdisjoint(city2)
print(cities)


city1={"surat","kim","vadodara","rajkot","ahmedabad"}
city2={"mumbai","delhi","bangalore","chennai","kolkata"}
cities=city1.issuperset(city2)
print(cities)


city1={"surat","kim","vadodara","rajkot","ahmedabad"}
city2={"mumbai","delhi","bangalore","chennai","kolkata"}
cities=city1.issubset(city2)
print(cities)



city1={"surat","kim","vadodara","rajkot","ahmedabad"}
city2={"mumbai","delhi","bangalore","chennai","kolkata"}

city1.add("amit")
print(city1)



city1={"surat","kim","vadodara","rajkot","ahmedabad"}
city2={"mumbai","delhi","bangalore","chennai","kolkata"}

city1.remove("surat")
print(city1)


city1={"surat","kim","vadodara","rajkot","ahmedabad"}
city2={"mumbai","delhi","bangalore","chennai","kolkata"}

city1.discard("amit")
print(city1)


city1={"surat","kim","vadodara","rajkot","ahmedabad"}
city2={"mumbai","delhi","bangalore","chennai","kolkata"}

a=city1.pop()
print(a)




'''city1={"surat","kim","vadodara","rajkot","ahmedabad"}
city2={"mumbai","delhi","bangalore","chennai","kolkata"}

a=city1.pop()
print(a)'''