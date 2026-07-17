# Why MRP Alone Cannot Run Your Supply Chain: The Complete SAP Landscape for Demand, Supply, and Replenishment Planning

A company runs MRP every night.

The planning job finishes successfully.

Thousands of planned orders and purchase requisitions are created.

The system has technically calculated every material requirement.

Yet planners still spend the morning:

- moving dates;
- cancelling proposals;
- increasing quantities;
- calling suppliers;
- checking production capacity;
- transferring stock between plants;
- expediting critical components.

Management asks why the company needs SAP IBP, PP/DS, aATP, supplier collaboration and warehouse planning when MRP already exists.

The answer is simple:

> MRP calculates material requirements. It does not manage the complete demand-to-supply process.

MRP can determine:

- what material is needed;
- how much is missing;
- when it should be available;
- whether it should be produced or purchased;
- which planning proposal should be created.

MRP cannot independently decide:

- what future market demand is likely to be;
- which demand scenario management should approve;
- where inventory should be positioned across a global network;
- whether production capacity is realistically available;
- whether the supplier accepts the requested quantity and date;
- which customer should receive scarce supply;
- whether the warehouse can execute the replenishment;
- whether the plan actually produced the expected result.

A modern SAP planning landscape therefore contains several layers.

```text
Market and customer signals
        ↓
Demand planning
        ↓
S&OP and business balancing
        ↓
Inventory and supply network planning
        ↓
Operational response planning
        ↓
S/4HANA demand management and MRP
        ↓
Detailed production and procurement planning
        ↓
Supplier, factory, and warehouse execution
        ↓
Actual consumption and feedback
```

Different SAP products and components support different parts of this chain.

The challenge is not purchasing every product.

It is assigning each planning decision to the right system.

## The first distinction: planning is not one process

Supply-chain planning is normally divided by time horizon and decision granularity.

## Strategic planning

Typical questions:

- Which plants and warehouses are required?
- Which products should be stocked?
- Which suppliers should receive long-term volume?
- Which capacities must be added?
- Which inventory risk is acceptable?

The horizon may cover years.

The data is aggregated.

## Tactical planning

Typical questions:

- What demand should we expect by month or week?
- Can current capacity support it?
- Which products or markets need inventory protection?
- Which scenarios should management approve?
- How should supply be distributed across the network?

The horizon may cover several months to more than a year.

## Operational planning

Typical questions:

- Which order should be produced next week?
- Which components must be purchased?
- Which plant should supply the demand?
- Which existing orders must be rescheduled?
- Which customers receive scarce supply?

The horizon is normally measured in days, weeks or a few months.

## Execution

Typical questions:

- Which production operation starts now?
- Which warehouse bin must be replenished?
- Did the supplier confirm the purchase order?
- Which handling unit should move to the production line?
- Was the expected quantity actually received?

Trying to use MRP for all four levels creates excessive system nervousness and manual intervention.

## The modern SAP planning stack

A complete architecture may include the following applications and components.

| Process responsibility | SAP solution or component |
|---|---|
| Strategic and financial alignment | SAP IBP for S&OP |
| Statistical demand planning | SAP IBP for Demand |
| Short-term demand sensing | SAP IBP demand sensing |
| Inventory target optimization | SAP IBP for Inventory |
| Network and constrained supply planning | SAP IBP for Response and Supply |
| Demand-driven network buffers | SAP IBP demand-driven replenishment or SAP S/4HANA DDR |
| Operational demand in ERP | Planned Independent Requirements in SAP S/4HANA |
| Material requirements calculation | SAP S/4HANA MRP Live |
| Scenario and capacity simulation | SAP S/4HANA predictive MRP |
| Detailed finite production planning | Embedded SAP S/4HANA PP/DS |
| Customer order confirmation | SAP S/4HANA aATP |
| Procurement execution | SAP S/4HANA Sourcing and Procurement |
| Supplier forecast and order collaboration | SAP Business Network Supply Chain Collaboration |
| Production execution | SAP S/4HANA Production Orders and SAP Digital Manufacturing |
| Warehouse replenishment and staging | SAP EWM |
| Transport execution | SAP Transportation Management |
| Alerts and network visibility | SAP IBP visibility and control-tower capabilities |

Not every business needs every layer.

A small distribution company may work effectively with:

- S/4HANA MRP;
- reorder-point planning;
- purchase orders;
- basic warehouse replenishment.

A global constrained manufacturer may need:

- IBP Demand;
- IBP Response and Supply;
- S/4HANA MRP Live;
- PP/DS;
- aATP;
- Business Network collaboration;
- EWM;
- Digital Manufacturing.

Complexity should follow the business problem.

## Part I: Where demand enters the process

MRP cannot plan without demand.

Demand can enter from several sources.

### Customer orders

These are real transactional requirements.

They contain:

- product;
- quantity;
- required date;
- customer;
- delivery location.

Customer orders are usually strongest as short-term demand evidence.

But waiting for customer orders may be too late for products with long procurement or production lead times.

### Planned Independent Requirements

Planned Independent Requirements, or PIRs, represent expected demand maintained in SAP S/4HANA.

They are commonly used in make-to-stock and forecast-based planning.

PIRs can originate from:

- manual planning;
- an external demand-planning system;
- SAP IBP;
- pMRP simulation results;
- historical demand calculation.

### Dependent requirements

When MRP explodes a bill of material, demand for a finished product creates dependent requirements for:

- assemblies;
- components;
- raw materials.

For example:

```text
100 finished products
× 4 components per product
= 400 component requirements
```

### Reservations and internal demand

Demand may also arise from:

- maintenance;
- projects;
- production orders;
- internal consumption;
- stock transfers;
- service processes.

### Forecast consumption

In many planning strategies, customer orders consume forecast requirements.

This prevents the system from planning twice for:

- the expected forecast;
- the actual customer order replacing that forecast.

The consumption logic depends on the selected planning strategy and configuration.

## SAP IBP for Demand

SAP IBP for Demand operates before operational MRP.

Its purpose is to create a demand plan from several demand signals.

SAP currently describes IBP demand capabilities as combining multiple demand signals, statistical forecasts, demand sensing, machine-learning models, outlier correction and time-series analysis.

Possible inputs include:

- historical shipments;
- customer orders;
- point-of-sale data;
- promotions;
- market events;
- customer forecasts;
- product lifecycle;
- planner adjustments.

The output is not automatically a purchase order.

It is an approved demand plan.

### What IBP Demand should own

IBP Demand may own:

- statistical baseline;
- planner forecast;
- consensus demand;
- promotional uplift;
- demand scenario;
- forecast accuracy analysis.

### What IBP Demand should not own

It should not normally become the transactional system for:

- purchase orders;
- production orders;
- warehouse tasks;
- goods movements.

Those remain execution responsibilities.

## Demand sensing

Demand sensing focuses on the short-term forecast.

It may use recent information such as:

- new customer orders;
- sales trends;
- current consumption;
- order cancellations;
- short-term market signals.

SAP positions demand sensing as a way to refine short-term forecasts and improve fulfilment and inventory performance.

Demand sensing does not eliminate the forecast.

It adjusts the near-term view using more recent evidence.

### Where demand sensing helps

- consumer goods;
- retail replenishment;
- high-frequency products;
- products with recent demand shifts;
- promotion-driven demand.

### Where it adds less value

- highly engineered products;
- one-off project demand;
- very low-volume spare parts;
- products with no meaningful history.

## S&OP and Integrated Business Planning

Sales and Operations Planning is the management process for balancing:

- demand;
- supply;
- inventory;
- capacity;
- finance.

SAP IBP currently provides S&OP capabilities for connecting financial and operational planning, collaboration, scenario simulation and performance monitoring.

The approved S&OP plan should answer:

- Which demand scenario do we accept?
- Which supply constraints remain?
- Which service levels do we protect?
- Which inventory investment is approved?
- Which capacity or sourcing action is needed?

MRP should not make these decisions automatically.

It should execute the approved assumptions at operational detail.

## Part II: Inventory planning before replenishment

Inventory planning asks:

> Where should inventory exist, and how much risk should it protect?

This is different from running MRP after a shortage occurs.

## SAP IBP for Inventory

SAP IBP for Inventory supports inventory target planning across several supply-chain stages.

SAP describes current capabilities including multi-echelon inventory optimization, statistical modelling, forecast-error management and analysis of inventory drivers.

A multi-echelon model can consider inventory at:

- factory;
- central warehouse;
- regional warehouse;
- local warehouse.

The objective is not to minimize each location independently.

It is to determine how the network should share buffers.

### Questions inventory optimization addresses

- Where should safety stock be positioned?
- Which echelon should absorb variability?
- How do service targets affect inventory?
- How do lead time and forecast error affect the buffer?
- Can centralized inventory protect several downstream locations?

### Output

The output may include target inventory parameters or recommendations that are transferred into operational planning.

IBP Inventory does not normally create the final warehouse replenishment task.

## Static safety stock in S/4HANA

SAP S/4HANA can maintain safety stock at plant or MRP-area level.

During net-requirements calculation, safety stock reduces the quantity considered freely available for planning. If stock falls below the defined safety level, MRP generates replenishment proposals.

This is straightforward.

Its limitations are that the parameter may become outdated if:

- demand variability changes;
- supplier performance changes;
- service policy changes;
- lead times change.

A static safety stock is only as current as its maintenance process.

## Part III: The main replenishment philosophies

There is no single best replenishment method.

Materials should be segmented.

## 1. Deterministic MRP

Deterministic MRP plans against explicit requirements such as:

- forecasts;
- PIRs;
- sales orders;
- dependent requirements.

SAP describes deterministic planning as a multilevel BOM-based process starting from independent demand and customer orders.

Best suited to:

- high-value components;
- products with dependent BOM demand;
- long-lead materials;
- manufactured products;
- materials requiring time-phased coordination.

### Main logic

```text
Demand
– available stock
– existing receipts
= shortage
```

The system then determines:

- lot size;
- procurement type;
- start and finish dates;
- dependent requirements.

## 2. Reorder-point planning

Reorder-point planning triggers replenishment when available stock falls below a defined threshold.

```text
Available stock position < reorder point
→ create replenishment proposal
```

SAP identifies reorder-point planning as a consumption-based approach suited to relatively consistent demand and known replenishment lead times.

Best suited to:

- low-value consumables;
- stable demand;
- simple replenishment;
- items where detailed BOM-driven planning is unnecessary.

Examples:

- screws;
- packaging;
- office materials;
- standard indirect parts.

### Manual reorder point

The planner maintains the reorder point.

### Automatic reorder point

The system may calculate parameters using historical consumption and forecasting, depending on the implemented planning method.

### Risk

A reorder point may fail when:

- consumption becomes volatile;
- supplier lead time changes;
- product demand is seasonal;
- the item becomes critical.

## 3. Forecast-based planning

Forecast-based planning uses historical consumption to estimate future requirements.

It is useful where demand is consumption-driven but cannot be managed through one fixed reorder threshold.

The system can create time-phased forecast requirements.

Best suited to:

- relatively repeatable consumption;
- products without detailed dependent demand;
- operational supplies.

## 4. Time-phased planning

Time-phased planning schedules replenishment according to defined planning cycles.

For example:

- supplier orders reviewed every Monday;
- deliveries received every Thursday.

It can reduce frequent small purchasing actions.

It is useful when:

- suppliers have fixed delivery cycles;
- transport operates on scheduled days;
- planners review materials periodically.

The main risk is missing short-term demand between cycles.

## 5. Kanban

Kanban is a pull-based replenishment method.

Consumption of a container or quantity triggers replenishment.

It is frequently used for:

- production supply;
- repetitive manufacturing;
- line-side components;
- simple internal replenishment.

A Kanban signal may trigger:

- internal transfer;
- production;
- external procurement.

Kanban is not a forecast system.

It is an execution signal for a predefined replenishment loop.

### Best conditions

- stable consumption;
- short and reliable replenishment;
- standardized containers;
- disciplined execution.

### Weak conditions

- highly variable consumption;
- long supplier lead time;
- frequent engineering changes;
- severe capacity constraints.

## 6. Demand-Driven Replenishment and DDMRP

Demand-Driven Material Requirements Planning uses strategic decoupling points and dynamically managed inventory buffers.

Instead of transmitting every demand fluctuation through the complete BOM and network, selected buffers absorb variability.

SAP describes its S/4HANA Demand-Driven Replenishment process as including:

1. buffer positioning;
2. buffer profiles and sizing;
3. dynamic buffer adjustment;
4. replenishment based on actual consumption;
5. execution prioritization based on buffer penetration.

### Core concepts

#### Decoupling point

A strategic location where inventory breaks dependency between upstream and downstream lead times.

#### Buffer zones

A buffer commonly represents different urgency zones.

The exact sizing depends on factors such as:

- average daily usage;
- lead time;
- variability;
- order cycle.

#### Net flow position

A demand-driven replenishment decision considers available and expected supply against qualified demand.

#### Buffer penetration

Shows how deeply actual demand has consumed the buffer.

This supports priority decisions.

### DDMRP is not “MRP without forecasts”

Forecasts may still be used for:

- capacity planning;
- buffer adjustment;
- S&OP;
- future risk.

But replenishment execution at decoupling points is driven more directly by actual consumption and buffer state.

### Where DDMRP can help

- long cumulative lead times;
- variable demand;
- repeated MRP nervousness;
- frequent rescheduling;
- need to protect material flow.

### Where it can fail

- buffers selected politically rather than analytically;
- poor average-usage calculation;
- no discipline in order priority;
- buffers never resized;
- every material made a decoupling point;
- planners continue overriding the system.

## 7. Distribution replenishment

Distribution replenishment determines how stock should flow between locations.

Examples:

```text
Factory
→ central distribution centre
→ regional warehouse
→ local warehouse
```

The problem is not only producing enough total quantity.

The company must decide where it should go.

This can be supported through:

- SAP IBP Response and Supply;
- stock-transfer planning in S/4HANA;
- deployment rules;
- replenishment parameters;
- scheduling agreements;
- demand-driven buffers.

IBP can model multilevel locations and BOM structures and create constrained or unconstrained tactical supply plans.

## 8. Warehouse replenishment

Warehouse replenishment is different from supply-chain MRP.

MRP may determine that a plant needs 10,000 units.

EWM may determine that a forward picking location needs another 100 units from reserve storage.

SAP EWM supports high-volume warehouse processes, integration with production and quality, inventory transparency, slotting and warehouse automation.

Typical EWM replenishment methods include concepts such as:

- planned replenishment;
- automatic replenishment;
- order-related replenishment;
- direct replenishment;
- crate or fixed-bin replenishment.

The exact supported options depend on the EWM edition and configuration.

### Supply-chain replenishment

Moves inventory between:

- suppliers;
- plants;
- warehouses.

### Warehouse replenishment

Moves inventory inside the warehouse from reserve to point of use.

Do not confuse them.

## Part IV: SAP IBP Response and Supply

SAP IBP Response and Supply operates between aggregate business planning and local ERP execution.

SAP currently describes it as supporting:

- multilevel network modelling;
- constrained and unconstrained planning;
- heuristic and optimization approaches;
- rough-cut capacity planning;
- operational and order-based supply planning;
- allocations and repromising.

## Supply planning

Supply planning decides how demand should be fulfilled across a network.

It may consider:

- plants;
- suppliers;
- warehouses;
- BOM levels;
- sourcing alternatives;
- lead times;
- rough-cut capacity;
- inventory targets.

### Unconstrained plan

Answers:

> What supply would be needed if capacity and selected constraints were unlimited?

This exposes the theoretical requirement.

### Constrained plan

Answers:

> What can realistically be supplied under the modelled constraints?

The difference between these plans exposes gaps.

## Heuristic planning

A heuristic follows defined planning rules.

Advantages:

- faster;
- easier to explain;
- suitable for large routine calculations.

Limitations:

- may produce a feasible but not economically optimal result;
- result depends strongly on sequence and rules.

## Optimization

An optimizer evaluates alternatives against objectives and constraints.

Possible objectives include:

- minimize cost;
- reduce late demand;
- protect service;
- reduce inventory.

The optimization result is only as valid as:

- costs;
- constraints;
- lead times;
- capacities;
- priorities.

An optimizer cannot repair false data.

## Response management

Response management focuses on operational or order-based supply plans.

It can support decisions such as:

- which customer orders receive constrained supply;
- how orders should be repromised;
- how allocations should be managed.

This overlaps conceptually with aATP BOP and allocation.

The architecture must define which system owns:

- tactical allocation;
- transactional confirmation;
- order repromising.

A common pattern is:

```text
IBP
creates network and allocation plan
        ↓
S/4HANA aATP
executes transactional confirmation
```

## Part V: SAP S/4HANA Demand Management

S/4HANA Demand Management translates demand into operational planning requirements.

The selected planning strategy determines how the system handles:

- forecast demand;
- customer orders;
- stock;
- consumption;
- individual customer segments.

## Make-to-stock

Production or procurement occurs before the final customer order.

Demand may be represented by PIRs.

Customer orders consume forecast quantities according to the planning strategy.

Best suited to:

- standard products;
- predictable or statistically planable demand;
- products requiring immediate availability.

## Make-to-order

Supply is linked more directly to a specific customer order.

Best suited to:

- configured products;
- project products;
- high-value low-volume items;
- customer-specific manufacturing.

### Advantages

- lower finished-goods risk;
- clear demand ownership.

### Trade-offs

- longer customer lead time;
- less ability to pool stock;
- production capacity becomes part of the promise.

## Assembly-to-order

Components or assemblies are stocked.

Final assembly occurs after the customer order.

This can balance:

- responsiveness;
- variety;
- inventory.

## Planning without final assembly

Demand may drive component planning while final production waits for customer orders.

This is useful when:

- components have long lead times;
- final configuration depends on the customer;
- common components can be shared.

## Part VI: Predictive MRP

Predictive MRP, or pMRP, is not the nightly operational MRP run.

It is a simulation capability.

SAP describes pMRP as supporting simplified multilevel simulations of demand, materials and capacity, allowing planners to compare scenarios and assess capacity problems, preproduction and make-or-buy decisions before releasing changes into operational planning.

### pMRP asks

- What happens if demand increases?
- Which work centre becomes overloaded?
- What if capacity is increased?
- Which components could be preproduced?
- What if the source of supply changes?

### pMRP does not execute

It should not be confused with:

- MRP Live;
- detailed PP/DS scheduling;
- production-order execution.

It provides an early warning and scenario view.

### Where pMRP is useful

- medium-term capacity risk;
- purchasing preparation;
- make-or-buy analysis;
- demand scenario evaluation;
- preproduction decisions.

### pMRP versus IBP

pMRP is closer to S/4HANA operational master and transaction data.

IBP provides broader collaborative and network planning.

A company may use:

- IBP for enterprise-wide S&OP and network planning;
- pMRP for a focused S/4HANA material and capacity simulation.

Using both for the same decision without ownership creates duplicate planning.

## Part VII: MRP Live in SAP S/4HANA

MRP Live is the operational S/4HANA planning engine.

Its task is to identify material shortages and create supply proposals.

SAP’s official S/4HANA learning content describes MRP as:

- multilevel BOM explosion;
- net-requirements calculation;
- lot sizing;
- procurement-type determination;
- scheduling;
- creation of planned orders or purchase requisitions.

## Step 1: Net-requirements calculation

The system compares requirements against relevant supply.

Possible requirements include:

- customer orders;
- PIRs;
- dependent requirements;
- reservations;
- stock-transfer demand.

Possible supply includes:

- stock;
- purchase orders;
- production orders;
- planned orders;
- scheduling-agreement receipts.

If supply covers demand, no new proposal is needed.

If a shortage exists, MRP plans replenishment.

## Step 2: Lot sizing

MRP determines the proposal quantity.

Possible lot-sizing philosophies include:

- lot for lot;
- fixed quantity;
- periodic quantity;
- minimum lot;
- maximum lot;
- rounding.

SAP describes lot sizing as the step that converts the shortage into the quantity to produce or procure.

### Lot-for-lot

Proposal matches the shortage.

Advantages:

- low excess.

Risks:

- many small orders;
- high setup or purchasing effort.

### Fixed lot

Proposal uses a predefined quantity.

Advantages:

- operational stability;
- can reflect production or packaging constraints.

Risks:

- excess inventory.

### Periodic lot

Several requirements in a period are combined.

Advantages:

- fewer orders;
- consolidation.

Risks:

- earlier inventory;
- potential delay.

## Step 3: Procurement type

The material determines whether supply should be:

- produced internally;
- purchased externally;
- selected between both approaches.

SAP’s learning material describes standard procurement types for in-house, external or both, with special procurement types refining the source.

Special procurement may represent:

- stock transfer;
- subcontracting;
- production at another plant;
- consignment;
- external processing.

## Step 4: Scheduling

MRP calculates when the supply process must begin.

For internal production, timing may consider:

- opening period;
- in-house production time;
- goods-receipt processing;
- routing lead times.

For external procurement:

- purchasing processing;
- planned delivery time;
- goods-receipt processing;
- transport where represented.

SAP describes backward scheduling from the required availability date and possible forward scheduling when the calculated start falls in the past.

## Step 5: BOM explosion

The planned finished-product quantity creates component requirements.

MRP repeats the calculation through lower BOM levels.

```text
Finished product
→ assembly
→ component
→ raw material
```

This is the power of MRP.

It is also the source of nervousness.

A small top-level change may move requirements across many levels.

## MRP outputs

Depending on the process, MRP can create planning elements such as:

- planned orders;
- purchase requisitions;
- scheduling-agreement schedule lines;
- stock-transfer proposals.

SAP notes that planned orders can later be converted to production orders, process orders or purchase requisitions, while purchase requisitions can be converted to purchase orders.

MRP creates proposals.

It does not prove that:

- a supplier has accepted;
- production capacity exists;
- the order has been released;
- the material will arrive on time.

## MRP Areas

MRP can plan at more granular scopes than the complete plant.

An MRP area may represent:

- plant;
- storage locations;
- subcontractor area.

This allows different:

- stock responsibility;
- planning parameters;
- replenishment.

MRP-area design should reflect operational ownership.

Creating too many areas increases master-data and planning complexity.

## MRP controller

The MRP controller represents planning responsibility.

It can support:

- work allocation;
- exception routing;
- planning selection.

It should not be used as a substitute for proper product segmentation.

## Planning time fence

A planning time fence protects the near-term plan from continuous automatic changes.

Inside the fence, selected proposals may be fixed or treated differently.

This helps reduce nervousness.

But a frozen plan that is already infeasible does not become feasible through protection.

The organization needs a controlled exception process.

## Firming

Firming prevents MRP from freely changing selected supply proposals.

Firming can protect:

- supplier commitments;
- production preparation;
- stable execution.

Excessive firming creates a planning landscape where MRP detects shortages but cannot resolve them.

## MRP exception messages

MRP can identify situations such as:

- bring order forward;
- postpone order;
- cancel proposal;
- shortage;
- start date in the past.

The exact message set depends on configuration and release.

The management issue is prioritization.

A planner should not be expected to process every message equally.

## Monitor Material Coverage

SAP’s S/4HANA learning material identifies the Monitor Material Coverage Fiori application as an interactive tool for analysing material planning and shortages.

Depending on the S/4HANA release and deployment model, planners may use Fiori applications such as:

- Monitor Material Coverage;
- Manage Material Coverage;
- Schedule MRP Runs;
- Manage Planned Orders;
- Manage Purchase Requisitions;
- Manage Production Orders;
- Manage PIRs;
- Schedule pMRP Simulation Creation;
- Process pMRP Simulations.

Exact application availability and names must be checked against the specific SAP release.

## Part VIII: Capacity — where ordinary MRP is not enough

Traditional MRP is primarily material-driven.

It may calculate capacity requirements.

But it does not automatically produce the best finite production sequence.

If five orders require the same machine at the same time, MRP may still create all five proposals.

The planner then sees an overload.

## Capacity evaluation

Basic capacity evaluation can show:

- required capacity;
- available capacity;
- overload by work centre;
- time buckets.

This is useful for identifying problems.

It may not be enough to solve complex sequencing.

## Embedded PP/DS

SAP S/4HANA PP/DS provides advanced planning and detailed scheduling for selected products and resources.

It is relevant when planning must consider:

- finite capacity;
- setup sequences;
- alternative resources;
- product priorities;
- detailed timing;
- component availability;
- optimization or advanced heuristics.

SAP’s official learning content confirms that MRP Live and PP/DS planning can be combined, with PP/DS-enabled products using advanced planning and other products remaining in standard S/4HANA planning.

### Use PP/DS selectively

Not every screw and packaging item needs detailed scheduling.

A practical segmentation may be:

#### PP/DS materials

- bottleneck products;
- constrained resources;
- sequence-dependent production;
- complex manufacturing.

#### Standard MRP materials

- simple externally purchased items;
- unconstrained consumables;
- low-value components;
- stable replenishment.

## PP/DS planning methods

Depending on the scenario, PP/DS may use:

- heuristics;
- product planning runs;
- resource scheduling;
- optimization;
- detailed scheduling board.

### Heuristic

Applies predefined planning logic.

### Optimizer

Searches for a better plan according to costs and constraints.

### Detailed scheduling board

Allows planners to review and adjust resource sequences.

The planner should not manually schedule every operation.

Human attention should focus on:

- bottlenecks;
- exceptions;
- economically important decisions.

## MRP Live and PP/DS coordination

A major architectural risk is allowing several planning runs to overwrite one another.

SAP’s learning material warns that PP/DS products and standard MRP materials need a carefully defined planning sequence and scope so that detailed results are not unintentionally recalculated.

The operating model should define:

1. which products are PP/DS relevant;
2. which planning run executes first;
3. which scope excludes already detailed products;
4. which system or algorithm owns the receipt dates;
5. when results may be changed.

## Part IX: Procurement execution

MRP creates a purchase requisition or another external-procurement proposal.

Procurement converts the proposal into a commercial commitment.

## Source determination

The system or buyer identifies:

- supplier;
- contract;
- purchasing info record;
- scheduling agreement;
- source list;
- quota arrangement.

MRP may know that the material should be purchased.

It may not know which supplier is commercially and operationally best unless sourcing master data is complete.

## Purchase requisition

A purchase requisition represents an internal requirement to buy.

It may be:

- created automatically by MRP;
- created manually;
- approved;
- sourced;
- converted to purchase order.

## Purchase order

The purchase order is the external commercial order.

It contains:

- supplier;
- quantity;
- date;
- price;
- delivery location;
- terms.

A purchase order date is still not a supplier confirmation.

## Scheduling agreement

For repetitive supply, a scheduling agreement can communicate recurring schedule lines against a longer-term agreement.

This is particularly relevant in:

- automotive;
- repetitive manufacturing;
- stable direct-material flows.

## Supplier confirmation

The supplier may confirm:

- accepted quantity;
- confirmed date;
- partial quantity;
- changed date.

The confirmation should update the planning picture.

Otherwise, MRP continues planning against the requested date rather than the supplier’s current commitment.

## Part X: SAP Business Network Supply Chain Collaboration

Supplier collaboration extends planning outside the company.

SAP Business Network Supply Chain Collaboration currently supports:

- forecast collaboration;
- supplier forecast commitments;
- purchase-order collaboration;
- order confirmation;
- shipment visibility;
- supplier-managed inventory;
- replenishment orders;
- scheduling agreements;
- manufacturing and quality collaboration.

## Forecast collaboration

The buyer shares expected demand.

The supplier may provide:

- commitment;
- available capacity;
- exceptions;
- adjusted quantity.

This provides earlier visibility than waiting for the purchase order.

### Important distinction

A supplier’s forecast commitment is not always legally equivalent to a purchase-order confirmation.

The contract and process must define its meaning.

## Purchase-order collaboration

The supplier receives the purchase order digitally and can confirm:

- quantity;
- date;
- changes.

This reduces:

- email;
- spreadsheet tracking;
- manual update.

## Inventory collaboration

SAP Business Network supports visibility into supplier-managed inventory and replenishment processes using replenishment orders or scheduling agreements.

Possible models include:

- vendor-managed inventory;
- consignment;
- customer-owned stock at supplier;
- supplier stock visibility.

## Manufacturing collaboration

For outsourced manufacturing, collaboration may include:

- component inventory;
- subcontracting demand;
- production status;
- finished quantity;
- quality information.

The planning model should not assume that supplier capacity is unlimited merely because the material is externally procured.

## Part XI: Production execution

A planned order is only a planning proposal.

It must be converted into an executable production order or process order.

## Production order

The production order controls:

- product;
- quantity;
- dates;
- operations;
- components;
- resources;
- confirmations;
- costs.

## Process order

Used in process-industry scenarios where production may involve:

- recipes;
- phases;
- batches;
- process instructions.

## Order release

Release authorizes execution.

Before release, checks may include:

- material availability;
- capacity;
- approvals;
- batch or quality requirements.

## Material staging

Components must reach production.

This can involve:

- warehouse transfer;
- EWM staging;
- Kanban;
- line-side supply;
- production supply areas.

## Confirmation

Production reports:

- quantity produced;
- scrap;
- operation progress;
- time;
- resource use.

## Goods receipt

Finished or semi-finished products enter inventory.

Actual production results must update future planning.

## SAP Digital Manufacturing

SAP Digital Manufacturing is SAP’s current cloud manufacturing-operations platform.

SAP describes it as connecting ERP planning with shop-floor operations, coordinating labour, inventory, quality and maintenance, and supporting execution worklists, resource orchestration, standard work and production analytics.

### Role in the architecture

```text
IBP and S/4 planning
→ production order and schedule
→ SAP Digital Manufacturing
→ shop-floor execution
→ confirmations and actuals
→ S/4HANA and planning feedback
```

Digital Manufacturing does not replace demand planning or MRP.

It executes and reports what actually happens on the shop floor.

## Part XII: Warehouse replenishment and execution

After procurement or production, inventory must be received and positioned.

SAP EWM supports:

- inbound receipt;
- putaway;
- stock management;
- production staging;
- picking;
- internal replenishment;
- automation;
- inventory transparency.

## Inbound execution

The process may include:

```text
Purchase order
→ inbound delivery
→ carrier arrival
→ unloading
→ goods receipt
→ quality
→ putaway
```

A purchase order is not usable stock until the relevant execution steps complete.

## Production supply

EWM may stage components to:

- production supply area;
- work centre;
- line-side storage;
- Kanban location.

## Picking-location replenishment

Reserve stock may replenish a forward picking bin.

This should consider:

- minimum quantity;
- maximum quantity;
- expected outbound work;
- warehouse-task capacity.

## Inventory status matters

MRP may see inventory at plant level.

Warehouse execution knows whether it is:

- available;
- blocked;
- in quality;
- in a handling unit;
- in transit;
- physically inaccessible.

Integration between ERP and EWM must preserve the state required for reliable planning.

## Part XIII: aATP and demand fulfilment

MRP creates supply.

aATP decides what may be promised to demand.

These processes form a loop.

```text
Demand
→ ATP confirmation
→ MRP supply proposal
→ production or procurement
→ changed supply
→ backorder processing
→ revised confirmation
```

aATP may provide:

- Product Availability Check;
- Product Allocation;
- Supply Protection;
- Backorder Processing;
- Alternative-Based Confirmation.

MRP and ATP should not compete.

### MRP

Asks:

> What supply should we create?

### aATP

Asks:

> What supply may we commit?

## Part XIV: The complete end-to-end planning process

A modern process can be structured into fourteen steps.

## Step 1: Collect demand signals

Systems:

- SAP IBP;
- CRM;
- e-commerce;
- customer EDI;
- S/4HANA sales orders;
- external market data.

Output:

- historical and current demand signals.

## Step 2: Create statistical forecast

System:

- SAP IBP for Demand.

Output:

- baseline forecast;
- forecast error;
- product classification.

## Step 3: Create consensus demand

Participants:

- sales;
- marketing;
- demand planning;
- finance.

System:

- SAP IBP S&OP and Demand.

Output:

- approved demand plan.

## Step 4: Set inventory policy

System:

- SAP IBP Inventory;
- S/4HANA safety-stock or DDR parameters.

Output:

- safety-stock targets;
- service levels;
- decoupling buffers.

## Step 5: Build network supply plan

System:

- SAP IBP Response and Supply.

Output:

- production plan;
- distribution plan;
- sourcing requirements;
- capacity gaps.

## Step 6: Approve scenario

Participants:

- operations;
- finance;
- sales;
- procurement;
- management.

Output:

- approved constrained or management plan.

## Step 7: Transfer operational demand

Systems:

- IBP integration;
- S/4HANA Demand Management.

Output:

- PIRs;
- allocation parameters;
- operational requirements.

## Step 8: Run pMRP simulation where needed

System:

- SAP S/4HANA pMRP.

Output:

- capacity scenarios;
- make-or-buy analysis;
- early component risk.

## Step 9: Run MRP Live

System:

- SAP S/4HANA.

Output:

- planned orders;
- purchase requisitions;
- scheduling-agreement lines;
- stock-transfer proposals;
- exception messages.

## Step 10: Perform detailed planning

System:

- embedded PP/DS.

Output:

- finite schedule;
- resource sequence;
- detailed planned orders.

## Step 11: Execute procurement collaboration

Systems:

- S/4HANA Procurement;
- SAP Business Network.

Output:

- purchase orders;
- supplier confirmations;
- shipment notices;
- revised supply dates.

## Step 12: Execute production

Systems:

- S/4HANA production;
- SAP Digital Manufacturing;
- EWM staging.

Output:

- confirmations;
- goods consumption;
- finished goods;
- scrap;
- actual dates.

## Step 13: Execute warehouse and transportation

Systems:

- SAP EWM;
- SAP TM.

Output:

- stock placement;
- picking;
- shipment;
- actual delivery.

## Step 14: Feed actuals back

Systems:

- S/4HANA;
- IBP;
- analytics;
- Business Network.

Actuals include:

- demand;
- lead time;
- supplier reliability;
- production performance;
- inventory;
- service.

The process then begins again.

## Part XV: Which solution should be used for which problem?

## Scenario 1: Simple consumables

Characteristics:

- low value;
- stable usage;
- predictable supplier lead time.

Recommended:

- S/4HANA reorder-point planning;
- fixed or calculated lot size;
- basic purchase-order execution.

Do not introduce IBP or PP/DS only for this category.

## Scenario 2: Make-to-stock manufacturing

Characteristics:

- forecast demand;
- multilevel BOM;
- moderate constraints.

Recommended:

- IBP Demand where forecast complexity justifies it;
- PIRs in S/4HANA;
- MRP Live;
- standard capacity evaluation;
- production orders.

## Scenario 3: Constrained manufacturing

Characteristics:

- bottleneck machines;
- setup sequence;
- shared components;
- high service impact.

Recommended:

- IBP Response and Supply;
- MRP Live;
- embedded PP/DS;
- aATP;
- Digital Manufacturing.

## Scenario 4: Long global supply chain

Characteristics:

- many plants and warehouses;
- long supplier lead time;
- global inventory.

Recommended:

- IBP Demand;
- IBP Inventory;
- IBP Response and Supply;
- S/4HANA MRP;
- supplier collaboration;
- EWM and TM.

## Scenario 5: Volatile flow with long lead times

Characteristics:

- repeated MRP rescheduling;
- unstable demand;
- long cumulative lead time.

Possible approach:

- DDMRP or DDR for selected decoupling materials;
- traditional MRP between decoupling points;
- clear buffer management.

Do not convert the complete material portfolio to DDMRP without segmentation.

## Scenario 6: Automotive JIT/JIS supply

Characteristics:

- scheduling agreements;
- frequent releases;
- line-side supply;
- supplier collaboration;
- strict sequence.

Possible architecture:

- S/4HANA scheduling agreements and automotive processes;
- MRP for upstream planning;
- JIT/JIS or Kanban execution;
- Business Network collaboration;
- EWM production supply;
- PP/DS for constrained manufacturing.

## Scenario 7: Externally manufactured product

Characteristics:

- contract manufacturer;
- customer-owned components;
- supplier capacity;
- outsourced production.

Recommended:

- IBP network planning;
- S/4HANA subcontracting;
- Business Network manufacturing collaboration;
- component and finished-goods visibility.

## Scenario 8: Retail or distribution replenishment

Characteristics:

- many locations;
- fast consumption;
- local inventory targets.

Recommended:

- IBP demand and inventory planning;
- distribution replenishment;
- reorder-point or time-phased planning for selected products;
- EWM internal replenishment;
- aATP for customer commitment.

## Part XVI: Legacy SAP APO landscape and modern replacements

Many companies still think in terms of APO components.

| Legacy APO capability | Modern primary direction |
|---|---|
| APO Demand Planning | SAP IBP for Demand |
| APO Supply Network Planning | SAP IBP Response and Supply |
| APO inventory planning | SAP IBP for Inventory |
| APO PP/DS | Embedded SAP S/4HANA PP/DS |
| APO gATP | SAP S/4HANA aATP |
| SAP SNC supplier collaboration | SAP Business Network Supply Chain Collaboration |
| ERP classic MRP | SAP S/4HANA MRP Live |

This is not always a one-to-one migration.

A company should map business capability, not technical configuration.

For example:

- an APO SNP deployment heuristic may become IBP supply planning;
- a detailed production heuristic may move to embedded PP/DS;
- local product allocation may move to aATP;
- supplier forecast collaboration may move to Business Network.

## Part XVII: Applications planners actually use

Exact availability depends on S/4HANA and IBP release, edition and role.

## Demand planner

Typical applications:

- SAP IBP Excel add-in;
- SAP IBP Planner Workspaces;
- analytics and forecast applications;
- collaboration and alert views.

## Supply planner

Typical applications:

- IBP planning views;
- supply-plan simulation;
- response planning;
- alerts;
- network visualization.

## MRP controller

Typical S/4HANA applications may include:

- Monitor Material Coverage;
- Manage Material Coverage;
- Schedule MRP Runs;
- Material Documents Overview;
- Manage Planned Orders;
- Manage Purchase Requisitions.

## Production planner

Typical applications may include:

- Manage Production Orders;
- Capacity Scheduling Table;
- Manage Work Centre Capacity;
- PP/DS Product View;
- Detailed Scheduling Planning Board;
- production-planning run applications.

## Procurement planner

Typical applications may include:

- Manage Purchase Requisitions;
- Assign and Process Purchase Requisitions;
- Manage Purchase Orders;
- supplier confirmation monitoring;
- source-of-supply applications.

## Warehouse planner

Typical EWM applications include:

- warehouse monitor;
- replenishment monitoring;
- inbound and outbound workload;
- stock and bin management;
- production staging.

The application is not the process.

The same planner may use several applications to resolve one material shortage.

## Part XVIII: The most important master data

Planning quality depends more on master data than on algorithm selection.

## Product and location

- material;
- plant;
- MRP area;
- storage location;
- warehouse product.

## Demand settings

- planning strategy;
- consumption mode;
- PIR;
- forecast parameters;
- customer-order relevance.

## MRP parameters

- MRP type;
- lot-sizing procedure;
- safety stock;
- MRP controller;
- planning time fence;
- procurement type;
- special procurement;
- scheduling margin key.

## Procurement data

- planned delivery time;
- purchasing processing time;
- purchasing info record;
- source list;
- quota arrangement;
- contract;
- scheduling agreement.

## Production data

- BOM;
- routing or recipe;
- work centre or resource;
- production version;
- setup data;
- capacity;
- yield and scrap.

## Inventory data

- target stock;
- service level;
- buffer profile;
- decoupling point;
- reorder point;
- maximum stock.

## Logistics data

- transport time;
- calendars;
- goods-receipt processing;
- warehouse replenishment;
- packaging;
- handling constraints.

A powerful optimizer using the wrong lead time creates a more convincing wrong plan.

## Part XIX: Planning horizons and ownership

A good architecture assigns one owner per horizon.

| Horizon | Main owner | Primary system |
|---|---|---|
| Strategic network | Supply-chain leadership | IBP and strategic tools |
| Tactical demand | Demand planning | IBP Demand |
| Tactical supply | Supply planning | IBP Response and Supply |
| Inventory targets | Inventory planning | IBP Inventory |
| Operational material plan | MRP controller | S/4HANA MRP Live |
| Detailed production schedule | Production planner | Embedded PP/DS |
| Transactional promise | Order fulfilment | S/4HANA aATP |
| Supplier commitment | Procurement and supplier | S/4HANA + Business Network |
| Shop-floor dispatch | Manufacturing operations | Digital Manufacturing / local execution |
| Warehouse replenishment | Warehouse operations | EWM |

Two systems may support one process.

Only one should own the binding decision.

## Part XX: Common mistakes

### Mistake 1: Using MRP as the demand forecast

MRP executes demand.

It does not create a market forecast.

### Mistake 2: Sending an unconstrained forecast directly into production

The result creates impossible planned orders.

### Mistake 3: Expecting MRP to perform finite scheduling

Capacity overload remains unresolved.

### Mistake 4: Planning every material with the same MRP type

High-value components and screws receive the same logic.

### Mistake 5: Using reorder-point planning for volatile critical materials

Thresholds react too late.

### Mistake 6: Using full MRP for every low-value consumable

The system produces excessive planning noise.

### Mistake 7: Treating supplier requested dates as confirmed dates

The plan is built on unaccepted supply.

### Mistake 8: Maintaining safety stock without an owner

Buffers remain after demand and lead time change.

### Mistake 9: Activating DDMRP for the entire portfolio

Too many buffers create inventory and complexity.

### Mistake 10: Allowing IBP and S/4HANA to change the same plan independently

Planners lose trust in both.

### Mistake 11: Running PP/DS and MRP in the wrong sequence

Detailed schedules are overwritten.

### Mistake 12: Confusing supply-chain replenishment with EWM replenishment

The wrong team owns the problem.

### Mistake 13: Measuring MRP job completion

The job is green while shortages and expedites rise.

### Mistake 14: Optimizing forecast accuracy alone

The plan still fails because of supplier and capacity variability.

### Mistake 15: Automating proposals without exception governance

The company creates more orders faster but does not improve flow.

## Part XXI: KPIs that matter

## Demand

- forecast accuracy;
- forecast bias;
- demand-sensing improvement;
- forecast-value-add;
- planner override rate.

## Supply planning

- constrained demand fulfilment;
- capacity overload;
- supply-plan stability;
- scenario response time;
- allocation compliance.

## Inventory

- service level;
- inventory turns;
- days of supply;
- excess and obsolete stock;
- safety-stock effectiveness;
- buffer penetration.

## MRP

- shortage count;
- overdue proposals;
- rescheduling message volume;
- exception recurrence;
- proposal conversion rate;
- nervousness or date-change rate.

## Procurement

- supplier confirmation rate;
- requested-versus-confirmed date;
- purchase-order change rate;
- on-time delivery;
- emergency procurement.

## Production

- schedule adherence;
- capacity utilization;
- order lateness;
- component shortage;
- yield and scrap;
- sequence changes.

## Replenishment

- stockout rate;
- replenishment cycle time;
- emergency replenishment;
- picking-location availability;
- Kanban-loop performance.

## End-to-end

- first-confirmation reliability;
- OTIF;
- expedite cost;
- plan-to-actual lead time;
- inventory required per service unit;
- time from demand change to approved response.

## Part XXII: A practical target architecture

For a complex manufacturing company:

```text
SAP IBP for Demand
Forecast and demand sensing
            ↓
SAP IBP S&OP
Consensus and financial alignment
            ↓
SAP IBP Inventory
Inventory targets and network buffers
            ↓
SAP IBP Response and Supply
Constrained network supply plan
            ↓
SAP S/4HANA Demand Management
PIRs and planning strategy
            ↓
S/4HANA pMRP
Scenario and capacity risk
            ↓
S/4HANA MRP Live
Material and procurement proposals
            ↓
Embedded PP/DS
Finite production schedule
            ↓
S/4HANA Procurement + Business Network
Supplier commitment
            ↓
S/4HANA Production + Digital Manufacturing
Factory execution
            ↓
SAP EWM
Material staging and warehouse replenishment
            ↓
SAP TM
Physical transport
            ↓
Actuals returned to S/4HANA and IBP
```

For a simpler company:

```text
Sales orders and simple forecast
            ↓
S/4HANA PIRs
            ↓
MRP Live and reorder point
            ↓
Purchase orders and production orders
            ↓
Inventory and warehouse execution
```

The simpler architecture may be better when it covers the real problem.

## Questions managers should ask

1. Who owns the demand forecast?
2. Which demand becomes binding for MRP?
3. Do sales orders consume the forecast correctly?
4. Which products use deterministic MRP?
5. Which products use reorder-point or consumption planning?
6. Which products genuinely need DDMRP?
7. Who owns safety-stock and buffer parameters?
8. Does the supply plan include realistic capacity?
9. Which system creates the constrained network plan?
10. Which system owns the operational material plan?
11. Which products require PP/DS?
12. Can MRP overwrite the PP/DS result?
13. Are supplier dates requested or confirmed?
14. Does supplier collaboration update planning automatically?
15. Which proposals are firm and why?
16. How much planning noise is caused by outdated lead times?
17. Is warehouse replenishment aligned with production and outbound demand?
18. Are actual execution times returned to planning?
19. Do we measure plan stability or only plan creation?
20. Does every planning system have one clear decision responsibility?

## The management conclusion

The complete planning process is not:

```text
Run MRP
→ create orders
```

It is:

```text
Understand demand
→ agree the business plan
→ position inventory
→ balance supply and capacity
→ calculate material requirements
→ create a feasible schedule
→ obtain supplier commitment
→ execute production and logistics
→ learn from actual results
```

SAP IBP currently covers the cloud planning layer across S&OP, demand, inventory, response and supply, demand-driven replenishment and supply-chain visibility.

SAP S/4HANA provides operational demand management, predictive simulation, MRP Live, procurement proposals, production orders and embedded PP/DS. SAP’s official learning content treats MRP Live, pMRP, demand-driven replenishment and PP/DS as different but connected planning capabilities.

SAP Business Network Supply Chain Collaboration extends the process to suppliers through forecast, procurement, inventory, manufacturing and quality collaboration.

SAP Digital Manufacturing executes and monitors production operations, while SAP EWM controls detailed warehouse stock, staging, replenishment and automation.

The company does not need every application.

It needs a planning model where:

- IBP plans at the right aggregate and network level;
- S/4HANA converts approved demand into operational supply proposals;
- PP/DS protects constrained production;
- suppliers confirm what they can deliver;
- warehouses and factories execute the plan;
- actual results correct the next cycle.

The decisive question is not:

> Did MRP run successfully?

It is:

> Did the complete planning system convert real demand into reliable supply with acceptable inventory, capacity and service?

When the answer is no, running MRP more frequently usually creates faster planning noise.

It does not create a better supply chain.

---

### SAP demand, MRP, and replenishment architecture checklist

- [ ] Demand forecasting is separated from operational MRP.
- [ ] S&OP approves one demand and supply scenario.
- [ ] Inventory targets have a defined owner.
- [ ] Materials are segmented by replenishment method.
- [ ] Deterministic MRP is used for dependent and explicit demand.
- [ ] Reorder-point planning is limited to suitable stable materials.
- [ ] Forecast-based and time-phased planning have clear use cases.
- [ ] Kanban is used only where replenishment loops are stable.
- [ ] DDMRP decoupling points are selected analytically.
- [ ] Buffer sizes are reviewed dynamically.
- [ ] IBP Response and Supply owns network-level balancing.
- [ ] S/4HANA Demand Management receives approved requirements.
- [ ] pMRP is used for simulation, not execution.
- [ ] MRP Live owns operational material proposals.
- [ ] Lot-sizing parameters reflect real economics.
- [ ] Procurement types and sources are current.
- [ ] Planning time fences and firming have explicit policies.
- [ ] PP/DS is used only for constrained and sequence-sensitive products.
- [ ] MRP and PP/DS planning sequences do not overwrite each other.
- [ ] Supplier confirmations update the supply picture.
- [ ] Business Network collaboration has defined contractual meaning.
- [ ] Production actuals return to planning.
- [ ] EWM replenishment is separated from network replenishment.
- [ ] Warehouse stock status is visible to operational planning.
- [ ] aATP and MRP roles are clearly separated.
- [ ] One system owns each binding decision.
- [ ] Planning performance is measured through service, inventory and stability.
- [ ] A successful planning job is not confused with successful fulfilment.

### Sources and further reading

SAP currently describes SAP Integrated Business Planning as combining S&OP, forecasting and demand, response and supply, demand-driven replenishment, inventory planning and supply-chain visibility in one cloud planning solution.

SAP’s current IBP capabilities include demand sensing, statistical forecasting, multi-echelon inventory optimization, multilevel supply planning, constrained and unconstrained planning, rough-cut capacity and order-based response planning.

SAP’s official S/4HANA production-planning learning content describes deterministic and consumption-based planning, reorder-point planning, multilevel BOM explosion, net-requirements calculation, lot sizing, procurement-type determination, scheduling and the creation of planned orders and purchase requisitions.

SAP’s official Demand-Driven Replenishment learning content describes strategic decoupling points, buffer profiles, dynamic buffer adjustment, consumption-driven order generation and prioritization based on buffer penetration.

SAP’s official pMRP learning content describes simulation of demand, capacity, source-of-supply and multilevel material scenarios before changes are released to operational planning.

SAP’s official PP/DS learning content explains how MRP Live can combine standard S/4HANA MRP and advanced PP/DS planning for selected products, while requiring careful planning-run scope and sequence.

SAP Business Network Supply Chain Collaboration currently supports forecast commitments, purchase-order collaboration, inventory collaboration, scheduling agreements, supplier-managed inventory and manufacturing collaboration.

SAP EWM currently supports high-volume warehouse operations, stock and process transparency, production integration, slotting and warehouse automation. SAP Digital Manufacturing supports manufacturing execution, resource orchestration and feedback between ERP planning and shop-floor operations.

*Reviewed: July 2026. Availability, naming and licensing of SAP IBP, MRP Live, pMRP, embedded PP/DS, DDR, Fiori applications and Business Network capabilities depend on the SAP product edition and release. Final architecture should be checked against the exact deployed system and current SAP documentation.*
