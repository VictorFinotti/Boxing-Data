# Professional Boxers Statistics Analysis

![Status](https://img.shields.io/badge/Status-Complete-green)
![Python](https://img.shields.io/badge/Python-3.13-blue)

## 📋 Table of Contents
- [Business Problem](#business-problem)
- [Dataset](#dataset)

## 🎯 Business Problem
*How to help people learn about boxing*

**Problem**: People may feel insecure about where to begin and want reassurance about their choices  
**Objective**: To compile data in order to give well informed indications and suggestions  
**Stakeholders**: Companies focused growing and transforming sport as a vehicle for social impact  

## 📊 Dataset
| Source | Size     | Time Period | Key Variables                         |
|--------|----------|-------------|---------------------------------------|
| https://boxing-data.com | 101 x 12 | up to date  | JSON clean, parsing and serialization |  

**Data Dictionary**:
```csv
Name, categorical, Boxer Full Name
Age, int, Boxer's Age
Debut, int, Boxer Debut Year
Nationality, categorical, Country of Origin
Stance, categorical, Boxer Prominent Stance
Reach, float/int, Boxer's wingspan in inch / cm
Total_Bouts, int, Boxer Number of Fights
Wins, int, Boxer Victories
Winrate, float, Boxer Wins/Total_Bouts
Total_Rounds, float, Sum of Boxer rounds in the Ring
Ko_Wins, int, Boxer Number of Wins by Knockout
Ko_Percentage, int, Ko_wins/Total_Bouts*100
