**Programming Concepts**  
> 1. **Heuristics:** Algorithms where you don't have any gaurantee on the quality of the algorithm.
> 2. **Approximation algorithms:** Normally the approximation algorithms are designed for NP-hard and NP-Commplete problems so as to get an efficient algorithm and to get a good bound.

> **Minimum Makespan Schedulling:**  
> **Problem:** Given a set of *n* jobs and their processing times p<sub>1</sub> ,..., p<sub>n</sub> and integer *m* find an assignment of jobs to m identical machines so that the completion time is minimized.  
>> **2-approximation algorithm steps**  
>> 1. Order the jobs arbitrarily
>> 2. Schedule the jobs in such a way that the next job to be processed is fed to the machine with the lowest load. 

**%matplotlib inline**  
- It is a python magic function [magic function : Magics are useful as convenient functions where python syntax is not the most natural one. or when one want to embed invalid python syntax in their workflow] With this command, the output of plotting commands is displayed inline within frontends like the jupyter notebook, directly below the code cell that produced it.
