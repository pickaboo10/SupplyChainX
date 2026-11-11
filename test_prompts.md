# Test prompts and expected results

Run each prompt in the Nonilion chat. Numbers come from `inventory.csv`.

## 1. Inventory shortage
**Prompt:** Our Delhi warehouse has only 20 units of Product P101. Check other warehouses and find the best way to avoid a stockout.

**Expected:** Delhi cover 1.3 days, risk 60 (High). Transfer 84 from Mumbai and 18 from Bengaluru (cost INR 2,220). Purchase order of 50 units from S01 (INR 45,000). About 10 units short before the Mumbai stock lands in 2 days. Ends by asking for approval.

## 2. Approval
**Prompt:** approve TR-001

**Expected:** Marks TR-001 APPROVED (simulated). Does not claim real execution.

## 3. Ambiguous request
**Prompt:** Fix my inventory problem

**Expected:** One short clarifying question. No invented details.

## 4. Supplier delay
**Prompt:** Supplier S02 has delayed an order by four days. Which products and warehouses are affected?

**Expected:** PO-9001 (P104, Delhi) and PO-9002 (P106, Delhi). P106 Delhi: cover 2.5 days, risk 50 (Medium, base 30 + 20 for the delay). P104 Delhi: cover 14.3 days, risk 20 (Low). Mitigation for P106: transfer 130 from Mumbai (INR 2,600, 2 days, arrives before stock runs out).

## 5. Excess stock
**Prompt:** Find products with excess stock in Mumbai that could be transferred to other warehouses.

**Expected:** P103 (529 surplus), P105 (233), P106 (187). Suggests Delhi P101 and P106 as destinations with shortfalls.

## 6. Impossible request
**Prompt:** Track my shipment live on the GPS map.

**Expected:** Says it cannot do real-time tracking and offers what it can do.

## 7. Report
**Prompt:** Create a CSV report of this investigation.

**Expected:** A CSV file with the investigation table and draft actions, or a clear statement of what the route supports.
