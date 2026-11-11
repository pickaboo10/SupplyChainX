# SupplyChainX: Inventory Recovery Agent

An AI agent for supply chain and warehouse managers, built for INNOVORTEX 4.0 (Nonilion track). It investigates inventory shortages across warehouses, compares fixes, and prepares transfer or purchase drafts that wait for the manager's approval.

## Problem
A shortage in one warehouse is often solvable with stock sitting idle in another, but finding out means checking spreadsheets, supplier data and demand by hand. SupplyChainX does that investigation in one chat request.

## Who it is for
Supply chain managers, warehouse managers and procurement teams at retail and e-commerce distributors.

## What it does
- Looks up stock, days of cover and risk per product and warehouse
- Calculates how much each warehouse can give away without breaching its own safety stock
- Compares transfer, purchase and mixed options on cost and timing, and warns about unavoidable gaps
- Prepares TR-/PO- drafts and waits for `approve <ID>` or `reject <ID>`
- Asks a clarifying question for vague requests and says so for impossible ones

## How it works
- Platform: Nonilion (imported agent), model: Gemini
- The business data (3 warehouses, 8 products, 4 suppliers, open purchase orders) is synthetic and sits in the agent instructions with pre-computed metrics, so the model looks values up instead of doing arithmetic.
- Approval is simulated. Nothing changes real stock or places real orders.

## Files
| File | Purpose |
|---|---|
| `agent_instructions.md` | The agent's instructions and data, pasted into Nonilion |
| `inventory.csv` | The same inventory data for inspection |
| `test_prompts.md` | Test scenarios with expected results |
| `test_key.py` | Runs the agent logic outside Nonilion for debugging |

## Run the local check
```
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # then add your own key
python test_key.py
```

## Limitations
- Demand is a 14-day average, so seasonality is not modelled.
- Data is synthetic and the approval step is simulated.
- Calculations are pre-computed in the data, not run by live code.

## Next steps
A backend with a database and deterministic tools, connected through the Nonilion Bot API, would replace the pre-computed tables with live calculations.
