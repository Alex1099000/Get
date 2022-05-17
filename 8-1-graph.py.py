import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data.txt', dtype=np.float64)
k = len(data)
settings = np.loadtxt('settings.txt', dtype=np.float64)
freq = settings[0]
q = settings[1]
time = k / freq
t = np.linspace(0, time, k)
T = t[data.argmax()]
data = data * q

fig, ax = plt.subplots(figsize=(10, 7), dpi=200)
ax.plot(t, data, label='$U(t)$', color='tab:blue', marker='o', markevery=10, linestyle='-', linewidth=2, markersize=4)
ax.set_xlim(0, time)
ax.set_ylim(0, max(data) + 0.2)
ax.set_xlabel('Время, с', size='large')
ax.set_ylabel('Напряжение, В', size='large')
ax.set_title('Процесс заряда и разряда конденсатора в RC-цепи', size='xx-large', wrap=True)
ax.minorticks_on()
ax.grid(which='minor', linestyle=':', color='0.9')
ax.grid(which='major', linestyle='-', color='0.8')
x_text = time / 6
y_text = max(data) / 2
ax.text(time / 6, max(data) / 2, f'Время зарядки: ' + str(round(T,1))+' c')
ax.text(time/ 6, max(data) / 2 - 0.2, f'Время разрядки: ' + str(round(time-T,1))+' c')
ax.legend()
fig.savefig('8-1-fig.png')
#plt.show()