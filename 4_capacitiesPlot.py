import matplotlib.pyplot as plt

# Data
categories = ['V2R_WT + IB cntrl', 'V2R_WT + IB 30', 'V2R_360 + IB cntrl', 'V2R_360 + IB 30', 'single cell']
values = [2.242668029,2.166057747,1.940012271,2.28336056, 2.364370355458091]

# Define colors for each lollipop
colors = ['blue', 'green', 'red', 'orange', 'purple']

# Create lollipop plot
plt.figure(figsize=(10, 6))
plt.stem(categories, values, markerfmt='o', basefmt=" ", linefmt='gray', use_line_collection=True)
plt.xlabel('Sample', fontsize=14)  # Increase font size
plt.ylabel('Channel Capacity (in bits)', fontsize=14)  # Increase font size
plt.title('Calculated Channel Capacity', fontsize=16)  # Increase font size
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Customize lollipop size and color
lollipop_size = 22
for category, value, color in zip(categories, values, colors):
    plt.plot(category, value, 'o', markersize=lollipop_size, color=color)

plt.xticks(rotation=45, fontsize=12)  # Increase font size
plt.yticks(fontsize=12)  # Increase font size
plt.tight_layout()
plt.show()