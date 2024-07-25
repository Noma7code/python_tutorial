import pandas as pd

cust = pd.read_csv("Tech-salaries-india.csv")
print(cust)
df = pd.DataFrame(cust)
print(df)
print(df.head())
print(df.shape)
print(df.sort_values("annual_salary(USD)"))
print(df["seniority"])
coln = df[df["seniority"] == "Senior"]  #subsetting based on logical conditon
print(coln)
#subsetting based on ligical condition for mutiple selection
mix_cond = df[(df["seniority"] == "Intern") & (df["seniority"] == "Mid")]
print(mix_cond)
#south_mid_atlantic = homelessness[homelessness["region"].isin(["South Atlantic","Mid-Atlantic"])] subetting south or mid
#The Mojave Desert states
#canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
#mojave_homelessness = homelessness[homelessness["state"].isin(canu)]

# See the result
#print(mojave_homelessness)