
#this is a detailed explanation of ebpf hello world program!
#use bcc python framework for now , as it is a very easy way to write ebpf basic programs
#refer to "https://github.com/lizrice/learning-ebpf" for more details!

#!/usr/bin/python

from bcc import BPF
program = r """
int hello (void *ctx){
bpf_trace_printk("Hello World!");
return 0;
}
"""
b=BPF(text=program)
syscall = b.get_syscall_fnname("execve")
b.attach_kprobe(event=syscall, fn_name="hello")
b.trace_print()

