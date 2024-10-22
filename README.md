# Random Number Dashboard

A simple multithreaded dashboard built using `Tkinter` that displays random numbers within specified ranges. Each label refreshes at different intervals, showcasing the use of Python's `threading` module to update the UI in real-time.

## Features

- Multithreading for updating random numbers asynchronously.
- A visually appealing dashboard with colored labels.
- Adjustable range of random numbers and refresh intervals for each label.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/random-number-dashboard.git
    ```

2. Navigate to the project directory:

    ```bash
    cd random-number-dashboard
    ```

3. Run the Python script:

    ```bash
    python dashboard.py
    ```

## How It Works

The application creates a simple graphical dashboard using the `Tkinter` library. Each label on the dashboard displays a random number that is updated asynchronously using the `threading` module. Each label has:

- A specific range for generating random numbers.
- A designated refresh time (in seconds).
- A unique background color for visual distinction.

### Dashboard Layout

The dashboard consists of six labels, each with its own random number range and refresh interval:

| Range           | Refresh Time (s) | Color            |
|-----------------|------------------|------------------|
| 10 to 20        | 10               | lightseagreen    |
| -10 to 10       | 20               | salmon           |
| -100 to 0       | 8                | gold             |
| 0 to 20         | 12               | cornflowerblue   |
| -40 to 40       | 16               | orchid           |
| 100 to 200      | 14               | palegreen        |

## Customization

You can easily customize the ranges, refresh times, and colors of the labels by editing the `ranges_and_times` list inside the `create_dashboard` function:

```python
ranges_and_times = [
    (10, 20, 10, "lightseagreen"),
    (-10, 10, 20, "salmon"),
    (-100, 0, 8, "gold"),
    (0, 20, 12, "cornflowerblue"),
    (-40, 40, 16, "orchid"),
    (100, 200, 14, "palegreen")
]
```
# Output
![image](https://github.com/user-attachments/assets/a201980b-df5c-4435-8968-528a0ad8cca1)

Each number is updated independently without affecting the others, using separate threads. The dashboard remains responsive while all numbers update concurrently.

