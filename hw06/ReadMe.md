I kept my name on the same project as last week.

I watched Julia's video and answered the questions below.

Questions:

1) Where does Julia Cartwrige work?
    National Instruments

2) What is PREEMT_RT?
    Real Time Linux Kernel Patch

3) What is mixed criticality?
    The mix of time intensive tasks and non time intensive tasks running 
    together and communicate.

4) How can drivers misbehave?
    They can misbehave because they have a shared kernel, scheduler, and stack 
    between RT tasks and non-RT tasks.

5) What is the delta in Figure 1?
    The delta represents the latency between the event and the application 
    launch.

6) What is Cyclictest [2]?
    take a timestamp, sleep for set duration, then take another time stamp
    the difference between the two timestamps is the actual time slept
    subtract the set duration from this to find the latency.

7) What is plotted in Figure 2?
    Figure 2 shows two results of the Cyclictest using preempt and preempt_rt.

8) What is dispatch latency? Scheduling latency?
    Dispatch latency is the difference between hardware firing and thread 
    scheduler being told what thread to running. Scheduling latency is the 
    difference between scheduler knowing what thread to run and the thread 
    actually being run.

9) What is mainline?
    Mainline is the single process that is running, which could contain multiple
    threads being switched on and off of the process.

10) What is keeping the External event in Figure 3 from starting?
    It can't be scheduled until the lower priority thread (interrupt) finishes.

11) Why can the External event in Figure 4 start sooner?
    It is now preemptive, because the irq interrupt goes to a small temporary 
    thread that allows higher priority, tasks to be placed on the process over 
    smaller priority threads.
    

I also did the PREEMT_RT exercise. The make file would not work so I ran an
infinint while loop. When the command was done running I got these values:

real    1m40.225s
user    0m1.000s
sys     0m2.117s

When I ran it in real time I got these values:

real    1m40.203s
user    0m0.728s
sys     0m2.350s

Then I ran it without any load. At first I got these values:

real    1m40.214s
user    0m0.551s
sys     0m1.768s

Then in real time I got these values:

real    1m43.413s
user    0m0.764s
sys     0m1.724s

The two plots with load are in a file called withLoad.png and the two plots
without load are in a file called noLoad.png.

