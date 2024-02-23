0x05 Processes and Signals


Understanding Processes and Signals

Introduction
This README provides a brief overview of processes and signals in Unix-like operating systems

Processes
What is a Process?

A process is an instance of a running program on a computer system. It consists of the program code, data, and resources allocated by the operating system

Process ID (PID)

Every process is identified by a unique numerical identifier called the Process ID (PID). PIDs are assigned by the operating system and are used to manage and control processes

Finding a Process' PID

You can find the PID of a process using commands like ps, pgrep, or pidof in the terminal

Terminating a Process

To terminate a process, you can use the kill command followed by the PID of the process you want to terminate. Alternatively, you can use pkill to kill processes based on their name or attributes

Signals
What is a Signal?

A signal is a software interrupt delivered to a process to notify it of an event or to instruct it to perform a specific action. Signals are used for inter-process communication and process management
