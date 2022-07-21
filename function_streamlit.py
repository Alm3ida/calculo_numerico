import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


st.write("""
# Riemman Integral """)

number = st.slider("Número de retângulos",
                    min_value = 2)
                    
                    
# --- Integral Section
def f_limits(lim_inf = 0, 
             lim_sup = 10, 
             func_delta_x = 0.01):
    """Define os parâmetros iniciais de plotagem da função de base"""

    return lim_inf, lim_sup, func_delta_x
    
def f(x):
    y = - x ** 3/100 * (x-10)
    return y

def vf(x):
    return np.vectorize(f)(x)

func_lim_inf, func_lim_sup, func_delta_x = f_limits()

func_num = (func_lim_sup - func_lim_inf) / func_delta_x
func_interval = np.linspace(func_lim_inf, func_lim_sup, num = int(func_num))

# Number of rectangles
def numerical_integration(num = 10):
    interval = np.linspace(func_lim_inf, func_lim_sup, num = num + 1)
    
    choice = interval[:-1] + np.diff(interval) / 2
    choice = np.insert(choice, choice.shape[0], 10)
    delta = (func_lim_sup - func_lim_inf) / num

    riemann_rect = vf(choice)

    integral_sum = sum(riemann_rect * np.diff(interval)[0])

    return interval, choice, delta, riemann_rect, num, integral_sum

interval, choice, width, riemann_rect, num, integral_sum = numerical_integration(number)


# --- Plot Section
fig, ax = plt.subplots(figsize = (11,6), dpi = 300)

plt.xlabel('x', size = 14)
plt.ylabel('f(x)', size = 14)
plt.title(f"n = {num} retângulos")

plt.bar(interval + np.diff(interval)[0] / 2, 
        riemann_rect, 
        width = width , 
        edgecolor="black", 
        alpha = 0.25, color = "red")

plt.plot(func_interval, vf(func_interval))
plt.grid(alpha = 0.1)
plt.xlim(-0.5, 10.5)
plt.xticks([x for x in range (0, 11)])

 
st.write(f"A função de exemplo utilizada é")
st.latex(r'''f(x) = -\dfrac{x^3}{100}(10-x), \quad (0\leq x \leq 10)''')
st.pyplot(fig)
st.write(f"O valor da integral é {round(integral_sum, 4)}")



