#Feature engineering

#Fuel cost
# O tried to create a column named fuel cost which will calculate the total fuel cost of the entire trip so that it will help us to know more detail about our project
MILEAGE = 15          # km per litre
PETROL_PRICE = 100    # ₹ per litre

df["Fuel Cost (₹)"] = (
    (df["Distance (km)"] / MILEAGE) * PETROL_PRICE
).round(2)

df.head()

#this column was created to calculate the total toll tax
def calculate_toll(road_type, distance):

    if "Expressway" in road_type:
        rate = 1.5

    elif "National Highway" in road_type:
        rate = 0.8

    else:
        rate = 0.3

    return round(distance * rate, 2)


df["Toll Tax (₹)"] = df.apply(
    lambda row: calculate_toll(
        row["Road Type"],
        row["Distance (km)"]
    ),
    axis=1
)

df.head()

#emmision factors gives us carbon emission directly in our hand
EMISSION_FACTOR = 0.12

df["Carbon Emission (kg CO₂)"] = (
    df["Distance (km)"] * EMISSION_FACTOR
).round(2)

df.head()

# to make our model work efficiently time was needed to be converted into numerical values
import re

def convert_to_hours(time):

    match = re.match(r'(\d+)h\s*(\d+)m', time)

    if match:
        hours = int(match.group(1))
        minutes = int(match.group(2))
        return round(hours + minutes/60, 2)

    return None


df["Travel Time (Hours)"] = df["Estimated Travel Time"].apply(convert_to_hours)
df["Travel Time (Hours)"].head()


# Total Cost = Fuel Cost + Toll Tax

df["Total Cost"] = df["Fuel Cost (₹)"] + df["Toll Tax (₹)"]
df.head()
