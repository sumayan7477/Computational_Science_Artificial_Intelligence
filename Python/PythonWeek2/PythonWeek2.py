# %% Exercise set 1
# task 1 ----------------------------------------------------

# 1(c)
print("Hello World!")

# 1(d)
import numpy as np
sine = np.sin(np.pi/2)
cosine = np.cos(3*np.pi)
print(sine)
print(cosine)


# 1(f)
sin_pi = np.sin(np.pi)
print(sin_pi)
# Explanation :
# the theoretical value of sin(pi) is 0 but the value obtained is 1.2246467991473532e-16 which is very close to 0 but not exactly 0. This is due to the limitations of floating point representation in computers. The value is so small that it can be considered as 0 for practical purposes.


# %% Exercise Set1
# task 2 ----------------------------------------------------

t2i = (23.4 * 2**2 - 238) / (9**2 + 34.2)
print("The value of t2i is:", t2i)

t2ii = ((8 / 9) ** 3) * 32 - (3**6) / (7**7 - 555)
print("The value of t2ii is:", t2ii)

t2iii = 4 * np.sqrt(2200) - 45
print("The value of t2iii is:", t2iii)

t2iv = np.sqrt(4**5) + np.log(np.exp(-5))
print("The value of t2iv is:", t2iv)

t2v = np.sin(np.pi) - abs(np.cos(np.pi) / 2)
print("The value of t2v is:", t2v)

t2vi = (23 + np.exp(-2)) / (np.exp(4) + np.log(1023))
print("The value of t2vi is:", t2vi)

t2vii = np.tan((np.pi / 6) * np.log(8)) / (np.sqrt(17) + 2)
print("The value of t2vii is:", t2vii)

t2viii = np.cbrt(-8) + (6103515625 ** (1 / 7))
print("The value of t2viii is:", t2viii)


t2ix = np.cos(5 * np.pi / 6) * (np.sin(8 * np.pi / 7) ** 2)
print("The value of t2ix is:", t2ix)

# %% Exercise Set1
# task 3 ----------------------------------------------------

ects_credits = 5
hours_per_ects = 1600/60
total_course_hours = ects_credits * hours_per_ects
weeks = 8
weekly_hours = total_course_hours / weeks
print(f"Total course hours: {total_course_hours:.2f} hours")
print(f"Weekly work needed: {weekly_hours:.2f} hours/week")

# %% Exercise Set1
# task 4 ----------------------------------------------------
# solve |x - 5| > |x| + 1
# sum 3^n from n=1 to 6
# derivative of sin(x^2 + 1)
# solve y = x + 1, y = -x + 3



