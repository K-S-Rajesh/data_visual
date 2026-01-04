import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Region": ["Cannanore RSA", "KANNUR", "MAHE", "Kanhangad RSA", "KANNUR", "KASARGOD", "KOZHIKODE EAST RSA", "KOZHIKODE", "WAYANAD", "KOZHIKODE WEST RSA", "KOZHIKODE", "LAKSHADWEEP", "MALAPPURAM", "Malappuram RSA", "MALAPPURAM", "Tirur RSA", "MALAPPURAM"],
    "Count of COMPANY": [177, 152, 25, 183, 85, 98, 189, 120, 69, 146, 140, 4, 2, 189, 189, 176, 176],
    "Count of RO CODE": [177, 152, 25, 183, 85, 98, 189, 120, 69, 146, 140, 4, 2, 189, 189, 176, 176]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plotting correlation
plt.figure(figsize=(8, 8))
plt.scatter(df['Count of COMPANY'], df['Count of RO CODE'])
plt.xlabel('Count of COMPANY')
plt.ylabel('Count of RO CODE')
plt.title('Correlation between COMPANY and RO CODE Counts')
plt.plot([0, 200], [0, 200], 'r--')  # 45-degree line for reference
plt.show()