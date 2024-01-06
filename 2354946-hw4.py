# Task-1: Loading historical data from file orcl.csv to a list of dictionaries.
def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        headers = lines[0].strip().split(',')
        for line in lines[1:]:
            values = line.strip().split(',')
            entry = {headers[i]: values[i] for i in range(len(headers))}
            data.append(entry)
    return data

# Task-2: Calculatingc the Simple Moving Averages (SMA) for a 5-day window.
def calculate_sma(data, window_size=5):
    sma_values = []
    for i in range(len(data) - window_size + 1):
        sum_close = sum(float(data[j]['Close']) for j in range(i, i + window_size))
        sma = sum_close / window_size
        sma_values.append(sma)
    return sma_values

# Task-2: Calculating the Relative Strength Index (RSI) for a 14-day window.
def calculate_rsi(data, window_size=14):
    rsi_values = []
    gains = losses = 0

    for i in range(1, len(data)):
        diff = float(data[i]['Close']) - float(data[i - 1]['Close'])

        if diff > 0:
            gains += diff
        elif diff < 0:
            losses += abs(diff)

        if i >= window_size:
            avg_gain = gains / window_size
            avg_loss = losses / window_size

            if avg_loss == 0:
                rsi = 100
            else:
                rs = avg_gain / avg_loss
                rsi = 100 - (100 / (1 + rs))

            rsi_values.append(rsi)

            # Updating gains and losses for the next iteration
            gains -= float(data[i - window_size + 1]['Close']) - float(data[i - window_size]['Close'])
            losses -= abs(float(data[i - window_size + 1]['Close']) - float(data[i - window_size]['Close']))

    return rsi_values

# Task-3: SMA and RSI to separate CSV files.
def write_to_csv(file_path, data, header):
    with open(file_path, 'w') as file:
        file.write(','.join(header) + '\n')
        for row in data:
            file.write(','.join(map(str, row.values())) + '\n')

if __name__ == "__main__":
    # Task-1: Loading historical data frombfile orcl.csv to a list of dictionaries.
    historical_data = load_data("orcl.csv")

    # Task-2: Calculate Simple Moving Averages (SMA) for a 5-day window.
    sma_values = calculate_sma(historical_data)

    # Task-2: Calculate Relative Strength Index (RSI) for a 14-day window.
    rsi_values = calculate_rsi(historical_data)

    # Task-3: Write SMA and RSI to separate CSV files.
    sma_headers = ['Date', 'SMA']
    rsi_headers = ['Date', 'RSI']

    sma_data = [{'Date': historical_data[i + 4]['Date'], 'SMA': sma_values[i]} for i in range(len(sma_values))]
    rsi_data = [{'Date': historical_data[i + 13]['Date'], 'RSI': rsi_values[i]} for i in range(len(rsi_values))]

    write_to_csv("orcl-sma.csv", sma_data, sma_headers)
    write_to_csv("orcl-rsi.csv", rsi_data, rsi_headers)