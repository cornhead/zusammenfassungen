
title: "**Zusammenfassung: Dependable Systems**"
...


# Basics

## Allgemeine Begriffe und Definitionen

* Definition of dependability[^def_dependability]:
	* original: Dependability is the ability to deliver service that can justifiably be trusted.
	* alternative: Dependability of a system is the ability to avoid service failures that are more frequent and more severe than is acceptable.
	* note: both definitions do not require that a system never fails, but it must not fail too often or with unacceptable consequences

* System: an entity that is interacting with other entities
* Environment (of a system): the sum of all other systems that a given system is interacting with
* Boundary (of a system): the common frontier between a system and its environment
* Function (of a system): describes what a system is inteded to do
	* defined in functional specification
* Behavior (of a system): describes what a system does in order to implement its function
	* described as a sequence of states
* Structure (of a system): enables the system to generate its behavior ...?
	* often the structure consists of multiple components that are bound together to interact
	* components may consist of subcomponents themselves. Otherwise, they are called *atomic*

A system is the *provider* of a *service* to one or many *users* (which again are systems).

* Service Interface (between a provider and the users): the respective part of the boundary of the provider
* External State: the part of the providers state that is perceivable at the service interface
* Internal State: the part of the providers state that is not external
* Use Interface: the interface interface at which the user receives the service of the provider

[^def_dependability]: IEEE: "Basic concepts and taxonomy of dependable and secure computing", ([Link](https://ieeexplore.ieee.org/document/1335465))

## Fault, Error, Failure

* Correct Service: is delivered when the system implements its function as specified
* (Service) Failure: the event of a service deviating from correct service
	* more precisely, a failure is the transition from correct to incorrect service
* Failure Modes: describe different kinds of service failure
	* failure modes can be ranked by *failure severity*

A **failure** means that at least one external state of a system deviates from the correct state (i.e. as according to the functional specification). This deviation is called **error**. The adjudged or hypothesized cause of an error is called a **fault**.

(The explanation of fault, error and failure given in "Programm- und Systemverifikation" is much clearer and less ambiguous, especially regarding the definition of errors.)

An error is *detected* if its presence is indicated by an error message, error signal, etc. Otherwise, it is called *latent*.

Whether or not an error leads to a failure depends on

* the system composition and the existence of (possibly unintended) redundancy
* the system activity; for instance, the erronious state may be overwritten
* the definition of failure from the users viewpoint

### Fault-Error-Failure-Chain

A fault that has not been activated by the computation process is called *dormant*.
If a fault is activated, it produces an error.

An error that has not been recognized is called *latent*.
If an error "passes through" it causes a failure.

A failure may cause a fault for a system that interacts with the component &rarr; chain continues on next hierarchy level

### State transition chart

// insert illustration from slide 38

## Attributes of Dependability:

* Reliability: the probability that a system will conform to its functional specification throughout a time period of duration $t$.
* Availability: the percentage of time for which the system will conform to its specification (also considering repair actions)
	* Availability can be expressed as a function of reliability and maintainability
* Maintainability
* Safety: the probability that a system does not exhibit specified undesired behavior throughout a time period of duration $t$.
	* often security is accounted to security: most important security target: CIA triade
* Integrity

### Reliability vs Availability

Take, for instance, factory automation. Availability is the most important paramter of that system, because it determines the throughput of the factory. Reliability, on the other hand, is not that important because short down-times can be tolerated if the system has good maintainability.

When considering a satellite, however, reliability is the most important parameter because once the satellite has deviated from correct behavior, it will potentially stay that way indefinitely (i.e. it has very low maintainability).

### Reliability vs Safety

Reliability describes that a system adheres to its functional specification while safety describes that it does not exhibit specific undesired behavior that usually may cause harm to the lifes of people, the environment, valuables or so forth. In general not all deviations from the functional specification imply such behavior. For instance, take a railway system: if a certain signal is turned to red, the train will simply stop. This state is considered safe since a standing train cannot cause collisions. However, if the function of the overall system requires the train to arrive at a certain station, then keeping the signal on red would lead to a failure.

A different example: for a fly-by-wire system, reliability and safety are roughly the same because almost every failure of the system could have fatal consequences.

## Life Cycle of a System

* Development Phase
	* System conception
	* Design, development, verifaction, validation
* Use Phase
	* Service delivery
	* Service outage
	* Service shutdown
	* Maintenance

## Classification of Faults

Faults can be classified by

* Phase of creation or occurrence (development vs. use phase)
* System boundaries (internal vs. external)
* Phenomenological cause (natural vs. human-made)
* Dimension (hardware vs. software)
* Objective (malicious vs. non-malicious)
* Intent (deliberate vs. non-deliberate)
* Capability (accident vs. incompetence)
* Persistence (permanent vs. transient)

For example, a typical software bug comes into being in the development phase, is internal, human-made, a software flaw, non-malicious (if it's a minor bug), undeliberate, could be both an accident or a result of incompentency and is permanent.

Three of the classes mentioned above are of particular importance:

* faults in the development phase &rarr; "Development Faults"
* faults that are outside of the system boundary &rarr; "Interaction Faults"
* faults that lie in the hardware domain &rarr; "Physical Faults"

## Classification of Failures {#classification_of_failures}

Failures can be classified by

* Domain
	* Content failures
	* Early or late timing failures
	* Halt failure
		* no system acitivity is perceptible
		* special mode of halt failure: fail silent; no service is delivered at all
	* Erratic Failure
		* e.g. babbling idiot failure
* Consistency:
	* Consistent failure: all users perceive the same system behavior
	* Inconsistent failure: different users may perceive different behavior
* Consequences:
	* minor: slight reduction of safety margins
	* major: significant reduction of safety margins
	* hazardous: large reduction of safety margins and/or functional capabilites
	* catastrophic

## Means to attain dependability (and security)

* Fault Prevention: takes place in both hardware and software
* Fault Tolerance: see below
* Fault Removal: see below
* Fault Forecasting: estimate present number, future incidents and likely consequences of faults

### Fault Tolerance

Four phases:

* error detection
* damage confinement
* recovery (more on that later)
* fault treatment and continued service

#### Error Recovery

Backwards recovery:

* system state is reset to a previously stored error-free system state
* the failed processing sequence is reexecuted
* typical for data base systems

Forwards recovery:

* system state is set to new error-free system state
* typical for realt time systems with periodic processing patterns

### Fault Removal

* verification: check whether system adheres to specification; Static analysis / Dynamic Analysis
* diagnosis: once a (potential) failure has been found by the verifaction, the fault is diagnosed
* correction: the fault can then be removed

## Redundancy

In order to tolerate faults, a system requires some form of redundancy. This redundancy can be implemented in three different domains

### Redundancy in the Domain of Information

Redundant information, e.g. error correcting codes, robust data structures, etc.

### Redundancy in the Domain of Space

replicating components, e.g. using two CPUs instead of one

* active redundancy: only possible with fail silent components
* triple modular redundancy (TMR): three replicas of component and one voter that analyses the output
* passive or standby redundancy: multiple replicas but only one is used at a time; when failure occurs, switch to different replica
		* hot standby: standby component is operating the whole time &rarr; fast switching
		* cold standby: component is only activated on failure

### Redundancy in the Domain of Time

multiple calculations:

* replication of computations (possibly by a different algorithm or unit)
* checking results by acceptance test or voting

sending messages mutliple times:

* retransmission in case of failure, positive acknowledge or retransmit (PAR)
* message transmission is always repeated n times (reduces temporal uncertainty)

# Mathematical Models

Reliability and Failure Probability:

* $Q(t)$ ... Failure probability: the probability that a system will _not_ conform to its specification throughout $[0, t]$
* $R(t)$ ... Reliability: the probability that a system _will_ conform to its specification throughout $[0, t]$

$R(0) = 1$, $R(\infty) = 0$, $R(t) = 1-Q(t)$

Failure Probability Density Function:

$f(t) = \dfrac{dQ(t)}{dt} = - \dfrac{dR(t)}{dt}$

## Failure Rate:

$\lambda(t) = \dfrac{f(t)}{R(t)} = - \dfrac{dR(t)}{dt}\cdot\dfrac{1}{R(t)}$
Unit: FIT (failures in time) $:=$ 1 failure in $10^9$ hours

### Constant Failure Rate

A constant failure rate is often used to model the normal-life period of the bathtub curve, i.e. the middle part.

* $\lambda(t) = \lambda$ (const.)
* $\Rightarrow f(t)=\lambda e^{-\lambda\cdot t}$
* $\Rightarrow R(t)=e^{-\lambda\cdot t}$

### Weibull Distributed Failure Rate

A Weibull distributed failure rate can be used to model infant mortality and wear out periods of components, where $\alpha$ describes if the failure rate descreases over time ($\alpha < 1$), stays constant ($\alpha = 1$) or increases over time ($\alpha > 1$).

* $\lambda(t) = \alpha\lambda(\lambda t)^{\alpha-1}$
* $\Rightarrow f(t) = \alpha\lambda(\lambda t)^{\alpha-1} \cdot e^{-(\lambda t)^\alpha}$
* $\Rightarrow R(t) = e^{-(\lambda t)^\alpha}$

### Lognormal Distributed Failure Rate

A lognormal distributed failure rate is often used to model semiconductors

* $\lambda(t) = \dfrac{f(t)}{R(t)}$
* $f(t) = \frac{1}{\sigma t \sqrt{2\pi}} \cdot e^{-\frac{1}{2}\left(\frac{ln(t)-\mu}{\sigma}\right)^2}$
* $R(t) = 1 - \frac{1}{\sigma \sqrt{2\pi}} \cdot \int \limits_0^t \frac{1}{x}e^{-\frac{1}{2}\left(\frac{ln(t)-\mu}{\sigma}\right)^2} dx$

## Probabilistic Structure-Based Modeling

Assumption: 

* identifiable (independent) components
* failure rate of components known
* system can be described by its components and their interconnection

### Simple and Arbitrary Block Diagram


For simple block diagrams, one further assumption has to be made: The system consists ony of serial and parallel connections of components.

Serial connections:

$R_{ser.}(t) = \prod\limits_{i=0}^{n-1}R_i(t) = 1 - \prod\limits_{i=0}^{n-1}\left(1-Q_i(t)\right)$

Parallel connections:

$Q_{par.}(t) = \prod\limits_{i=0}^{n-1}Q_i(t) = 1 - \prod\limits_{i=0}^{n-1}\left(1-R_i(t)\right)$

For constant Failure Rate:

* $\lambda_{ser.} = \sum\limits_{i=0}^{n-1}\lambda_i$
* For serial blocks, failure rate remains constant. For parallel blocks, however, failure rate is generally not constant and formula is not as tidy.

On the upside, simple block diagrams allow for very easy mathematics when dealing with constant failure rates. On the downside however, we are restricted to serial and parallel connections only, maintenance cannot be modeled and it is only suited for active redundancy and fail-silent components. So let's extend the model!

Extension to arbitrary block diagrams:

* arbitrary connections between blocks
	* system reliability is calculated by means of the inclusion-exclusion-principle: add up all paths that lead to output, subtract paths that were added multiple times and so forth
* TMR: certain number of parallel components need to work for the voter to detect right result
	* e.g. for 2 out of 3 components, reliability can be calculated as R_{TMR} = $R_A R_B R_C + (1-R_A) R_B R_C + R_A (1-R_B) R_C + R_A R_B (1-R_C)$
	* not taken into account: reliability of voter and validity of fail-silent assumption
* switches for passive stand-by redundancy: component A is used unless A is detected to behave erroneous, then B is used
	* reliability is higher than active redundancy with two components as long as the error detection rate and the reliability of the switch are very high. Otherwise, the reliability drops below that of the active redundancy.

still not taken into account: maintainability

## Maintainability

Mean Time To Failure (MTTF): $MTTF = \int\limits_{0}^{\infty}t\cdot f(t)dt$

Applied to constant failure rate:

* $MTTF = \int\limits_{0}^{\infty}t\cdot \lambda e^{-\lambda t} dt = \lambda^{-1}$
* $MTTF_{ser.} = \dfrac{1}{\lambda_1 + \lambda_2 + \cdots + \lambda_n}$


Meant Time To Repair (MTTR): $MTTR = \int\limits_{0}^{\infty}t\cdot f_r(t)dt$

Repair Rate (analogous to failure rate): $\mu(t)$ (commonly assumed to be constant)

For consant repair rate: $MTTR = \mu^{-1}$

Mission time $t_m$: during mission, no repair is possible

Mission Reliability: $R(t_m)$ 

Note: The choice of a fault-tolerant architecture depends on the mission time. A single (non-fault-tolerant) component actually has higher reliability for short mission times than TMR, up to a certain point beyond which TMR outperforms the single component.

Steady State Availability (A): $A = \dfrac{MTTF}{MTTF+MTTR}$

Without maintenance and repair: $MTTR = \infty \Rightarrow A=0$

Mission availability: $A_m = \frac{1}{t_m} \int \limits_{t=0}^{t_m} R(t) dt$

## Markov Models

General properties:

* Suitable for modeling of:
	* arbitrary structures(active, passive and voting redundancy)
	* systems with complex dependencies (assumption of independent failures is no longer necessary)
	* coverage effects
* Markov property: The system behavior at any time instant $t$ is independent of history (except for the last state)
* Restriction to constant failure rates 

As with all models, there are two phases:

* Phase I: building the model
	* identify relevant system states
	* determine transition rates (either failure or repair rates)
* Phase II: evaluating
	* either analytically by solving a system of differential equations
	* or numerically, as with PRISM or other tools

The affects of maintenance increased the MTTF of a system with two *active* redundant components by a factor of 34, while increasing the MTTF of a system with *passive* redundancy by a factor of 51.

What also can be modeled with markov models is assumption coverage: So far we have assumed that components are fail-silent, which is necessary for active redundancy. But if this assumption is not met, active redundancy may fail.Therefore, we intruduce the factor of assumption coverage $c$, which can be used for further transitions that lead directly to a failure of the active redundant system.

To model safety, we can differentiate between states in which the system has failed and states that are deemed unsafe.

## Generalized Stochastic Petri Nets (GSPN)

Markov models offer only very limited mechanisms, hence, they tend to become rather complex. Since GSPN offer richer mechanisms, the model is often tidier.

Following steps have to be carried out when modeling a GSPN:

* model contruction
* model validation: does the model really represent the system at question
* definition of performance indices: definition of markings and transition firings
* conversion to markov chain
* analysis on markov chain

The last two steps can be executed fully automatically.

GSPNs are well suited for simulation but complex models are computationally expensive.

## Open Issues of Probabilistic Structure-Based Modeling

* high level of abstraction $\Rightarrow$ large gap between system and model
* time consuming, error prone and unintuitive
* small changes in system can lead to large changes in model
* model validation for ultra-high dependability

Also, this approach is not suited for software for the following reasons

* software does not have well defined individual components
* complexity of software structures is very high
* assumption of independent failures is too strong
* real-time aspects are not captured
* parallelism and sychronization are not considered (except for GSPNs)

# Reliability Growth Models

The essential idea of reliability growth models is to determine the reliability of an already built system by means of clever testing and correction of faults.

* System is treated as blackbox $\Rightarrow$ no need to identify separat components
* Iterative improvement process: test &rarr; correct &rarr; re-test
* Goals of Reliability growth models:
	* desciplined and managed process for reliability improvement
	* extrapolate the current reliability status to future results
	* assessing the magnitude of the test, correction and re-test effort
* Allows modeling of wear-out and design faults
* Can be used for both hardware and software
* Downsides:
	* Accuracy of models is very variable
	* No single model can be trusted to behave well under all circumstances (as with all types of models)

Usually, a probabilistic model with unknown parameters is built first, then statistical inference procedures are used to determine the unknown parameters, then predictions about future behavior can be made.

// todo: insert table comparing all sorts of models

# Limits of Validation for Ultra-High Dependability

The frequency of very rare events -- e.g. catastrophic events during flight that may only occur every $10^9$ h -- cannot be tested experimentally, so we have to resort to models for validation.


# Certification, Processes and Standards

## Generic Characteristics of Development Processes

The aim of development processes is to minimize the likelihood for *development faults*.

Interesting example: Since the DO-178B standard ("Software Considerations in Airborne Systems and Equipment Certification") was introduced in the 90s, not a single lethal incident has occured that could be traced back to development fault in software.

Typically, development processes can be understood as a V-shape, where the left branch describes the development from top to bottom and the right branch the verification from bottom to top. (Compare this to the design process as described in "Hardware Modeling".)

Important elements of development processes for dependable systems are *peer reviews* and *auditing*. A key property is the *traceability* of requirements down to their implementations and up again to the requirement during verification. For traceability to be possible, requirements are tagged. Those tags are then used on every abstraction layer to show where a certain requirement is fulfilled, e.g. a line in the source code might have a comment with a respective tag.

Side-note: There is a distinction between validation and verification. Validation: "Do I build the right system?"; Verification: "Do I build the system right?"

## Certification

Different certificates certify different thins, e.g. there are certificates over certain properties of a product and there are other certificates that a company adheres to certain standards.

## Standards

Standards specify the individual steps of a development process and the requirements on the safety managment. Most standards for dependable systems identify *criticallity classes* that map the highest acceptable frequency and severity of failures onto a certain scale.

Standards also include safety life cycle considerations. A complete framework for the safety life cycle consists of:

* definition of defferent life cycle phases
* specification of which activities to perform in each phase
* specification of which inputs to provide to each of the activities
* requirements on which results to achieve

Methods used in standards can either be prescriptive or performance oriented:

* Prescriptive:
	* product prescriptive: states what features should be implemented in a product
	* process prescriptive: states how a product should be developed
* performance-oriented: specifies certain performance thresholds which a product must meet

### Safety Integrity Levels (as defined in IEC 61508)

* Safety Function: the function that is intedet to achieve or maintain a safe state for the EUC (equipment under control) in case of a specific hazardous event.
* Safety Integrity: the probability that the safety function is executed satisfactorily under all stated conditions within a stated period of time.
* Safety Integrity Level (SIL): a discrete level corresponding to a range of safety integrity values.

The SIL in IEC 61508 is determined by frequency and severity of accidents. In ASIL (automotive SIL), the SIL is determined with the additional factor of controllability. In standards for aircrafts (e.g. ARP, DO 178, DO 254) the Design Assurance Level (short DAL, same concept as SIL) is determined only via the affects on the aircraft itself.

// todo: further summary of different standards?

## Common Cause Analysis

The Common Cause Analysis (CCA) aims to indentify design errors that may invalidate the subsystem failure independence assumption, which is required by most modeling techniques and the (P)SSA (preliminary system safety analysis).

There are three types of CCA:

* Zonal Safety Analysis: should examine each physical zone of an aircraft to ensure that equipment installations and potential physical interference with adjacent systems do not violate the independence requirements. For instance, if there are redundant replicas of a component, the replicas should be distributed over multiple zones so that a collision does not affect all of the replicas at once.
* Particular Risk Assessment
* Common Mode Analysis: provides evidence that the failures assumed to be independet are truly endependent. Covers effects of design, manufacturing and maintenance errors. 


# Failure Modes and Models

## Failure Mode Hierarchy

The failure modes introduced [above](#classification_of_failures) are cannonical. However, there are other ways to classify failure modes:

Ordered from weakest to strongest assumption about erratic behavior:

* Byzantine failure: no assumptions. component might also forge messages of other components &rarr; "babbling idiot"
* Authentication detectable byzantine: the only restriction is that a component cannot forge other components messages
* Performance failures: a system delivers correct results in the value domain but does not adhere to its temporal specifications, so either the result is to early or to late
* Omission failures: results may be omitted; extreme case of performance failure with infinite delay of message delivery
* Crash failures: if an omission failure has ocurred once, the system stops delivering any subsequent results
* Fail-stop failures: the component crashes but other systems can detect that it has cashed; also, the last correct state is preserved (in a stable storage)

## Fault Hypothesis, Failure Semantics and Assumption Coverage

* Fault Hypothesis: specifies anticipated faults which a server must be able to handle
* Failure Semantics: ?
* Assumption Coverage: the probability that the possible failure modes defined by the failure semantics proves to be true in practice

The specification of suitable fault hyptheses, failure semantics and required assumption coverage is crucial to the system design. If an assumption is violated, the system might fail as a whole. For instance, the RMS Titanic was built to stay afloat if less or equal to four underwater compartments were flooded. Unfortunately, the iceberg damaged five of the compartments.

# Sefety Analysis

Usually includes:

* Which? (Hazard Analysis)
* How? (Accident Sequencing)
* How likely? (Quantitative analysis)

## Preliminary Hazard Analysis (PHA)

The first step in any sefety program is to identify hazards and to categorize them with respect to criticality and probability

* define system hazards
* define critical states and failure modes
* identify critical elements
* determine consequences of hazardous events
* estimate likelihood of hazardous events
* issues to be analyzed in more detail

## Hazards and Operability Study (HAZOP)

The core idea is to identify intentions of a system and then search for possible deviations thereof that may cause hazards during system operation.

* Intention: for each part of the system a specification of the intention is made
* Deviation: search for deviations from intended behavior which may lead to hazards
* Guide Words: while doing so, a list of guide words is covered, e.g. no, not, more, less, as well as, part of, reverse, other than
* Team: this is done by a whole team rather than an individual. Usually the team consists of specialists of different fields
* Consequences: identify potential consequences of those deviations

Example:

Intention: pump a specified amount from tank A to reaction tank B.

* NO / NOT:
	* There is no fluid left in tank A
	* One of the pipes is blocked
* MORE:
	* The pump has to high capacity
	* Tank B could get overfilled
* AS WELL AS:
	* Valve 1 is open, as well as valve 2 &rarr; wrong fluid is being pumped





\vspace{2cm}

---

**Diese Zusammenfassung ist noch sehr unvollständig. Bei Interesse kann sie auf [Github](https://github.com/cornhead/zusammenfassungen.git) erweitert werden. Mitwirken ist ausdrücklich erwünscht!**

---
