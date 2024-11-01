# Daily Streamflow Analysis at Khairtabad Station

This repository contains Python scripts and data for analyzing daily streamflow at the Khairtabad station in the Kabul River Basin for the year 2010. The analysis includes calculations of mean monthly discharge and visualizations of both daily and monthly discharge data.

## Table of Contents

- [Overview](#overview)
- [Data](#data)
- [Installation](#installation)
- [Usage](#usage)
- [Visualization](#visualization)
- [License](#license)
- [Contributing](#contributing)

## Overview

This project aims to provide insights into the streamflow patterns of the Kabul River Basin by processing and visualizing daily discharge data. It leverages Python libraries such as Pandas and Matplotlib for data manipulation and visualization.

## Data

The data used in this analysis is a daily discharge dataset for the Khairtabad station, provided in an Excel file format. The file contains two columns:
- `Date`: The date of the recorded discharge (format: MM/DD/YYYY).
- `Discharge (Cumics)`: The discharge value in cubic meters per second.

## Installation

To run this project, you need Python 3.x installed on your machine along with the required libraries. You can install the necessary packages using pip:

```bash
pip install pandas matplotlib openpyxl
