data = [100, 120, 130, 125, 140, 150]

alpha = 0.3

forecast = data[0]

print("Actual Data:", data)

for value in data[1:]:
    forecast = alpha * value + (1 - alpha) * forecast

print("Next Period Forecast:", round(forecast, 2))
