
title: "**Zusammenfassung: Programm- und Systemverifikation**"
lang: en-GB
...

---

An dieser Zusammenfassung und der zugehörigen Formelsammlung kann gerne auf [Github](https://github.com/cornhead/zusammenfassungen.git) mitgewirkt werden!

---


* Fault: cause of an error
* Error: erroneous state, but not directly observable in behaviour $\rightarrow$ might lead to failure, but not necessarily
* Failure: deviation from expected behaviour

# Coverage

Coverage criteria state when enough testing has been done.

## Control Flow Based Coverage Criteria

### Path Coverage

Execute every path the program could take at least once.

Easy counter example to see that path coverage has not been reached are loops: every new loop iteration constitutes a new path and all paths have to be taken. Path coverage is generally not always reachable, e.g., it es not achievable for the [following program](#inf_loop):

~~~ {#inf_loop .c .number-lines}
while (1) {
	if ( getchar () == EOF )
	break ;
}
~~~

### Statement Coverage

Execute every statement of the program (merely syntactic) at least once.

Statement Coverage is implied by path coverage. Hence, if statement coverage can't be achieved, path coverage can't be achieved either. On the other hand, if path coverage can't be achieved for a given program, statement coverage still can be reached, as is the case in (above program)[#inf_loop]

If for a given program statement coverage can't be achieved, it is said to contain unreachable code:

~~~ {.c .number-lines}
if (false){
	...
}
~~~

### Branch Coverage

Execute every branch at least once.

In literature, the definitions of branches are rather imprecise $\rightarrow$ what about unconditional jumps, `goto`, function calls or fall-throughs?

### Condition Coverage

Exercise every boolean sub-expression/atom/condition outcome (but their values do not necessarily have to affect the overall outcome)

Condition coverage does not imply descision coverage, as can be seen by the following program, with the test cases $\{x=5, y=-3\}$ and $\{x=-1, y=2\}$

~~~ {.c .number-lines}
if ( ( x > 0) && ( y > 0) )
	x++;
~~~

All outcomes of the sub-expressions are exercised once but the decision never evaluated to `true`.

### Modified Condition / Decision Coverage (MC/DC)

Every condition in a decision has to have taken affect on the outcome at least once. (see the stuck-at error model in the lecture on digital design)

MC/DC is defined in DO-178B (high relevance in industry)

### Multiple Condition Coverage

For $n$ sub-conditions in a decision, try all $2^n$ combinations.







## Data Flow Based Coverage Criteria

* Definitions: assignment of a value to a variable
* Use: statement where the value of a variable is read
	* C(omputation)-Use: defines/computes other variables
	* P(redicate)-Use:  within conditional statements


------------------------------------------------------------------------
                  Name         Criteria
----------------------         -------------------------------------------------------------
              all-defs         all definitions get used at some point

            all-c-uses         one path from a definition to each c-use that is affected by that definition

            all-p-uses         one path from a definition to each p-use that is affected by that definition

all-c-uses/some-p-uses         same as all-c-uses, but if there are no c-uses, than at least one affected p-use needs to be triggered

all-p-uses/some-c-uses         same as all-p-uses, but if there are no c-uses, than at least one affected c-use needs to be triggered

              all-uses         all-c-uses and all-p-uses $\rightarrow$ all uses need to be executed

          all-du-paths         same as all-uses, but all possible du paths have to be taken at least once, not just one path
------------------------------------------------------------------------

Table: Data Flow Criteria

![subsumption lattice](./img/psv_subsumption_lattice.png){.width=50%}





## Mutation Testing

# Automated Test Case Generation


# Examples

## Coverage

\pagebreak

### Example 1, taken from the exam in June 2017

Consider the following program fragment and test suite:

~~~ {.c .number-lines}
bool prime (unsigned n){
	bool result = true;				//	  Test Suite
	unsigned i = 2;					//	---------------
	while ((i != n) && result){		//	 n     result
		if (n % i == 0)				//	----   ------
			result = false;			//	 0     false
		else						//	 3     true
			i = i + 1;				//	 42    false
	}								//	---------------
	return result;
}
~~~

#### A) Control flow based criteria

Indicate (X) which of the following coverage criteria are satisfied by the test-suite above (assume that the term “decision” refers to all non-constant Boolean expressions in theprogram).

---------------------------------------------
                  Criterion     Satisfied     Not Satisfied
---------------------------    -----------   ---------------
              path coverage                         X

         statement coverage        X

            branch coverage        X

          decision coverage        X

 condition/decision coverag        X
----------------------------------------------


#### B) Data flow based criteria

Indicate (X) which of the following coverage criteria are satisfied by the test-suite above(here, the  parameters of the function do not constitute definitions, and the return statements are c-uses)

---------------------------------------------
                  Criterion     Satisfied     Not Satisfied
---------------------------    -----------   ---------------
                   all-defs         X
                   
                 all-c-uses                         X
                 
                 all-p-uses         X
                 
     all-c-uses/some-p-uses                         X
     
     all-p-uses/some-c-uses         X
----------------------------------------------



\pagebreak

### Example 2, taken from the exam in June 2018

Consider the following program fragment and test suite

~~~ {.c .number-lines}
bool range_check (unsigned m, unsigned n){
	if (m > n){
		unsigned t = m;					//	  Test Suite
		m = n;							//	---------------
		n = t;							//	 m   n   result
	}									//	--- ---  ------
	bool result = false;				//	 3   7   true
	bool tmp = true;					//	 1   0   false
	unsigned i = m;						//	 2   5   true
	while ((i > 0) && (i < n)){			//	---------------
		i = i + 1;
		if (i % m == 0)
			result = result || tmp;
	}
	return result;
}
~~~

#### A) Control flow based criteria

Indicate (X) which of the following coverage criteria are satisfied by the test-suite above (assume that the term “decision” refers to all non-constant Boolean expressions in theprogram).

---------------------------------------------
                           Criterion     Satisfied     Not Satisfied
------------------------------------    -----------   ---------------
                  statement coverage         X

                     branch coverage         X

                   decision coverage         X

modified condition/decision coverage         ?
---------------------------------------------

#### B) Data flow based criteria

Indicate (X) which of the following coverage criteria are satisfied by the test-suite above (here, the parameters of the function do not constitute definitions, and the return statements are c-uses).

---------------------------------------------
                  Criterion     Satisfied     Not Satisfied
---------------------------    -----------   ---------------
                   all-defs         X
                   
                 all-c-uses                         X
                 
                 all-p-uses         X
                 
     all-c-uses/some-p-uses                         X
     
     all-p-uses/some-c-uses                         X
----------------------------------------------
