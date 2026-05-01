# 📊 Trader Performance vs Market Sentiment

This project looks at how traders behave when the market is in Fear vs Greed.

Instead of just looking at prices, I wanted to understand something simple:
👉 Does market emotion affect how people trade?

---

## 🧠 What I tried to find

I explored questions like:

- Do traders make more profit during Greed?
- Are they more careful during Fear?
- Does risk (like leverage) change with sentiment?

---

## 📂 Data Used

I worked with two datasets:

1. **Historical Trading Data**
   - Includes trade details like price, size, side, leverage, and profit/loss

2. **Fear & Greed Index**
   - Shows whether the market sentiment is Fear or Greed for each day

---

## ⚙️ What I did

- Converted timestamps into dates  
- Matched each trade with the market sentiment of that day  
- Cleaned missing and messy data  
- Focused on 3 main things:
  - Profit (PnL)
  - Win rate
  - Leverage usage  

---

## 📈 What I found

### 1. Profit Behavior
- During **Greed**, profits can be higher  
- But results are not stable (more ups and downs)

### 2. Win Rate
- During **Fear**, win rate is slightly better  
- This suggests traders are more careful

### 3. Risk (Leverage)
- Leverage is higher in **Greed**
- Traders take bigger risks when market is positive

### 4. Trading Behavior
- More trading activity happens during Greed  
- Could be due to excitement or overconfidence

---

## 🧾 Conclusion

There is a clear connection between market sentiment and trading behavior.

- **Greed → higher risk, higher reward, less consistency**
- **Fear → lower risk, more stable performance**

---

## 💡 Simple Takeaway

A trader can improve decisions by adjusting behavior:

- During Greed → control risk  
- During Fear → focus on consistency  

---

## 🚀 How to run this project

```bash
pip install -r requirements.txt
python src/analysis.py
