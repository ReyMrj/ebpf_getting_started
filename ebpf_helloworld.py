
#this is a detailed explanation of ebpf hello world program!
#use bcc python framework for now , as it is a very easy way to write ebpf basic programs
#refer to "https://github.com/lizrice/learning-ebpf" for more details!
#just so you know , this code consists of two parts , the ebpf program that will run in the kernel and ofcourse the userspace program that loads the ebpf prgrm into the kernel and reads out the trace that it generates



#!/usr/bin/python this is a python code run by the python interpreter 

from bcc import BPF

#here starts ebpf code , it's written in c , bfp_trace_printk is a helper function used by epbf to interact with the system , and the entire ebpf program is defined as a string "program" in the python code , the c program is compiled tehn excuted by BCC 
program = r """

int hello (void *ctx){ 
bpf_trace_printk("Hello World!"); 
return 0;
}
"""
b=BPF(text=program) # here , all u need to do is pass the string "program"as a parameter when creating BPF object
syscall = b.get_syscall_fnname("execve") #here we are attaching ebpf program to an event that is the system call execve, use to excute a prgrm! , basically whenever anyone or anything strats a program that excutes on this machine , execve() will be called which will trigger the ebpf program 
#but why b.get_syscall_fnname? becuz execve is the standard interfac ein linux but we want to use bcc to get the name of the function that implements it in the kernel , it actually depends on the chip architecture of the machine
b.attach_kprobe(event=syscall, fn_name="hello")# now , deal with syscall as the name of the function in the kernel. now just use a kprobe to attach hello function(our ebpf prgrm) to that event
#congrats, at this point ur ebpf program is loaded into the kernel and attached into an event, whenever a new executable gets launched on the machine ur prgrm will be triggered
b.trace_print()#this is the remaining python code to read the output of the tracing by the kernel and write it on the screen
# trace_print() function will loop indefinitely until u stop the program , use ctrl+c




