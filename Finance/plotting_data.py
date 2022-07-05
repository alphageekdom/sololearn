import matplotlib.pyplot as plt

rev = [18000, 25000, 20000, 45000, 32000]
months = ['June', 'July', 'August', 'September', 'October']

# plot(x-axis, y-axis)
plt.plot(months, rev)
plt.savefig('rev_plot.png')